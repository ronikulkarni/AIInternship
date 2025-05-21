
# Ask user to input their age
age_float = float(input("How old are you? "))

# If user is 18 or older, they can vote. Otherwise, wait for an x no. of years
age = int(round(age_float)) 
x = 18 - age
if age >= 18:
    print("Congratulations! You are eligible to vote. Go make a difference!")
else:
    print("Oops! You're not eligible yet. But hey, only ", x, " years to go!")
