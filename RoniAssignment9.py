#-------------------------------------------------
#    Author: Roni Kulkarni
#    Date : 05-28-2025
#    About Parameters and Functions

#-------------------------------------------------


# Task 1: Writing Functions
# Write a function to accept name as parameter and print a greeting message.
def greet_user(name):
    print(f"Hello, {name}! Welcome aboard.")
# Create a new function to add the sum of two numbers.
def add_numbers(num1, num2):
    print("The sum of", num1, "and", num2, "is:", num1 + num2)
# Call the two functions with appropriate parameters.
greet_user("Roni")
add_numbers(5, 10)

# Task 2: Using Default Parameters
# Function that takes two parameters: pet name and pet type, with a default value for pet type is "dog".
def describe_pet(pet_name, pet_type="dog"):
    print(f"I have a {pet_type} named {pet_name}.")
# Call the function with and without the default parameter.
describe_pet("Buddy")
describe_pet("Whiskers", "cat")

# Task 3: Functions with Variable Arguments
# Function that accepts a variable number of arguments as sandwich ingredients and prints them.
def make_sandwich(*ingredients):
    print("Making a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")
    
# Call the function with different numbers of ingredients.
make_sandwich("lettuce", "tomato", "cheese")
make_sandwich("peanut butter", "jelly")

# Task 4: Understanding Recursion
# Function to calculate the factorial of a number using recursion.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# Call the function with a number and print the result.
print("Factorial of 5 is:", factorial(5))
# Call another function to calculate the nth number in the Fibonacci sequence using recursion.
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# Call the function with a number and print the result.
print("Fibonacci number at position 6 is:", fibonacci(6))