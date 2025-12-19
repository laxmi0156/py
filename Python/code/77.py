# 77)Write a Python program to read a file line by line store it into a variable. 

content = ""

file = open("data.txt", "r")

for line in file:
    content += line

file.close()

print(content)
