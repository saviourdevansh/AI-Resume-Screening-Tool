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