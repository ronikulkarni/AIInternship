#-------------------------------------------------
#    Author: Roni Kulkarni
#    Date : 05-23-2025
#    Exploring String Methods

#-------------------------------------------------
# Task 1-String Slicing and Indexing
str = "Python is amazing!"

# extract using slicing
print("Extracting the first 6 characters ", str[0:6])
print("Extracting the word amazing ", str[10:17])
print("String in reverse order ", str[::-1])

# Task 2-String Methods
str2 = " hello, python world! "
str2 = str2.strip()  # Remove leading and trailing spaces
print("Removing extra spaces ", str2)
print("Capitalizing the first letter ", str2.capitalize())
print("Replacing 'world' with 'universe' ", str2.replace("world", "universe"))
print("Converting to uppercase ", str2.upper())

# Task 3-Check for Palindromes
word = input("Please enter a word to check for palindrome: ")
reverseWord = word[::-1]
if (word == reverseWord):
    print("The word is a palindrome!")
else:
    print("The word is not a palindrome!")