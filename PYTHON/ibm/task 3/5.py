numbers = (1, 2, 3, 2, 4, 2, 5)

key = int(input("Enter element to count: "))

count = 0

for num in numbers:
    if num == key:
        count += 1

print("Occurrence:", count)