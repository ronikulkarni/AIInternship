#-------------------------------------------------
#    Author: Roni Kulkarni
#    Date : 05-29-2025
#    About Menu

#-------------------------------------------------

# Step 2: Define Functions for Each Choice
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)
    
def find_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return find_fibonacci(n - 1) + find_fibonacci(n - 2)
    

def draw_fractal(n):
    if n == 0:
        return
    else:
        print("Drawing fractal level", n)
        draw_fractal(n - 1)     
        print("Completed fractal level", n) 


# Step 1: Create a Menu of Choices for User 
#1.Calculate the factorial of a number.
#2.Find the nth Fibonacci number.
#3.Draw a recursive fractal pattern (bonus).
#4.Exit
input_choice = 0
# Keep prompting the user until they choose to exit
while input_choice < 1 or input_choice > 4: 
    print("Welcome to the Recursive Artistry Program! ")
    print("1. Calculate Factorial")
    print("2. Find Fibonacci")
    print("3. Draw a Recursive Fractal")
    print("4. Exit")
    
    try:
        input_choice = int(input("Please choose an option (1-4): "))
        if input_choice < 1 or input_choice > 4:
            print("Invalid choice! Please select a valid option from the menu.")
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 4.")

    # Step 3: Handle User Choices
    if input_choice == 1:
        try:
            num = int(input("Enter a non-negative integer to calculate its factorial: "))
            if num < 0:
                print("Error: Factorial is not defined for negative numbers.")
            else:
                result = calculate_factorial(num)
                print(f"The factorial of {num} is {result}.")
        except ValueError:
            print("Error: Please enter a valid non-negative integer.")
    
    elif input_choice == 2:
        try:
            n = int(input("Enter a non-negative integer to find its Fibonacci number: "))
            if n < 0:
                print("Error: Fibonacci is not defined for negative numbers.")
            else:
                result = find_fibonacci(n)
                print(f"The Fibonacci number at position {n} is {result}.")
        except ValueError:
            print("Error: Please enter a valid non-negative integer.")
    
    elif input_choice == 3:
        try:
            level = int(input("Enter the level of the fractal to draw (non-negative integer): "))
            if level < 0:
                print("Error: Fractal level cannot be negative.")
            else:
                draw_fractal(level)
        except ValueError:
            print("Error: Please enter a valid non-negative integer.")
    elif input_choice == 4:
        print("Exiting the program. Thank you for using the Recursive Artistry Program!")
        break
# End of the program

