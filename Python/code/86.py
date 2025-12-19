# 86)Can one block of except statements handle multiple exception? 

try:
    a = int(input("Enter number: "))
    b = int(input("Enter another number: "))
    print(a / b)

except (ZeroDivisionError, ValueError):
    print("Invalid input or division by zero")
