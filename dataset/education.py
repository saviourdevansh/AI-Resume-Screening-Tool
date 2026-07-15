import random

EDUCATION = [

    {
        "degree": "B.Tech Computer Science",
        "college": "IIT Delhi",
        "cgpa": "8.9"
    },

    {
        "degree": "B.Tech Information Technology",
        "college": "NIT Trichy",
        "cgpa": "8.4"
    },

    {
        "degree": "BCA",
        "college": "Delhi University",
        "cgpa": "8.1"
    },

    {
        "degree": "MCA",
        "college": "VIT Vellore",
        "cgpa": "8.7"
    },

    {
        "degree": "B.Sc Computer Science",
        "college": "Lucknow University",
        "cgpa": "7.9"
    },

    {
        "degree": "BE Software Engineering",
        "college": "Anna University",
        "cgpa": "8.3"
    },

    {
        "degree": "M.Tech Artificial Intelligence",
        "college": "IIT Bombay",
        "cgpa": "9.1"
    },

    {
        "degree": "B.Tech Artificial Intelligence",
        "college": "IIIT Hyderabad",
        "cgpa": "8.8"
    },

    {
        "degree": "B.Tech Data Science",
        "college": "Manipal University",
        "cgpa": "8.5"
    },

    {
        "degree": "B.Tech Computer Engineering",
        "college": "AKTU",
        "cgpa": "8.0"
    }

]


def generate_education():

    return random.choice(EDUCATION)