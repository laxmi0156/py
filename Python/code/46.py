# 46)Write a Python program to convert a list of tuples into a dictionary. 

l=[("Name","Laxmi"),("Age",22),("weight",47)]
d={}
for key,value in l:
    d[key]=value

print(d)   
