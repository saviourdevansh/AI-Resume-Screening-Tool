def calculate_match(resume_skills, jd_skills):

    resume_set = set(skill.lower() for skill in resume_skills)
    jd_set = set(skill.lower() for skill in jd_skills)

    matched = sorted(list(resume_set & jd_set))

    missing = sorted(list(jd_set - resume_set))

    if len(jd_set) == 0:
        percentage = 0
    else:
        percentage = round((len(matched) / len(jd_set)) * 100)

    ats_score = percentage

    return {
        "matched": matched,
        "missing": missing,
        "percentage": percentage,
        "ats_score": ats_score
    }