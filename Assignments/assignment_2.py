# Project: Eligible Elector
# Author: Guillermo Jair Montiel Juárez

print("Welcome to the Eligible Elector Project!")
# Step 1: Ask the user's age :D
age = int(input("How old are you? "))

# Step 2: Decide the eligibility
if age >= 18: # You are eligible to vote!
    print("Congratulations! You are eligible to vote. Go make a difference! ദ്ദി ( ᵔ ᗜ ᵔ )")
else:
    x = 18 - age # Calculate how many years left to choose the future of the country (joke)
    print(f"Oops! You’re not eligible yet. But hey, only {x} more years to go! (ꐦ¬_¬)")

# Example Outputs:
# How old are you? 20
# Congratulations! You are eligible to vote. Go make a difference!
# How old are you? 16
# Oops! You’re not eligible yet. But hey, only 2 more years to go!