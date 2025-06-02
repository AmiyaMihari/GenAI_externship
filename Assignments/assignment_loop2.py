# Number Guesing Game
# Step 1: Generate a random number between 1 and 100
import random
number_to_guess = random.randint(1, 100)

# Step 2: Prompt the user to guess the number
attempts = 0
print("Welcome to the Number Guessing Game")
print()
print("Guess the number between 1 and 100.")

# Loop until the user guesses the number
while True:
    # Max of 10 attemps, otherwise you fail
    if attempts == 10:
        print()
        print("Game over! Better luck next time! o(╥﹏╥)o")
        break

    print()
    guess = int(input("My guess: "))
    attempts += 1
    
    # Step 3: Check if the guess is correct
    if guess < number_to_guess:
        print(f"Attemp {attempts}: {guess} is too low!")
    elif guess > number_to_guess:
        print(f"Attemp {attempts}: {guess} is too high!")
    else:
        print()
        print("ヾ(≧∇≦)ゞ")
        print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        break