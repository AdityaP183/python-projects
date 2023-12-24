# Check if a string is a palindrome.
user_input = input("Enter a string:\n")

reversed_string = user_input[::-1]

if(user_input == reversed_string):
    print("Plaindrome string")
else:
    print("Not a plaindrome string")