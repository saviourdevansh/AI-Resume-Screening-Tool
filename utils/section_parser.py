def extract_sections(resume_text):

    lines = resume_text.splitlines()

    headings = {
        "education": ["education", "academic"],
        "experience": ["experience", "work experience", "professional experience"],
        "projects": ["projects", "project"],
        "skills": ["skills", "technical skills"],
        "certifications": ["certifications", "certificates", "licenses"]
    }

    sections = {
        "education": "",
        "experience": "",
        "projects": "",
        "skills": "",
        "certifications": ""
    }

    current_section = None

    for line in lines:

        line = line.strip()

        if not line:
            continue

        lower = line.lower()

        found = False

        for key, values in headings.items():

            if lower in values:
                current_section = key
                found = True
                break

        if found:
            continue

        if current_section:
            sections[current_section] += line + "\n"

    return sections