'''61)Write a Python function to calculate the factorial of a number (a
nonnegative integer) 
'''

def fac():
    n=int(input("Enter Number:"))
    fac=1
    
    for i in range(1,n+1):
        fac=fac*i
    print("Factorial:",fac)
    
fac()    