list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

merged = list1 + list2

common = []
unique = []

for item in merged:
    if item in list1 and item in list2:
        if item not in common:
            common.append(item)
    else:
        if item not in unique:
            unique.append(item)

print("Merged List:", merged)
print("Common Elements:", common)
print("Unique Elements:", unique)