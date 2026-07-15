import os
import csv
import random

# ======================================================
# AI Resume Dataset Generator
# ======================================================

TOTAL_RESUMES = 50

OUTPUT_FOLDER = "Generated_Resumes"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

CSV_FILE = "dataset_info.csv"

# ======================================================
# Names
# ======================================================

FIRST_NAMES = [

    "Rahul","Aman","Vikram","Priya","Neha",
    "Rohit","Ankit","Karan","Pooja","Sneha",
    "Arjun","Devansh","Ayush","Nikhil","Riya",
    "Shreya","Yash","Aditya","Sakshi","Rohan",
    "Harsh","Vaibhav","Akash","Shivam","Aryan",
    "Ananya","Khushi","Muskan","Ishita","Simran",
    "Deepak","Manish","Saurabh","Tushar","Mohit",
    "Komal","Ritika","Tanvi","Megha","Payal",
    "Nitin","Gaurav","Abhishek","Rajat","Vivek"

]

LAST_NAMES = [

    "Sharma","Verma","Singh","Patel","Gupta",
    "Kumar","Yadav","Joshi","Mehta","Mishra",
    "Pandey","Tiwari","Rathore","Saxena","Bansal",
    "Kapoor","Jain","Roy","Nair","Reddy",
    "Naidu","Pillai","Das","Banerjee","Gill",
    "Sidhu","Bedi","Sandhu","Malhotra","Arora"

]

# ======================================================
# Roles
# ======================================================

ROLES = [

    "Python Developer",

    "Java Developer",

    "Frontend Developer",

    "Data Analyst",

    "ML Engineer"

]

# ======================================================
# Skills
# ======================================================

SKILLS = {

    "Python Developer":[

        "Python",
        "Flask",
        "Django",
        "FastAPI",
        "SQL",
        "MySQL",
        "Git",
        "GitHub",
        "Docker",
        "Linux",
        "REST API",
        "Pandas",
        "NumPy"

    ],

    "Java Developer":[

        "Java",
        "Spring Boot",
        "Hibernate",
        "JDBC",
        "MySQL",
        "Git",
        "Maven",
        "JUnit",
        "REST API",
        "Docker"

    ],

    "Frontend Developer":[

        "HTML",
        "CSS",
        "JavaScript",
        "Bootstrap",
        "React",
        "Redux",
        "Tailwind CSS",
        "Git",
        "GitHub",
        "Responsive Design"

    ],

    "Data Analyst":[

        "Excel",
        "SQL",
        "Power BI",
        "Tableau",
        "Python",
        "Statistics",
        "Pandas",
        "NumPy",
        "Data Cleaning"

    ],

    "ML Engineer":[

        "Python",
        "TensorFlow",
        "PyTorch",
        "Scikit-Learn",
        "OpenCV",
        "NLP",
        "Deep Learning",
        "Machine Learning",
        "Docker"

    ]

}

# ======================================================
# Education
# ======================================================

EDUCATION = [

    "B.Tech Computer Science",

    "B.Tech Information Technology",

    "B.Tech Artificial Intelligence",

    "B.Tech Data Science",

    "BCA",

    "MCA",

    "B.Sc Computer Science",

    "BE Software Engineering"

]

# ======================================================
# Companies
# ======================================================

COMPANIES = [

    "TCS",

    "Infosys",

    "Wipro",

    "Accenture",

    "Capgemini",

    "IBM",

    "HCL",

    "Tech Mahindra",

    "Cognizant",

    "LTIMindtree"

]

# ======================================================
# Projects
# ======================================================

