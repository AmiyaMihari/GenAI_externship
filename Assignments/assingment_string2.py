# Project: Password Strenght Checker
# Author: Guillermo Jair Montiel Juárez

# Loop until a strong password is entered
while True:
    # Step 1: Imput the Password
    password = input("Enter a password: ")

    # Step 2: Evaluate the Password Strength}
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
    # Check if passworkd contains at least one uppercase letter, one digit, and one special character (@, #, $, etc.)
    elif password.islower():
        print("Password must contain at least one uppercase letter.")
    elif password.isupper():
        print("Password must contain at least one lowercase letter.")
    elif password.isdigit():
        print("Password must contain at least one digit.")
    elif password.isalnum(): # islanum() checks if the string contains only alphanumeric characters
        # If the password contains only letters and digits, it lacks special characters
        print("Password must contain at least one special character (@, #, $, etc.).")
    else:
        break
# When the password is strong, print a success message and exit the loop    
print("Password is strong! 💪")