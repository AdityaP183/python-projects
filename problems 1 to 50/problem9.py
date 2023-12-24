# Count the number of vowels in a given string.
user_input = input("Enter a string:\n")

letters = [letter for letter in user_input]
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

no_of_vowels = 0
for letter in letters:
    if letter in vowels:
        no_of_vowels += 1

print("Total no. of vowels:", no_of_vowels)