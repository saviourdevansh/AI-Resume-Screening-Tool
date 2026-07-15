import os

from utils.parser import extract_text_from_pdf
from utils.section_parser import extract_sections
from utils.skills import extract_skills
from utils.experience import extract_experience
from utils.education import extract_education
from utils.projects import extract_projects
from utils.certifications import extract_certifications
from utils.ranking import calculate_match
from utils.ai_feedback import generate_ai_feedback


def analyze_candidate(filepath, job_description):

    resume_text = extract_text_from_pdf(filepath)

    sections = extract_sections(resume_text)

    resume_skills = extract_skills(
        sections["skills"] if sections["skills"].strip() else resume_text
    )

    jd_skills = extract_skills(job_description)

    result = calculate_match(resume_skills, jd_skills)

    experience = extract_experience(
        sections["experience"] if sections["experience"].strip() else resume_text
    )

    education = extract_education(
        sections["education"] if sections["education"].strip() else resume_text
    )

    projects = extract_projects(
        sections["projects"] if sections["projects"].strip() else resume_text
    )

    certifications = extract_certifications(
        sections["certifications"] if sections["certifications"].strip() else resume_text
    )

# AI Feedback
try:

    ai_feedback = generate_ai_feedback(
        resume_text[:1500],
        job_description[:700]
    )

except Exception:

    ai_feedback = "AI Review Not Available"

    return {

        "name": os.path.basename(filepath),

        "resume_file": os.path.basename(filepath),

        "path": filepath,

        "ats_score": result["ats_score"],

        "match_percentage": result["percentage"],

        "matched_skills": result["matched"],

        "missing_skills": result["missing"],

        "experience": experience,

        "education": education,

        "projects": projects,

        "certifications": certifications,

        "resume_skills": resume_skills,

        "ai_feedback": ai_feedback

    }


def rank_candidates(files, upload_folder, job_description):

    candidates = []

    for file in files:

        if file.filename == "":
            continue

        filepath = os.path.join(upload_folder, file.filename)

        file.save(filepath)

        candidate = analyze_candidate(filepath, job_description)

        candidates.append(candidate)

    candidates.sort(
        key=lambda x: x["ats_score"],
        reverse=True
    )

    for index, candidate in enumerate(candidates, start=1):

        candidate["rank"] = index

    return candidates