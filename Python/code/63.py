# 63)Write a Python function to check whether a number is perfect or not. 

def is_perfect(num):
    
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i

    return total == num

print(is_perfect(6))    
print(is_perfect(28))   
print(is_perfect(12))  
