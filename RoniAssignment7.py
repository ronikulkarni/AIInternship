#-------------------------------------------------
#    Author: Roni Kulkarni
#    Date : 05-26-2025
#    Password Strength Checker

#-------------------------------------------------
# Task 1 - Working with Lists
# Create a list of fruits
print("TASK 1 - Working with Lists")
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# Add a new fruit to the list
fruits.append("fig")
# Print the appended list
print("List after appending a new fruit:", fruits)
# Remove a fruit from the list
fruits.remove("banana")
# Print the list after removing a fruit
print("List after removing a fruit:", fruits)
# Print the reversed list using slicing
fruits = fruits[::-1]
print("Reversed list of fruits:", fruits)
print("")

# Task 2 - Exploring Dictionaries
# Create a dictionary to store information about yourself with the following keys: name, age, and city
print("TASK 2 - Exploring Dictionaries")
my_info = {
    "name": "Roni Kulkarni",
    "age": 22,
    "city": "Westbury"   
}
# Add a new key-value pair for your favorite color
my_info["favorite_color"] = "blue"

# Print the dictionary
print("My Information Dictionary:", my_info)

# Update the city key with a new value
my_info["city"] = "Jericho"
# Print the updated dictionary
print("Updated My Information Dictionary:", my_info)
# Print all keys and values in the dictionary using a for loop
for key, value in my_info.items():
    print(f"{key}: {value}")
print("")

# Task 3 - Using Tuples
print("TASK 3 - Using Tuples")
# Create a tuple with three elements: your favorite movie, song, and book
favorite_tuple = ("Wreck it Ralph", "Story of My Life", "Outliers by Malcolm Gladwell")
# Print the tuple
print("Favorite Tuple:", favorite_tuple)
# Try to change an element in the tuple (this will raise an error)
try:
    favorite_tuple[0] = "Despicable Me"
except TypeError as e:
    print("Error:", e)
# Print the length of the tuple using the len() function
print("Length of the favorite tuple:", len(favorite_tuple))
