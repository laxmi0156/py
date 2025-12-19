'''64)Write a Python function that checks whether a passed string is
palindrome or not 
'''

def palin(s):
    rev = ""
    for ch in s:
        rev = ch + rev   # reverse the string

    if s == rev:
        return True
    else:
        return False

print(palin("madam"))  
print(palin("hello"))  
