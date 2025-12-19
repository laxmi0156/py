# 40)Write a Python program to get unique values from a list 

l=[1,1,3,2,3,4]
uni=[]
for i in l:
    if i not in uni:
        uni.append(i)
print(uni)        