dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 15, "c": 25, "d": 40}

result = dict1.copy()

for key, value in dict2.items():
    if key in result:
        result[key] += value
    else:
        result[key] = value

print(result)