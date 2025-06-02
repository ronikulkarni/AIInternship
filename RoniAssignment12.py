#-------------------------------------------------
#    Author: Roni Kulkarni
#    Date : 05-30-2025
#    Calculator with Exception Handling

#-------------------------------------------------
# Step 1: Menu of Operations
# Create a program that displays a menu of operations for the user to choose from.
def display_menu():
    print("Welcome to the Menu Program!")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
# Call the function to display the menu
display_menu()
# Step 2: Input Validation
# Add input validation to ensure the user enters numbers only for the calculations. If the input is invalid, catch the exception and prompt the user to enter a valid number.
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
# Step 3: Division with Exception Handling
# Handle the following exceptions specifically for the division operation:
def divide_numbers(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Error: Cannot divide by zero. Please enter a non-zero divisor.")
        return None
# Step 4: Logging Errors (Bonus)
# Use a logging module to log errors to a file named "error_log.txt" if any exceptions occur.
import logging
logging.basicConfig(filename='error_log.txt', level=logging.ERROR)
def log_error(error_message):
    logging.error(error_message)
# Step 5: User-Friendly Interface
def main():
    while True:
        display_menu()
        choice = input("Please choose an operation (1-5): ")
        
        if choice == '1':
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            print(f"The result of addition is: {num1 + num2}")
        
        elif choice == '2':
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            print(f"The result of subtraction is: {num1 - num2}")
        
        elif choice == '3':
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            print(f"The result of multiplication is: {num1 * num2}")
        
        elif choice == '4':
            num1 = get_number("Enter the numerator: ")
            num2 = get_number("Enter the denominator: ")
            result = divide_numbers(num1, num2)
            if result is not None:
                print(f"The result of division is: {result}")
        
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please select a valid option from the menu.")
if __name__ == "__main__":
    main()
    # Log any errors that occur during the execution
    try:
        main()
    except Exception as e:
        log_error(f"An error occurred: {e}")
        print("An error occurred. Please check the error_log.txt file for details.")