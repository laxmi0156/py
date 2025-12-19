# 37)Write a Python program to convert a list of characters into a string. 

def fun(char_list):    
     result = ''.join(char_list)     
     return result 
chars = ['H', 'e', 'l', 'l', 'o'] 
print("Original list:", chars) 
print("Converted string:", fun(chars)) 