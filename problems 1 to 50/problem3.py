# Check if a number is even or odd.
num = int(input("Enter a number to check if odd or even: "))
if(num < 0 ):
    print("Invalid number. Enter real numbers")
elif (num == 0):
    print("Even number")
elif (num % 2 == 0):
    print("Even number")
else:
    print("Odd number")