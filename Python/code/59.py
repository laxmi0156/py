'''59)Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string. '''

s=input("Enter String:")
d={}

for i in range(0,len(s)-1,2):
      d[s[i]]=s[i+1]
 
print(d)    
