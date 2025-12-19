# 76)Write a Python program to read a file line by line and store it into a list

lines_l = []

file = open("data.txt", "r")

for line in file:
    lines_l.append(line.strip())

file.close()

print(lines_l)
