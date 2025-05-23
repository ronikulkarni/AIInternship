#-------------------------------------------------
#    Author: Roni Kulkarni
#    Date : 05-22-2025
#    Number Guessing Game

#-------------------------------------------------


import random
randomNum = random.randint(1, 100)

userNum = 0
numAttempts = 0

while(userNum != randomNum):
    userNum = int(input("Please enter a number between 1 and 100 "))
    numAttempts = numAttempts + 1
    if (numAttempts == 10):
        print("Game over! Better luck next time!")
        break
    if (userNum > randomNum):
        print("Too high! Try again.")
    elif (userNum < randomNum):
        print("Too low! Try again.")
    else:
        print("Congratulations! You guessed it in" , numAttempts, "attempts!")
        break
    