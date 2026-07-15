import random

COMPANIES = [
    "TCS",
    "Infosys",
    "Wipro",
    "Accenture",
    "Capgemini",
    "Cognizant",
    "IBM",
    "Tech Mahindra",
    "HCL",
    "LTIMindtree",
    "Deloitte",
    "Oracle",
    "Microsoft",
    "Amazon",
    "Google"
]

DESIGNATIONS = {
    "Python Developer": [
        "Python Developer",
        "Backend Developer",
        "Software Engineer"
    ],

    "Java Developer": [
        "Java Developer",
        "Software Engineer",
        "Backend Engineer"
    ],

    "Frontend Developer": [
        "Frontend Developer",
        "React Developer",
        "UI Developer"
    ],

    "Data Analyst": [
        "Data Analyst",
        "Business Analyst",
        "BI Analyst"
    ],

    "ML Engineer": [
        "Machine Learning Engineer",
        "AI Engineer",
        "Data Scientist"
    ]
}


def generate_experience(role):

    years = random.randint(0, 5)

    if years == 0:

        return {
            "years": 0,
            "company": "-",
            "designation": "Fresher"
        }

    return {

        "years": years,

        "company": random.choice(COMPANIES),

        "designation": random.choice(DESIGNATIONS[role])

    }