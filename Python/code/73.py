# 73)Write a Python program to append text to a file and display the text. 

# Append text to file
file = open("data.txt", "a")
file.write("\nThis text is appended.")
file.close()

# Read and display file content
file = open("data.txt", "r")
print(file.read())
file.close()
