# AI Resume Screening Tool

An intelligent web application that helps recruiters analyze resumes efficiently using NLP, ATS-style scoring, AI-powered feedback, and recruiter-friendly candidate management.

---

## Overview

Recruiters often spend significant time reviewing resumes manually. This project automates the initial screening process by extracting key information from resumes, calculating an ATS score, identifying technical skills, and generating AI-based feedback to assist in shortlisting candidates.

The application is built with Flask and provides a clean interface for both resume analysis and recruiter management.

---

## Features

- Resume upload (PDF)
- ATS Score calculation
- Technical skill extraction using NLP
- Experience detection
- Education extraction
- Project identification
- Certification extraction
- Resume ranking
- Recruiter dashboard
- Candidate history
- Candidate detail page
- AI-generated resume feedback
- PDF report generation
- CSV export
- SQLite database integration

---

## Tech Stack

### Backend
- Python
- Flask
- SQLite

### AI / NLP
- spaCy
- PhraseMatcher
- OpenRouter API

### Frontend
- HTML
- CSS
- Bootstrap
- JavaScript

### Libraries
- PyPDF2
- ReportLab
- Pandas

---

## Project Structure

```
AI-Resume-Screening-Tool
│
├── app.py
├── database.py
├── requirements.txt
├── Procfile
├── runtime.txt
│
├── static/
├── templates/
├── utils/
│
├── uploads/
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/saviourdevansh/AI-Resume-Screening-Tool.git

cd AI-Resume-Screening-Tool
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

> **Note:** Never commit your API key to GitHub.

---

## Run the Application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## Workflow

1. Upload a resume (PDF)
2. Resume text is extracted
3. Skills are identified using NLP
4. Experience, education, projects and certifications are detected
5. ATS score is calculated
6. AI generates personalized feedback
7. Candidate is stored in the recruiter dashboard
8. PDF report can be generated

---

## Screenshots

Add screenshots here.

- Home Page
- Resume Upload
- ATS Score
- Recruiter Dashboard
- Candidate Details
- AI Feedback

---

## Future Improvements

- Multi-resume bulk upload
- Job description matching
- Authentication system
- Email notifications
- Interview scheduling
- Docker support
- Cloud deployment
- Multi-language resume support

---

## License

This project is developed for educational and portfolio purposes.

---

## Author

**Devansh Kumar**

GitHub: https://github.com/saviourdevansh

If you found this project useful, consider giving it a ⭐ on GitHub.