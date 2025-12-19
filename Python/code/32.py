# 32)Write a Python program to remove duplicates from a list. 

a=[1,2,3,1,2] 
uni=[] 
for i in a:    
    if i not in uni:         
        uni.append(i) 
        print(uni) 