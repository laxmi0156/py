'''29) Write a Python function to get the largest number, smallest num
and sum of all from a list. '''

a=[26,62,42,21,11] 
a.sort() 
sum=0 
for i in a: 
       sum=sum+i 
 
print("Smallest:",a[0])
print("Largest:",a[-1]) 
print("sum:",sum) 
