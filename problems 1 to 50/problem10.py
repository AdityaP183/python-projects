# Write a program to reverse a string.

user_input = input("Enter a string:\n")

## Case 1
# letters = [letter for letter in user_input]
# letters.reverse()
# reversed_string = ''.join(letters)

# Case 2
reversed_string = user_input[::-1]
print(reversed_string)