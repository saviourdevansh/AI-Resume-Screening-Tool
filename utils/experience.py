import re

def extract_experience(resume_text):

    text = resume_text.lower()

    patterns = [
        r'(\d+)\+?\s*years?',
        r'(\d+)\+?\s*yrs?',
        r'experience\s*[:\-]?\s*(\d+)',
        r'(\d+)\s*years?\s*of\s*experience'
    ]

    for pattern in patterns:

        match = re.search(pattern, text)

        if match:
            return int(match.group(1))

    return 0