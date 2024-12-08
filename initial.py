# Please check the flow
# https://amazing-artichoke-67f.notion.site/Computer-Programming-Inventory-1488b592586280ba859ddba53db888ae?pvs=74

# Prerequisite: https://learnpython.org/en/Dictionaries
# Learn dictionaries
import json
import os

INVENTORY_DATA = "inventory_data.json"

# Check if we have inventory file
if not os.path.exists(INVENTORY_DATA):
    raise FileNotFoundError(f"File {INVENTORY_DATA} not found")

inventory_data: dict = None
with open(INVENTORY_DATA, "r") as inventory_data_file:
    inventory_data = json.load(inventory_data_file)

# print(inventory_data)
# The inventory_data is a dictionary please see: 
# https://learnpython.org/en/Dictionaries

# Functions
# It is organized to these parts
# operation_add_stock, operation_remove_stock, and operation_deploy_stock are options when running this file
# tool_save_inventory

# Function to save inventory data
def tool_save_inventory(inventory_data: dict):
    if not type(variable_inventory_data) == dict:
        raise TypeError("Inventory Data is not valid")

    with open(INVENTORY_DATA, "w") as inventory_data_file:
        json.dump(inventory_data, inventory_data_file)

# You can add welcome message code here

# Function add entry to inventory
def operation_add_stock():
    # Preloaded variables, use input and reassign these variables
    product_id = None
    product_name = None
    product_quantity = None
    product_in_production = False

    # Use inventory_data variable
    # What you're going to do is implmenet the input and validation logic

    # Input valid product ID
    # Check if product ID exists in inventory_data dictionary variable, if it does, raise an error message
    # Input product name
    # Input product quantity and must be an integer: int(input("quantity"))
    # Input if the product is in production? accepted values are only Y or N

    # Override inventory_data variable with updated one
    # Do not remove this line unless you know what you're doing, this will create a new dictionary entry
    inventory_data[product_id] = {
        "name": product_name,
        "quantity": product_quantity,
        "production_pending": product_in_production
    }

    # Call tool_save_inventory(inventory_data)
    tool_save_inventory(inventory_data)

    # Also, give them a message that it is successful
    # You can also use pretty python libraries like colorama or if you want to like make text rainbow, great
    # Or anything that indicates success

    
def operation_remove_stock():
    # Preloaded variables
    product_id = None

    # You only need to check and find product ID and delete it using dictionary methods

    # Hmm, yeah, as I said.... inventory_data variable is a dictionary
    # What you're gonna do is to find a dictionary key :)

    # Search on google "check if key exists in"
    # AI Prompt: how to delete a specific key from the dictionary
    # Challenge: DO NOT MENTION INVENTORY, I want you to learn how to delete specific entries in the dictionary :)
    # And product ID is the "dictionary key" which the value is a dictionary with given data

    # OK HERE ARE THE STEPS NOW:
    # 1. User input product ID
    # 2. Check if product ID exists in the dictionary as key
    if not product_id in inventory_data:
        # IMPLEMENT ERROR LOGIC HERE
        pass
    # 3. When product ID is found in inventory_data dictionary, delete the key from inventory_data dictionary
    # 4. Call tool_save_inventory(inventory_data)
    tool_save_inventory(inventory_data)

def operation_deploy_stock():
    # Preloaded variables
    product_id = None

    # 1. User input for product ID
    # 2. Again if product ID doesn't exist in the inventory_data dictionary keys, must throw an error - DONE
    if not product_id in inventory_data:
        # IMPLEMENT ERROR LOGIC HERE
        pass
    # 3. When product ID is found in inventory_data dictionary, use the deploying_product variable
    deploying_product = inventory_data[product_id]
    # 4. After that. let's check for the product quantity status
    #
    # If the product is still producing yet the stock quantity are low, give warning
    if deploying_product[production_pending] == True and deploying_product[quantity] < 20:
        # Warning and proceed to continue the flow
        pass
    # If the product isn't producing from the manufacturer and the stock quantity are low, means product failed or really high in demand
    # Which sales cannot be justified here
    elif deploying_product[production_pending] == False and deploying_product[quantity] < 20:
        # MUST TERMINATE THE PROGRAM IMMEDIATELY AND PRINT OR RAISE AN ERROR
        pass
    #
    # 5. Next, user input how much the product should be 
    # IT MUST BE AN INTEGER AND SHOULD THROW AN ERROR IF ITS NOT AN INTEGER
    num_of_product = None # Add input here
    # 
    # Ok user input achieved, but, check if the original deploying_product[quantity] is less than num_of_product
    # If num_of_product input IS HIGHER than deploying_product[quantity] which is the original, then error it out
    if deploying_product[quantity] < num_of_product:
        # ERROR AND EITHER YOU IMPLEMENT QUIT OR RETRY BY LOOPING
        pass

    # 6. If the above condition results NO ERRORS, subtracting and updating
    new_quantity = deploying_product[quantity] - num_of_product

    # 7. Update and save, do not modify this
    deploying_product[quantity] = new_quantity
    inventory_data[product_id] = deploying_product
    tool_save_inventory(inventory_data)


# IMPLEMENT USER INPUT HERE DETERMINE WHAT TO DO
# Id expect when the program runs, it must be like this or similar:
##########################################################
# C:\Users\zavocc306> python main.py
# What do you to do?
# 1. Add stock or products to the stocks -> call operation_add_stock()
# 2. Remove specific item or products from the stocks -> call operation_remove_stock()
# 3. Deploy products from the stocks that are ready to be sold and shelved -> call operation_deploy_stock()
# 4. Exit -> exit()
# ENTER YOUR SELECTION: 5
# INVALID CHOICE! TRY AGAIN
# ENTER YOUR SELECTION: 1
# ........ calling operation_add_stock() ...............
