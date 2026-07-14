from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()


def create_pdf(candidate, filename):

    pdf = SimpleDocTemplate(filename)

    story = []

    # -----------------------------
    # Title
    # -----------------------------

    story.append(
        Paragraph(
            "<b>AI Resume Screening Report</b>",
            styles["Title"]
        )
    )

    # -----------------------------
    # Basic Information
    # -----------------------------

    story.append(
        Paragraph(
            f"<b>Candidate:</b> {candidate['name']}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>ATS Score:</b> {candidate['ats_score']}/100",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Match Percentage:</b> {candidate['match_percentage']}%",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Experience:</b> {candidate['experience']} Years",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Projects:</b> {candidate['projects']}",
            styles["Normal"]
        )
    )

    # -----------------------------
    # Education
    # -----------------------------

    story.append(
        Paragraph(
            "<br/><b>Education</b>",
            styles["Heading2"]
        )
    )

    if candidate["education"]:

        story.append(
            Paragraph(
                ", ".join(candidate["education"]),
                styles["Normal"]
            )
        )

    else:

        story.append(
            Paragraph(
                "Not Available",
                styles["Normal"]
            )
        )

    # -----------------------------
    # Certifications
    # -----------------------------

    story.append(
        Paragraph(
            "<br/><b>Certifications</b>",
            styles["Heading2"]
        )
    )

    if candidate["certifications"]:

        story.append(
            Paragraph(
                ", ".join(candidate["certifications"]),
                styles["Normal"]
            )
        )

    else:

        story.append(
            Paragraph(
                "None",
                styles["Normal"]
            )
        )

    # -----------------------------
    # Matched Skills
    # -----------------------------

    story.append(
        Paragraph(
            "<br/><b>Matched Skills</b>",
            styles["Heading2"]
        )
    )

    if candidate["matched_skills"]:

        story.append(
            Paragraph(
                ", ".join(candidate["matched_skills"]),
                styles["Normal"]
            )
        )

    else:

        story.append(
            Paragraph(
                "None",
                styles["Normal"]
            )
        )

    # -----------------------------
    # Missing Skills
    # -----------------------------

    story.append(
        Paragraph(
            "<br/><b>Missing Skills</b>",
            styles["Heading2"]
        )
    )

    if candidate["missing_skills"]:

        story.append(
            Paragraph(
                ", ".join(candidate["missing_skills"]),
                styles["Normal"]
            )
        )

    else:

        story.append(
            Paragraph(
                "None",
                styles["Normal"]
            )
        )

    # -----------------------------
    # Recommendations
    # -----------------------------

    story.append(
        Paragraph(
            "<br/><b>Recommendations</b>",
            styles["Heading2"]
        )
    )

    if candidate["recommendations"]:

        for item in candidate["recommendations"]:

            story.append(
                Paragraph(
                    "• " + item,
                    styles["Normal"]
                )
            )

    else:

        story.append(
            Paragraph(
                "No Recommendations",
                styles["Normal"]
            )
        )

    # -----------------------------
    # AI Review
    # -----------------------------

    story.append(
        Paragraph(
            "<br/><b>AI Resume Review</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            candidate["ai_feedback"].replace("\n", "<br/>"),
            styles["Normal"]
        )
    )

    pdf.build(story)
