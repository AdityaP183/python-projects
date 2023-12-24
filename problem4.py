# Write a program to find the factorial of a number.
num = int(input("Enter a number to find the factorial of: "))
factorial = 1
while num > 0:
    factorial *= num    
    num -= 1
print(factorial)