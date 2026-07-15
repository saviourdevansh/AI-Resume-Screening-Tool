import random

FIRST_NAMES = [
    "Rahul", "Aman", "Vikram", "Priya", "Neha",
    "Rohit", "Ankit", "Karan", "Pooja", "Sneha",
    "Arjun", "Devansh", "Ayush", "Nikhil", "Riya",
    "Shreya", "Yash", "Aditya", "Sakshi", "Rohan",
    "Abhishek", "Harsh", "Vaibhav", "Akash", "Shivam",
    "Ananya", "Khushi", "Muskan", "Ishita", "Simran",
    "Deepak", "Manish", "Saurabh", "Tushar", "Mohit",
    "Aditi", "Komal", "Ritika", "Tanvi", "Megha",
    "Aryan", "Rajat", "Vivek", "Nitin", "Gaurav",
    "Anmol", "Nidhi", "Payal", "Kirti", "Swati"
]

LAST_NAMES = [
    "Sharma", "Verma", "Singh", "Patel", "Gupta",
    "Kumar", "Yadav", "Joshi", "Mehta", "Mishra",
    "Pandey", "Tiwari", "Chauhan", "Rathore", "Saxena",
    "Bansal", "Agarwal", "Malhotra", "Kapoor", "Soni",
    "Jain", "Dubey", "Tripathi", "Chawla", "Arora",
    "Nair", "Iyer", "Reddy", "Naidu", "Pillai",
    "Das", "Roy", "Dutta", "Bose", "Banerjee",
    "Kohli", "Gill", "Sidhu", "Bedi", "Sandhu"
]


def generate_name():

    first = random.choice(FIRST_NAMES)
    last = random.choice(LAST_NAMES)

    return f"{first} {last}"


def generate_email(name):

    username = name.lower().replace(" ", ".")

    number = random.randint(10, 999)

    return f"{username}{number}@gmail.com"


def generate_phone():

    return "9" + "".join(
        str(random.randint(0, 9))
        for _ in range(9)
    )