# 45)Write a Python program to unzip a list of tuples into individual lists.

data=[(1,"a"),(2,"b"),(3,"c"),(4,"d")]
l1,l2=zip(*data)
l1=list(l1)
l2=list(l2)

print("list1=",l1)
print("list2=",l2)