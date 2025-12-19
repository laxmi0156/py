'''22) Write a Python function to reverses a string if its length is a multiple
of 4. 
'''

def rev(string): 
    if len(string) % 4 == 0:         
        return string[::-1]        
    else:        
         return string           
 
text = input("Enter a string: ") 
 
result = rev(text) 
print("Resulting string:", result) 
 
 
