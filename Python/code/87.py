# 87)When is the finally block executed? 

try:
    x = int(input("Enter number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always execute")
