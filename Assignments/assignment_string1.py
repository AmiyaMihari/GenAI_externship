# Assignment: Exploring String Methods
# Author: Guillermo Jair Montiel Juárez

# Task 1 - String Slicing and Indexing

# Create a string variable with the value "Python is amazing!".
phrase = "Python is amazing!"
print(phrase)

# Extract the first 6 characters
first_six = phrase[:6]
print(first_six)

# Extract the word "amazing"
amazing_word = phrase[10:17]
print(amazing_word)

# Extract the entire string in reverse order
phrase_reversed = phrase[::-1]
print(phrase_reversed)

# -----------------------------------------------------------
# Task 2 - String Methods
# Create a string with the value "hello, python world!"
hello_world = " hello, python world! "
print(hello_world)

# Use string methods to manipulate it
# strip() to remove extra spaces
hello_world = hello_world.strip()
print(hello_world)

# capitalize() to capitalize the first letter
hello_world = hello_world.capitalize()
print(hello_world)

# replace() to replace "world" with "universe"
hello_world = hello_world.replace("world", "universe")
print(hello_world)

# upper() to convert the entire string to uppercase
hello_world = hello_world.upper()
print(hello_world)

# ---------------------------------------------------------------
# Task 3 - Check Palindromes
# Write a Python program to check if a stirng is a palindrome. (reads the same backward and forward)

# Ask the user to input a word
word = input("Enter a word: ")

# Use slicing to reverse the word and check if it is a palindrome
if word == word[::-1]:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")