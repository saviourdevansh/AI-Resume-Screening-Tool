def analyze_resume(match_percentage, matched_skills, missing_skills):

    if match_percentage >= 80:
        category = "Excellent"
        color = "success"

    elif match_percentage >= 60:
        category = "Good"
        color = "primary"

    elif match_percentage >= 40:
        category = "Average"
        color = "warning"

    else:
        category = "Needs Improvement"
        color = "danger"

    summary = {
        "resume_skills": len(matched_skills) + len(missing_skills),
        "matched_skills": len(matched_skills),
        "missing_skills": len(missing_skills),
        "category": category,
        "color": color
    }

    return summary