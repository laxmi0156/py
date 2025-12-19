'''89)How Do You Handle Exceptions with Try/Except/Finally in Python?
Explain with coding snippets. 
'''

try:
    a = int(input("Enter number: "))
    b = int(input("Enter another number: "))
    result = a / b
except ZeroDivisionError:
    print("Division by zero error")
except ValueError:
    print("Wrong input")
else:
    print("Result:", result)
finally:
    print("Execution completed")
