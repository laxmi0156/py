# 54)Write a Python program to check multiple keys exists in a dictionary.

data = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

keys_to_check = ['a', 'c', 'e']

if all(key in data for key in keys_to_check):
    print("All keys exist in the dictionary")
else:
    print("All keys do not exist in the dictionary")
