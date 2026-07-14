numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Original List:", numbers)
print("Without Duplicates:", unique)