# Assignment: Explore Loops in Python
# Author: Guillermo Jair Montiel Juárez

# -----------------------------------------------------------------
# Task 1 - Counting Down with Loops
# Ask the user for a starting nummer
num = int(input("Enter a starting number for countdown: "))

# Use a while loop to print numbers from that number down to 1
while num >= 1:
    print(num, end=" ")
    num -= 1

# Print a celebration message at the end
print("To the infinity and beyond 🎉")

# -----------------------------------------------------------------
# Task 2 - Multiplication Table with Foor Loops
# Ask the user for a number to input a number
num_mult = int(input("\nEnter a number see the table: "))

# Use a for loop to print the multiplication table for that number
for i in range(1, 11):
    result = num_mult * i
    print(f"{num_mult} x {i} = {result}")

# -----------------------------------------------------------------
# Task 3 - Find the Factorial
# Ask the user for a number to calculate the factorial
num_factorial = int(input("\nEnter a number to calculate its factorial: "))

# Use a for loop to calculate the factorial
# Initialize the result variable as 1 to avoid multiplication by 0
result_factorial = 1

# We define the range num_factorial + 1 to include the number itself
for i in range(1, num_factorial + 1):
    # Multiply the result by each number from 1 to num_factorial
    result_factorial *= i
print(f"The factorial of {num_factorial} is {result_factorial}")
