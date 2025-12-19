'''56)Write a Python program to map two lists into a dictionary
Sample output: Counter ({'a': 400, 'b': 400,'d': 400, 'c': 300}). '''

l=["a","b","c","d"]
l2=[400,400,400,300]

d={}

for i in range(len(l)):
    d[l[i]]=l2[i]

print(d)    