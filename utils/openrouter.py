import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)


def generate_ai_feedback(resume_text, job_description):

    prompt = f"""
You are an ATS Resume Reviewer.

Compare the resume with the job description.

Resume:
{resume_text[:1500]}

Job Description:
{job_description[:700]}

Return only:

1. Overall Score (/10)

2. Top 3 Strengths

3. Top 3 Missing Skills

4. Top 3 Resume Improvements
"""

    completion = client.chat.completions.create(
        model="deepseek/deepseek-r1-0528",
        max_tokens=300,
        temperature=0.2,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content