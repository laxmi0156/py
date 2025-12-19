# 47)How will you create a dictionary using tuples in python?

t=l=((1,"a"),(2,"b"),(3,"c"))
d={}

for key,value in t:
    d[key]=value 

print(d)      