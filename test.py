from utils.section_parser import extract_sections

sample = """
John Doe

SKILLS
Python
Java
Flask

EDUCATION
Bachelor of Technology

EXPERIENCE
Software Engineer
2 Years

PROJECTS
AI Resume Screening Tool
Weather Forecast App

CERTIFICATIONS
AWS Cloud Practitioner
Coursera Python
"""

sections = extract_sections(sample)

for name, value in sections.items():

    print("=" * 30)
    print(name.upper())
    print("=" * 30)
    print(value)
    
  