import os

OUTPUT_FOLDER = "Job_Descriptions"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

JOB_DESCRIPTIONS = {

    "Python_Developer.txt": """
Python Developer

Required Skills
---------------
Python
Flask
Django
FastAPI
SQL
REST API
Git
Docker
Linux
Pandas
NumPy

Experience
----------
1-3 Years

Education
---------
B.Tech / BCA / MCA / B.Sc Computer Science

Responsibilities
----------------
Develop backend applications
Build REST APIs
Debug applications
Write clean code
Work with databases
""",

    "Java_Developer.txt": """
Java Developer

Required Skills
---------------
Java
Spring Boot
Hibernate
MySQL
Git
REST API
Maven
JUnit

Experience
----------
1-3 Years

Education
---------
B.Tech / MCA / BCA

Responsibilities
----------------
Develop Java applications
Work on backend systems
Database integration
API development
Bug fixing
""",

    "Frontend_Developer.txt": """
Frontend Developer

Required Skills
---------------
HTML
CSS
JavaScript
Bootstrap
React
Redux
Git
Responsive Design

Experience
----------
0-2 Years

Education
---------
B.Tech / BCA / MCA

Responsibilities
----------------
Build responsive websites
Create UI components
Connect APIs
Improve user experience
""",

    "Data_Analyst.txt": """
Data Analyst

Required Skills
---------------
Excel
SQL
Power BI
Python
Statistics
Pandas
NumPy

Experience
----------
0-2 Years

Education
---------
B.Tech / B.Sc / MCA

Responsibilities
----------------
Analyze datasets
Create dashboards
Generate reports
Perform data cleaning
""",

    "ML_Engineer.txt": """
Machine Learning Engineer

Required Skills
---------------
Python
TensorFlow
PyTorch
Machine Learning
Deep Learning
OpenCV
NLP
Docker

Experience
----------
1-3 Years

Education
---------
B.Tech / M.Tech AI / MCA

Responsibilities
----------------
Train ML models
Deploy AI models
Data preprocessing
Model evaluation
"""

}

for filename, content in JOB_DESCRIPTIONS.items():

    filepath = os.path.join(
        OUTPUT_FOLDER,
        filename
    )

    with open(
        filepath,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(content.strip())

print("=" * 50)
print("Job Descriptions Generated Successfully!")
print("=" * 50)
print(f"Files Created : {len(JOB_DESCRIPTIONS)}")
print(f"Folder : {OUTPUT_FOLDER}")