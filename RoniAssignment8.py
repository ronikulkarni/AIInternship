#-------------------------------------------------
#    Author: Roni Kulkarni
#    Date : 05-27-2025
#    Implement your own data structures

#-------------------------------------------------

# Step 1: Create the Inventory
inventory = {
    "apples": (50, 1.5),
    "bananas": (30, 1.2),
    "oranges": (20, 1.0),
    "pears": (25, 1.3)
}
# Step 2: Define Functions for Inventory Management

def add_item(inventory, item, quantity, price):
    if item in inventory:
        print(f"{item} already exists in the inventory.")
    else:
        inventory[item] = (quantity, price)
        print(f"Added {item} to the inventory.")
def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
        print(f"Removed {item} from the inventory.")
    else:
        print(f"{item} does not exist in the inventory.")
def update_item(inventory, item, quantity=None, price=None):
    if item in inventory:
        current_quantity, current_price = inventory[item]
        if quantity is not None:
            current_quantity = quantity
        if price is not None:
            current_price = price
        inventory[item] = (current_quantity, current_price)
        print(f"Updated {item} in the inventory.")
    else:
        print(f"{item} does not exist in the inventory.")

# Step 3: Call the Functions
print("Original Inventory:")
for item, (quantity, price) in inventory.items():
    print(f"{item}: Quantity = {quantity}, Price = ${price:.2f}")
item = "mangoes"
add_item(inventory, item, 80, 2.5)
remove_item(inventory, "pears")
update_item(inventory, "bananas", quantity=40, price=1.1)
# Step 4: Print the Updated Inventory
print("Updated Inventory:")
for item, (quantity, price) in inventory.items():
    print(f"{item}: Quantity = {quantity}, Price = ${price:.2f}")