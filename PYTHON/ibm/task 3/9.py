students = {
    "Rahul": 85,
    "Aman": 91,
    "Priya": 88,
    "Neha": 95
}

highest = -1
name = ""

for student in students:
    if students[student] > highest:
        highest = students[student]
        name = student

print("Highest Marks:", highest)
print("Student:", name)