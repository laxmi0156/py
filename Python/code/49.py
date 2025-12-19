'''49)Write a Python script to concatenate following dictionaries to create
a new one. 
'''

d={1:"a",2:"b",3:"c",4:"d"}
d1={5:"e",6:"f"}
d3={}

d3.update(d)
d3.update(d1)

print(d3)