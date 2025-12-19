# 12) Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. 

n1=int(input("Enter First Number:"))
n2=int(input("Enter Second Number:")) 
n3=int(input("Enter Third Number:")) 
 
if (n1==n2 or n1==n3  or n2==n3 ): 
           print("Zero") 
else: 
         print(n1+n2+n3) 
