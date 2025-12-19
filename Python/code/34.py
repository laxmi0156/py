'''34) Write a Python function that takes two lists and returns true if they
have at least one common member. '''

def fun(list1, list2):    
  for item in list1:         
    if item in list2:             
        return True    
        return False 
 
list1 = [1, 2, 3, 4, 5] 
list2 = [5, 6, 7, 8, 9] 
 
print( fun(list1, list2)) 
