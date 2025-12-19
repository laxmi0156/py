# 80)Write a Python program to count the frequency of words in a file.

word_count = {}

file = open("text02.txt", "r")

for line in file:
    words = line.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

file.close()

print(word_count)
