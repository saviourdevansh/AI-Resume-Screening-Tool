numbers = (1, 2, 3, 2, 4, 5, 3, 6)

unique = ()

for num in numbers:
    if num not in unique:
        unique += (num,)

print("Unique Tuple:", unique)