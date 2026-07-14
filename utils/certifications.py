import re

def extract_certifications(resume_text):

    text = resume_text.lower()

    certification_patterns = {
        "AWS": r"\baws\b",
        "Azure": r"\bazure\b",
        "Google Cloud": r"\bgoogle cloud\b|\bgcp\b",
        "Oracle": r"\boracle\b",
        "IBM": r"\bibm\b",
        "Cisco": r"\bcisco\b",
        "CCNA": r"\bccna\b",
        "CCNP": r"\bccnp\b",
        "Red Hat": r"\bred hat\b",
        "Salesforce": r"\bsalesforce\b",
        "Coursera": r"\bcoursera\b",
        "Udemy": r"\budemy\b",
        "NPTEL": r"\bnptel\b",
        "Infosys Springboard": r"\binfosys springboard\b"
    }

    found = []

    for cert, pattern in certification_patterns.items():

        if re.search(pattern, text):
            found.append(cert)

    return sorted(found)