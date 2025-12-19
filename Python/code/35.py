'''35) Write a Python program to generate and print a list of first and last 5
elements where the values are square of numbers between 1 and 30. '''

def print_square_list(): 
    squares = [x**2 for x in range(1, 31)]     
    print("Full list of squares:", squares)     
    print("First 5 elements:", squares[:5])     
    print("Last 5 elements:", squares[-5:]) 
print_square_list() 
 
