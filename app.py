import csv
from flask import Response
from flask import Flask, render_template, request
from utils.parser import extract_text_from_pdf
from utils.skills import extract_skills
from utils.ranking import calculate_match
from utils.recommendations import generate_recommendations
from utils.analyzer import analyze_resume
from utils.experience import extract_experience
from utils.education import extract_education
from utils.projects import extract_projects
from utils.certifications import extract_certifications
from utils.section_parser import extract_sections
from utils.recruiter import rank_candidates
from utils.openrouter import generate_ai_feedback
from utils.pdf_report import create_pdf
from markdown import markdown

import os

last_candidate = {}

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ---------------------------------------
# Home
# ---------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------------------------------
# Recruiter Dashboard
# ---------------------------------------

@app.route("/recruiter")
def recruiter():
    return render_template("recruiter.html")


# ---------------------------------------
# Single Resume Analysis
# ---------------------------------------

@app.route("/upload", methods=["POST"])
def upload():

    if "resume" not in request.files:
        return "No Resume Uploaded"

    file = request.files["resume"]

    if file.filename == "":
        return "Please Select Resume"

    job_description = request.form.get("job_description", "")

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)

    file.save(filepath)

    # Resume Text
    resume_text = extract_text_from_pdf(filepath)

    # Sections
    sections = extract_sections(resume_text)

    # Experience
    experience = extract_experience(
        sections["experience"] if sections["experience"].strip() else resume_text
    )

    # Education
    education = extract_education(
        sections["education"] if sections["education"].strip() else resume_text
    )

    # Projects
    projects = extract_projects(
        sections["projects"] if sections["projects"].strip() else resume_text
    )

    # Certifications
    certifications = extract_certifications(
        sections["certifications"] if sections["certifications"].strip() else resume_text
    )

    # Skills
    resume_skills = extract_skills(
        sections["skills"] if sections["skills"].strip() else resume_text
    )

    jd_skills = extract_skills(job_description)

    # ATS Match
    result = calculate_match(
        resume_skills,
        jd_skills
    )

    # Recommendations
    recommendations = generate_recommendations(
        result["missing"]
    )

    # -------- AI --------
    ai_feedback = "AI Temporarily Disabled"


    try:

        ai_feedback = generate_ai_feedback(
        resume_text[:1500],
        job_description[:700]
    )

        ai_feedback = markdown(ai_feedback)

    except Exception as e:

        ai_feedback = f"AI Feedback Error : {e}"

    # Analysis
    analysis = analyze_resume(
        result["percentage"],
        result["matched"],
        result["missing"]
    )

    global last_candidate

    last_candidate = {
        "name": file.filename,
        "ats_score": result["ats_score"],
        "match_percentage": result["percentage"],
        "experience": experience,
        "education": education,
        "projects": projects,
        "certifications": certifications,
        "matched_skills": result["matched"],
        "missing_skills": result["missing"],
        "recommendations": recommendations,
        "ai_feedback": ai_feedback
    }

    return render_template(

        "result.html",

        filename=file.filename,

        job_description=job_description,

        resume_text=resume_text,

        resume_skills=resume_skills,

        jd_skills=jd_skills,

        matched_skills=result["matched"],

        missing_skills=result["missing"],

        match_percentage=result["percentage"],

        ats_score=result["ats_score"],

        recommendations=recommendations,

        category=analysis["category"],

        category_color=analysis["color"],

        total_skills=analysis["resume_skills"],

        matched_count=analysis["matched_skills"],

        missing_count=analysis["missing_skills"],

        experience=experience,

        education=education,

        projects=projects,

        certifications=certifications,

        ai_feedback=ai_feedback

    )


# ---------------------------------------
# Multiple Resume Ranking
# ---------------------------------------



@app.route("/rank", methods=["POST"])
def rank():

    job_description = request.form.get("job_description", "")

    files = request.files.getlist("resumes")

    if not files:
        return "No Resumes Uploaded"

    candidates = rank_candidates(
        files,
        app.config["UPLOAD_FOLDER"],
        job_description
    )

    # CSV Save
    csv_file = os.path.join(
        app.config["UPLOAD_FOLDER"],
        "ranking.csv"
    )

    with open(csv_file, "w", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        writer.writerow([
            "Rank",
            "Candidate",
            "ATS Score",
            "Match %",
            "Experience",
            "Projects",
            "Certificates"
        ])

        for c in candidates:

            writer.writerow([
                c["rank"],
                c["name"],
                c["ats_score"],
                c["match_percentage"],
                c["experience"],
                c["projects"],
                len(c["certifications"])
            ])

    return render_template(
        "ranking.html",
        candidates=candidates
    )


# ---------------------------------------
# Download CSV
# ---------------------------------------

@app.route("/download_csv")
def download_csv():

    csv_file = os.path.join(
        app.config["UPLOAD_FOLDER"],
        "ranking.csv"
    )

    if not os.path.exists(csv_file):
        return "No Ranking Available"

    with open(csv_file, "r", encoding="utf-8") as f:
        data = f.read()

    return Response(
        data,
        mimetype="text/csv",
        headers={
            "Content-Disposition":
            "attachment; filename=Candidate_Ranking.csv"
        }
    )

# ---------------------------------------
# naya route
# ---------------------------------------

@app.route("/download_pdf")
def download_pdf():

    global last_candidate

    if not last_candidate:
        return "No Resume Available"

    pdf_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        "Resume_Report.pdf"
    )

    create_pdf(
        last_candidate,
        pdf_path
    )

    with open(pdf_path, "rb") as f:
        pdf_data = f.read()

    return Response(
        pdf_data,
        mimetype="application/pdf",
        headers={
            "Content-Disposition":
            "attachment; filename=Resume_Report.pdf"
        }
    )


# ---------------------------------------
# naya route
# ---------------------------------------

@app.route("/ai_review", methods=["POST"])
def ai_review():

    resume_text = request.form["resume_text"]

    job_description = request.form["job_description"]

    ai_feedback = generate_ai_feedback(
        resume_text[:1500],
        job_description[:700]
    )

    return render_template(
        "ai_review.html",
        ai_feedback=ai_feedback
    )


# ---------------------------------------
# Run App
# ---------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
