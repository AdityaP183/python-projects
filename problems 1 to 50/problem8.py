# Create a simple calculator program in Python.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Calculator:\n1 - Add, 2 - Subtract, 3 - Multiply, 4 - Divide")
user_action = int(input("Select the action to perform: "))

if(user_action > 1 and user_action < 5):
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if(user_action == 1):
        print(f"Result after adding {num1} and {num2}: {add(num1, num2)}")
    elif(user_action == 2):
        print(f"Result after subtracting {num1} and {num2}: {subtract(num1, num2)}")
    elif(user_action == 3):
        print(f"Result after multiply {num1} and {num2}: {multiply(num1, num2)}")
    else:
        print(f"Result after dividing {num1} and {num2}: {divide(num1, num2)}")
else:
    print("Invalid")