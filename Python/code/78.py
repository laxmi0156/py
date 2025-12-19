# 78)Write a python program to find the longest words. 

file = open("data.txt", "r")

text = file.read()
words = text.split()

max_len = 0
for word in words:
    if len(word) > max_len:
        max_len = len(word)

longest_words = []
for word in words:
    if len(word) == max_len:
        longest_words.append(word)

file.close()

print("Longest word(s):", longest_words)
print("Length:", max_len)
