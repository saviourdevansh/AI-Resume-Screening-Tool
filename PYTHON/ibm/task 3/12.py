students = {
    "Rahul": 85,
    "Aman": 91,
    "Priya": 88,
    "Neha": 95
}

ascending = dict(sorted(students.items(), key=lambda x: x[1]))

descending = dict(sorted(students.items(), key=lambda x: x[1], reverse=True))

print("Ascending Order:")
print(ascending)

print("Descending Order:")
print(descending)