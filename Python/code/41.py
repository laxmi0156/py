# 41)Write a Python program to check whether a list contains a sub list 

def fun(lst, sublist):     
    if not sublist:          
         return True 
 
    for i in range(len(lst) - len(sublist) + 1):         
        if lst[i:i+len(sublist)] == sublist: 
            return True     
            return False 
 
main_list = [1, 2, 3, 4, 5, 6] 
sub_list = [3, 4, 5] 
 
print("Main list:", main_list) 
print("Sublist:", sub_list) 
print("Contains sublist?", fun(main_list, sub_list)) 
 