PROJECTS = {

    "Python Developer":[
        "AI Resume Screening Tool",
        "Library Management System",
        "Employee Management System",
        "Hospital Management System",
        "Weather Forecast App",
        "Expense Tracker",
        "Chat Application",
        "Inventory Management System"
    ],

    "Java Developer":[
        "Bank Management System",
        "Hotel Management System",
        "Online Examination System",
        "Payroll Management System",
        "College ERP",
        "Library Automation",
        "Vehicle Rental System",
        "Ticket Booking System"
    ],

    "Frontend Developer":[
        "Portfolio Website",
        "Netflix Clone",
        "Amazon Clone",
        "Restaurant Website",
        "Travel Booking Website",
        "E-Commerce Frontend",
        "Task Management App",
        "News Portal"
    ],

    "Data Analyst":[
        "Sales Dashboard",
        "HR Analytics Dashboard",
        "Customer Churn Analysis",
        "IPL Data Analysis",
        "Retail Sales Analysis",
        "Netflix Data Analysis",
        "COVID-19 Dashboard",
        "Stock Market Analysis"
    ],

    "ML Engineer":[
        "Face Mask Detection",
        "Spam Email Classifier",
        "Image Classification",
        "Movie Recommendation System",
        "Object Detection",
        "Sentiment Analysis",
        "Plant Disease Detection",
        "Fake News Detection"
    ]

}

# ======================================================
# Certifications
# ======================================================

CERTIFICATES = [

    "AWS Cloud Practitioner",

    "Google Data Analytics",

    "IBM Python for Data Science",

    "Oracle Java Foundations",

    "Microsoft Azure Fundamentals",

    "Cisco Networking Essentials",

    "NPTEL Python",

    "Coursera Machine Learning",

    "HackerRank SQL",

    "TensorFlow Developer"

]

# ======================================================
# Helper Functions
# ======================================================

def random_name():

    return random.choice(FIRST_NAMES) + " " + random.choice(LAST_NAMES)


def random_email(name):

    return (
        name.lower().replace(" ", ".")
        + str(random.randint(10,999))
        + "@gmail.com"
    )


def random_phone():

    return "9" + "".join(
        str(random.randint(0,9))
        for _ in range(9)
    )


def random_skills(role):

    available = SKILLS[role]

    return random.sample(
        available,
        random.randint(
            5,
            len(available)
        )
    )


def random_projects(role):

    return random.sample(
        PROJECTS[role],
        random.randint(2,4)
    )


def random_certificates():

    return random.sample(
        CERTIFICATES,
        random.randint(1,3)
    )


print("="*60)
print("AI Resume Dataset Generator")
print("="*60)

dataset_rows = []

# ======================================================
# Generate Dataset
# ======================================================

for i in range(1, TOTAL_RESUMES + 1):

    name = random_name()

    role = random.choice(ROLES)

    email = random_email(name)

    phone = random_phone()

    education = random.choice(EDUCATION)

    experience = random.randint(0, 5)

    company = "-" if experience == 0 else random.choice(COMPANIES)

    skills = random_skills(role)

    projects = random_projects(role)

    certificates = random_certificates()

    resume_text = f"""
==================================================
{name}
==================================================

Role
----
{role}

Contact
-------
Email : {email}

Phone : {phone}

Education
---------
{education}

Experience
----------
{experience} Years

Company
-------
{company}

Skills
------
{", ".join(skills)}

Projects
--------
"""

    for p in projects:
        resume_text += f"- {p}\n"

    resume_text += "\nCertificates\n------------\n"

    for c in certificates:
        resume_text += f"- {c}\n"

    filename = f"Resume_{i:03}.txt"

    filepath = os.path.join(
        OUTPUT_FOLDER,
        filename
    )

    with open(filepath, "w", encoding="utf-8") as file:

        file.write(resume_text)

    dataset_rows.append([

        filename,

        name,

        role,

        education,

        experience,

        company,

        ", ".join(skills),

        len(projects),

        len(certificates)

    ])

# ======================================================
# CSV File
# ======================================================

with open(
    CSV_FILE,
    "w",
    newline="",
    encoding="utf-8"
) as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow([

        "Resume File",

        "Candidate Name",

        "Role",

        "Education",

        "Experience",

        "Company",

        "Skills",

        "Projects",

        "Certificates"

    ])

    writer.writerows(dataset_rows)

print()

print("=" * 60)

print("Dataset Generated Successfully!")

print("=" * 60)

print(f"Total Resumes : {TOTAL_RESUMES}")

print(f"Resume Folder : {OUTPUT_FOLDER}")

print(f"CSV File : {CSV_FILE}")

print("=" * 60)