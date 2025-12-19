# 82)Write a Python program to copy the contents of a file to another file. 

source = open("data.txt", "r")
destination = open("destination.txt", "w")

for line in source:
    destination.write(line)
    
source.close()
destination.close()

print("File copied successfully")

