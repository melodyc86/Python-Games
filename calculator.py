'''
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice not in ('1', '2', '3', '4'):
        print("Invalid input. Please enter a valid number (1/2/3/4).")
        return

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))

if __name__ == "__main__":
    calculator()
'''

import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y



print(add(1,2))








'''
def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def power(x, y):
    return x ** y 

def square_root(x):
    return math.sqrt(x)

def logarithm(x, base):
    return math.log(x, base)

def calculator():
    print("Advanced Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm")

    choice = input("Enter choice (1/2/3/4/5/6/7): ")

    if choice not in ('1', '2', '3', '4', '5', '6', '7'):
        print("Invalid input. Please enter a valid number (1/2/3/4/5/6/7).")
        return

    if choice in ('1', '2', '3', '4', '5', '7'):
        num1 = float(input("Enter first number: "))
    else:
        num1 = float(input("Enter base number: "))

    if choice in ('1', '2', '3', '4', '5', '7'):
        num2 = float(input("Enter second number: "))
    else:
        num2 = None 

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    elif choice == '5':
        print(num1, "raised to the power of", num2, "=", power(num1, num2))
    elif choice == '6':
        print("Square root of", num1, "=", square_root(num1))
    elif choice == '7':
        base = float(input("Enter logarithm base: "))
        print("Logarithm of", num1, "with base", base, "=", logarithm(num1, base))

if __name__ == "__main__":
    calculator()

'''


