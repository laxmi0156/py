'''21) Write a Python program to add 'in' at the end of a given string (length
should be at least 3). If the given string already ends with 'ing' then
add 'ly' instead if the string length of the given string is less than 3,
leave it unchanged. '''

s = input("Enter a string: ") 
 
if len(s) >= 3:    
   result = s + 'in'
elif s.endswith('ing'): 
    result = s + 'ly'
else: 
    result = s
 
print("Resulting string:", result) 
