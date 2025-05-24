#-------------------------------------------------
#    Author: Roni Kulkarni
#    Date : 05-23-2025
#    Password Strength Checker

#-------------------------------------------------

pwd = input("Please enter a password: ")
# Check if the password is at least 8 characters long
if len(pwd) < 8:
    print("Your password must be at least 8 characters long.")
# Check if the password contains at least one uppercase letter
elif not any(char.isupper() for char in pwd):
    print("Your password must contain at least one uppercase letter.")
# Check if the password contains at least one lowercase letter
elif not any(char.islower() for char in pwd):
    print("Your password must contain at least one lowercase letter.")
# Check if the password contains at least one digit
elif not any(char.isdigit() for char in pwd):
    print("Your password must contain at least one digit.")
# Check if the password contains at least one special character
elif not any(char in "!@#$%^&*()-_+=<>?{}[]|;:'\",./" for char in pwd):
    print("Your password must contain at least one special character.")
# Check if the password contains any spaces
else:
    print("Your password is strong!")

# Add a password strength meter between 1 and 10
strength = 0
if len(pwd) >= 8:
    strength += 1
if any(char.isupper() for char in pwd):
    strength += 1
if any(char.islower() for char in pwd):
    strength += 1
if any(char.isdigit() for char in pwd):
    strength += 1
if any(char in "!@#$%^&*()-_+=<>?{}[]|;:'\",./" for char in pwd):
    strength += 1
if " " not in pwd:
    strength += 1
if pwd.__len__() >= 12:
    strength += 1
if pwd.__contains__("1234"):    
    strength -= 1
if pwd.__contains__("password"):
    strength -= 1
#check if the password contains any repeating characters
if len(pwd) != len(set(pwd)):
    strength -= 1
#check if the password contains any sequential characters
if any(pwd[i] == pwd[i+1] for i in range(len(pwd)-1)):
    strength -= 1

if strength == 7:  
    print("Your password strength is 10/10!")
elif strength == 6:
    print("Your password strength is 9/10!")
elif strength == 5:
    print("Your password strength is 8/10!")
elif strength == 4:
    print("Your password strength is 7/10!")
elif strength < 4:
    print("Your password strength is too low!")
