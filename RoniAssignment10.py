#-------------------------------------------------
#    Author: Roni Kulkarni
#    Date : 05-29-2025
#    Checking your Knowledge on Errors

#-------------------------------------------------
# Task 1: Understanding Python Exceptions

# Write a Python program that prompts the user to enter a number
# tries to divide 100 by that number, and handles any exceptions that may occur.
def divide_by_number():
    try:
        #ask user to enter a number
        num = float(input("Please enter a number to divide 100 by: "))
        result = 100 / num
        print(f"100 divided by {num} is {result}.")
    except ZeroDivisionError:
        print("Error: Oops! You cannot divide by zero.")
    except ValueError:
        print("Error: Invalid input! Please enter a valid number")
# Call the function to execute the division
print("Task 1 : Demonstrating ZeroDivisionError and ValueError:")
divide_by_number()

# Task 2: Types of Exceptions
# Create a program that intentionally raises and handles the following exceptions:
#1. IndexError by accessing an invalid index in a list.
print("Task 2 : Demonstrating IndexError, KeyError, and TypeError:")
def access_invalid_index():
    my_list = [1, 2, 3]
    print("Attempting to access value at index 5 in the list:",my_list)
    try:
        print(my_list[5])
    except IndexError:
        print("Error: Index out of range. Please check the list index.")
# Call the function to demonstrate IndexError
access_invalid_index()
#2. KeyError by trying to access a non-existent key in a dictionary.
def access_invalid_key():
    my_dict = {"name": "Roni", "age": 22}
    print("Attempting to access the key 'city' in the dictionary:", my_dict)
    try:
        print(my_dict["city"])
    except KeyError:
        print("Error: Key not found in the dictionary. Please check the key.")
# Call the function to demonstrate KeyError
access_invalid_key()
#3. TypeError by adding a string and an integer.
def add_string_and_integer():
    try:
        print("Attempting to add a string and an integer: Hello + 5" )
        result = "Hello" + 5
    except TypeError:
        print("Error: Cannot add a string and an integer. Please check the data types.")
# Call the function to demonstrate TypeError
add_string_and_integer()

# Task 3: Using try-except-else-finally
# Write a program that prompts the user to enter two numbers,
# tries to divide the first number by the second, and uses try-except-else-finally to handle exceptions.
def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")
    except ValueError:
        print("Error: Please enter valid numbers.")
    else:
        print(f"The result of {num1} divided by {num2} is {result}.")
    finally:
        print("Thank you for using the division program.")
# Call the function to execute the division with try-except-else-finally
print("Task 3 : Demonstrating try-except-else-finally:")
divide_numbers()