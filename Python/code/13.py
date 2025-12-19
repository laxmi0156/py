''' 13) Write a Python program that will return true if the two given integer values are
 equal or their sum or difference is 5.'''


n1=int(input("Enter First Number:")) 
n2=int(input("Enter Second Number:"))
n3=n1+n2 
n4=n1-n2 
print(n1==n2 or n3==5 or n4==5) 
