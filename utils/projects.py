import re


def extract_projects(resume_text):

    text = resume_text.lower()

    # If resume has a Projects section
    project_section = re.search(
        r'projects?(.*?)(education|experience|skills|certifications|$)',
        text,
        re.DOTALL
    )

    if project_section:

        section = project_section.group(1)

        lines = [
            line.strip()
            for line in section.split("\n")
            if line.strip()
        ]

        # Count meaningful project titles
        count = 0

        for line in lines:

            if len(line.split()) >= 2:
                count += 1

        return count

    # Fallback method
    project_keywords = [
        "project",
        "developed",
        "built",
        "created",
        "implemented"
    ]

    count = 0

    for keyword in project_keywords:
        count += len(re.findall(r"\b" + re.escape(keyword) + r"\b", text))

    return max(count, 0)