'''36) Write a Python function that takes a list and returns a new list with
unique elements of the first list. 
'''

def fun(lst):     
  unique = []     
  for item in lst:         
     if item not in unique:             
        unique.append(item)     
        return unique 
sample_list = [1, 2, 2, 3, 4, 4, 5, 1, 6] 
print("Original list:", sample_list) 
print("List with unique elements:", fun(sample_list)) 
