import re


def extract_education(resume_text):

    text = resume_text.lower()

    education_patterns = {
        "B.Tech": r"\bb\.?\s?tech\b|\bbtech\b",
        "B.E.": r"\bb\.?\s?e\b",
        "B.Sc": r"\bb\.?\s?sc\b|\bbsc\b",
        "M.Tech": r"\bm\.?\s?tech\b|\bmtech\b",
        "M.E.": r"\bm\.?\s?e\b",
        "M.Sc": r"\bm\.?\s?sc\b|\bmsc\b",
        "MBA": r"\bmba\b",
        "MCA": r"\bmca\b",
        "Diploma": r"\bdiploma\b",
        "Bachelor": r"\bbachelor\b",
        "Master": r"\bmaster\b",
        "PhD": r"\bphd\b|\bdoctorate\b"
    }

    found = []

    for degree, pattern in education_patterns.items():

        if re.search(pattern, text):
            found.append(degree)

    return sorted(found)