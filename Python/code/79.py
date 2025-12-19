# 79)Write a Python program to count the number of lines in a text file. 

count = 0

file = open("text01.txt", "r")

for line in file:
    count += 1

file.close()

print("Number of lines:", count)
