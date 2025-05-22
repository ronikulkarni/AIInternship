#------------------------------
# Author: Roni Kulkarni
# Date: May 21, 2025
# Loops assignment
#------------------------------

# Task 1 - Counting Down with Loops

# Ask user to input a starting number
print("Let's countdown with loops!")
start = int(input("Please enter a number "))

end = 1

while start >= end:
    print(start)

    start -= 1
print("Blast off!")

# Task 2 - Multiplication Table with For Loops
print("Let's do multiplication tables with loops!")
num = int(input("Please enter a number "))
for i in range(1, 11):
    print(num, " * ", i, " = ", i*num)


# Task 3 - Find the Factorial
print("Let's find the factorial of a number with loops!")
num = int(input("Please enter a number "))
factorial = num

for i in range(1, num):
    factorial = factorial * i
print("The factorial of" , num, "is" , factorial)
