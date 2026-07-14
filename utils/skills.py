import re

SKILLS = [
    "python",
    "java",
    "c++",
    "html",
    "css",
    "javascript",
    "react",
    "nodejs",
    "flask",
    "django",
    "sql",
    "mysql",
    "mongodb",
    "machine learning",
    "deep learning",
    "data science",
    "nlp",
    "git",
    "github",
    "oop",
    "rest api"
]


def extract_skills(text):

    text = text.lower()

    words = re.findall(r"\b[\w+]+\b", text)

    found_skills = []

    for skill in SKILLS:

        if " " in skill:

            if skill in text:
                found_skills.append(skill.title())

        else:

            if skill in words:
                found_skills.append(skill.title())

    return sorted(found_skills)