numbers = [12, 45, 67, 89, 34, 23, 90, 10]

ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

print("Ascending:", ascending)
print("Descending:", descending)

unique = sorted(list(set(numbers)))

print("Second Largest:", unique[-2])