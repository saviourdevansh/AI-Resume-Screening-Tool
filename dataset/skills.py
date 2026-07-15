import random

SKILLS = {

    "Python Developer": [
        "Python",
        "Flask",
        "Django",
        "FastAPI",
        "SQL",
        "MySQL",
        "PostgreSQL",
        "REST API",
        "Git",
        "GitHub",
        "Docker",
        "Linux",
        "Pandas",
        "NumPy",
        "OOP",
        "Problem Solving"
    ],

    "Java Developer": [
        "Java",
        "Spring Boot",
        "Hibernate",
        "JDBC",
        "MySQL",
        "REST API",
        "Git",
        "Maven",
        "JUnit",
        "Docker",
        "Linux",
        "OOP",
        "Data Structures",
        "Algorithms"
    ],

    "Frontend Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "Bootstrap",
        "React",
        "Redux",
        "Tailwind CSS",
        "Git",
        "GitHub",
        "Responsive Design",
        "REST API",
        "Figma"
    ],

    "Data Analyst": [
        "Excel",
        "SQL",
        "Python",
        "Power BI",
        "Tableau",
        "Pandas",
        "NumPy",
        "Data Cleaning",
        "Statistics",
        "Data Visualization"
    ],

    "ML Engineer": [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "PyTorch",
        "Scikit-Learn",
        "Pandas",
        "NumPy",
        "OpenCV",
        "NLP",
        "Docker",
        "Git"
    ]
}


def generate_role():

    return random.choice(list(SKILLS.keys()))


def generate_skills(role):

    return random.sample(
        SKILLS[role],
        random.randint(6, 10)
    )