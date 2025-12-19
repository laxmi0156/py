# 57)Write a Python program to find the highest 3 values in a dictionary

data = {'a': 10, 'b': 45, 'c': 23, 'd': 67, 'e': 34}

values = list(data.values())
values.sort(reverse=True)

print("Highest 3 values:", values[:3])
