# Number Guesing Game
# Step 1: Generate a random number between 1 and 100
import random
number_to_guess = random.randint(1, 100)

# Step 2: Prompt the user to guess the number
attempts = 0
print("Welcome to the Number Guessing Game!")
print("Guess the number between 1 and 100.")

# Loop until the user guesses the number
while True:
    guess = int(input())
    attempts += 1
    
    # Step 3: Check if the guess is correct
    if guess < number_to_guess:
        print(f"Attemp {attempts}: {guess} is too low! Try again.")
    elif guess > number_to_guess:
        print(f"Attemp {attempts}: {guess} is too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        break