import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL_NAME = "gemini-3.5-flash"

def generate_ai_feedback(resume_text, job_description):

    prompt = f"""
You are an ATS Resume Reviewer.

Compare the following resume with the job description.

Resume:
{resume_text[:1500]}

Job Description:
{job_description[:700]}

Return ONLY:

1. Overall ATS Score (/10)

2. Top 3 Strengths

3. Top 3 Missing Skills

4. Top 3 Resume Improvements

Keep the response concise and professional.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text.strip()