# 81)Write a Python program to write a list to a file. 

my_list = ["Apple", "Banana", "Mango", "Orange"]

file = open("data.txt", "w")

for item in my_list:
    file.write(item + "\n")

file.close()

print("List written to file")
