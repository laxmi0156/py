'''62)Write a Python function to check whether a number is in a given range '''

def range(num, start, end):
    if start <= num <= end:
        return True
    else:
        return False


print(range(5, 1, 10))   
print(range(15, 1, 10)) 
