nested = ((1, 2), (3, 4), (5, 6))

total = 0

for t in nested:
    for num in t:
        total += num

print("Sum:", total)