tuple1 = (1, 2, 3, 4)
tuple2 = (5, 6, 7, 8)

merged = tuple1 + tuple2

even = []
odd = []

for num in merged:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Merged Tuple:", merged)
print("Even Numbers:", even)
print("Odd Numbers:", odd)