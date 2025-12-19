'''50)Write a Python script to check if a given key already exists in a
dictionary. '''

d={1:"a",2:"b",3:"c",4:"d"}
key="c"
if key in d:
    print(key,"is already exist in d")
else:
    print(key,"is not exist in d")

