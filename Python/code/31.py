'''31) Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given list
of strings. '''

def fun(words): 
   count=0    
   for word in words:      
      if len(word) >= 2 and word[0] == word[-1]: 
         count += 1    
   print("Number of matching words:",count ) 
word_list = ['abc', 'xyz', 'aba', '1221', 'aa', 'ghg'] 
fun(word_list)
 
