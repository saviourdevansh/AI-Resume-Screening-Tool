from utils.gemini_ai import generate_ai_feedback

resume = """
Python Developer

Skills:
Python
Flask
SQL
Machine Learning

Projects:
AI Resume Screening Tool
"""

jd = """
Looking for Python Developer with

Python
Flask
Docker
AWS
Git
REST API
"""

print(generate_ai_feedback(resume, jd))