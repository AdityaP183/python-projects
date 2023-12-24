# Calculate the square root of a number without using built-in method.

def squareRoot(num):
    if num < 0:
        return "Square root of negative number is not possible"
    precision = 1e-10
    guess = num
    while abs(guess * guess - num) > precision:
        guess = (guess + num / guess) / 2

    return guess

user_input = int(input("Enter a number: "))
result = squareRoot(user_input)
print(result)