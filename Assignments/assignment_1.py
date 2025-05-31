# Assignment: Exploring Python Concepts

# ----------------------------------------------------------------
# Task 1 - Variables: Your First Python Intro
name = "Gigi"
age = 20
height = 5.5

print(f"Hello there, my name is {name}!!!, I am {age} years old and {height} feet tall. uwur")

# ----------------------------------------------------------------
# Task 2 - Operators: Playing with Numbers
num1 = 3.1416 # Pipipipipi
num2 = 9.9999 # I don't know what to put here

# Let's do some math (I forgot how to do this lmao)
# Addition
result_add = num1 + num2
# Subtraction
result_sub = num1 - num2
# Multiplication
result_mul = num1 * num2
# Division
result_div = num1 / num2

# Printing the results (how tedious)
print("The sum of", num1, "and", num2, "is:", result_add)
print("The difference between", num1, "and", num2, "is:", result_sub)
print("The product of", num1, "and", num2, "is:", result_mul)
print("The quotient of", num1, "and", num2, "is:", result_div)

# ----------------------------------------------------------------
# Task 3 - Lists: A List of Things
print("Insert a number:")
num = int(input())

if num > 0: 
    print("The number is positive. Awesome!")
elif num < 0:
    print("The number is negative. Better luck next time!")
else:
    print("The number is zero. A perfect balance!")