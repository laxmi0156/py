# 9)Write python program that swap two number with temp variable and without temp variable. 

'''a=int(input("Enter First Number:")) 
b=int(input("Enter Second Number:")) 
temp=a      # with temp variable a=b b=temp 
print("a=",a) 
print("b=",b) '''

a=int(input("Enter First Number:")) 
b=int(input("Enter Second Number:")) 
a=a+b   # without temp variable
b=a-b
a=a-b
print("a=",a)
print("b=",b) 
