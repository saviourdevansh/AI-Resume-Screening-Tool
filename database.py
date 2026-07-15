import sqlite3

DATABASE = "resume_screening.db"


def get_connection():

    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row

    return conn


def create_database():

    print("Creating Database...")

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS candidates(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,

        resume_file TEXT,

        ats_score INTEGER,

        match_percentage REAL,

        experience REAL,

        education TEXT,

        projects INTEGER,

        certificates INTEGER,

        matched_skills TEXT,

        missing_skills TEXT,

        ai_feedback TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )

    """)

    conn.commit()

    conn.close()

    print("Database Created Successfully")


def insert_candidate(candidate):

    conn = get_connection()

    cursor = conn.cursor()

    # ---------- Safe Conversion ----------

    education = candidate.get("education", "")

    if isinstance(education, list):
        education = ", ".join(education)

    matched_skills = candidate.get("matched_skills", [])

    if isinstance(matched_skills, list):
        matched_skills = ", ".join(matched_skills)

    missing_skills = candidate.get("missing_skills", [])

    if isinstance(missing_skills, list):
        missing_skills = ", ".join(missing_skills)

    certifications = candidate.get("certifications", [])

    if isinstance(certifications, list):
        certifications = len(certifications)

    ai_feedback = candidate.get("ai_feedback", "")

    cursor.execute("""

    INSERT INTO candidates(

        name,

        resume_file,

        ats_score,

        match_percentage,

        experience,

        education,

        projects,

        certificates,

        matched_skills,

        missing_skills,

        ai_feedback

    )

    VALUES(?,?,?,?,?,?,?,?,?,?,?)

    """, (

        candidate["name"],

        candidate["resume_file"],

        candidate["ats_score"],

        candidate["match_percentage"],

        candidate["experience"],

        education,

        candidate["projects"],

        certifications,

        matched_skills,

        missing_skills,

        ai_feedback

    ))

    conn.commit()

    conn.close()


def get_candidates():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM candidates

    ORDER BY ats_score DESC

    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def clear_candidates():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("DELETE FROM candidates")

    conn.commit()

    conn.close()