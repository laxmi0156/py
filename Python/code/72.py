# 72)Write a Python program to read an entire text file. 

file = open("data.txt", "r")
content = file.read()
print(content)
file.close()
