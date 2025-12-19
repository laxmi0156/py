# 24)Write a Python function to insert a string in the middle of a string. 

def insert(original, insert): 
    mid_ind = len(original) // 2 
    new_string = original[:mid_ind] + insert + original[mid_ind:] 
     
    return new_string 
print(insert("Python", "123")) 
