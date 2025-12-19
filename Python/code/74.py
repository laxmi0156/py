# 74)Write a Python program to read first n lines of a file. 

n = int(input("Enter number of lines: "))

file = open("data.txt", "r")

for i in range(n):
    print(file.readline(), end="")

file.close()
