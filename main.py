from datetime import datetime
import os

all_products = {
    1: {"name": "Milk", "stock": 50, "price": 295},
    2: {"name": "Tobleron", "stock": 20, "price": 140},
    3: {"name": "Lollipop", "stock": 10, "price": 3},
    4: {"name": "Happy", "stock": 100, "price": 5},
    5: {"name": "Canburry", "stock": 120, "price": 280},
    6: {"name": "Fries", "stock": 30, "price": 45},
    7: {"name": "Mentos", "stock": 15, "price": 30},
    8: {"name": "Cornetto", "stock": 20, "price": 35},
    9: {"name": "Oreo", "stock": 9, "price": 48},
    10: {"name": "Cheese Curls", "stock": 10, "price": 15}
}

# By Wyatt Marcus - clear screen function for readability
def clear_screen():
    # For Microsoft DOS to Windows 11
    if os.name == 'nt':
        os.system('cls')
    # For macOS, Linux, and other Unix-like systems
    else:
        os.system('clear')

# Show the user input banner options
def banner():
    print("_" * 35)
    print("Lola Nening's Store")
    print(" " * 35)
    print("  1. Show All Products")
    print("  2. Buy Product")
    print("  3. Add Products")
    print("  4. Exit")
    print("_" * 35, end="\n\n")


# Lists all products available in the store
def display_all():
    print("-" * 40)
    print("AVAILABLE PRODUCTS:")
    print("-" * 40)
    for prodid, product in all_products.items():
        print(f"Product ID: {prodid}")
        print(f"Name: {product['name']}")
        print(f"Stock: {product['stock']}")
        print(f"Price: ₱{product['price']}")
        print("-" * 40)

# Display the order summary
def order_summary(prodid, name, newquantity):
    product = all_products[prodid]
    print("_" * 35)
    print("Lola Nening's Store Order Summary")
    print(" " * 35)
    print(f"Order Summary (Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')})")
    print(f"Customer Name: {name}")
    print(f"Product: {product['name']}")
    print(f"Current Stock Quantity: {product['stock']}")
    print(f"Quantity Requested: {newquantity}")
    print(f"Total Price: {product['price']}")
    print("_" * 35)
    print("Thank you for shopping with us!", end="\n\n")

# Function to buy or commision a product
def buy_product():
    display_all()
    try:
        product_id = int(input("Enter the Product ID to buy: "))
        if product_id in all_products:
            name = input("Hello customer! Before I make any transactions, please enter your name: ")

            # If the name is empty, default to "Customer"
            if name == "":
                name = "Customer"
            
            # Just check if there's stock available
            if all_products[product_id]['stock'] <= 0:
                raise ValueError("Sorry, this product is out of stock.")
        else:
            raise ValueError(f"Invalid Product ID {product_id}. Please try again.")

        quantitytobuy = int(input("Enter the quantity you want to buy: "))
        if quantitytobuy > all_products[product_id]['stock']:
            raise ValueError("Sorry, we do not have enough stock for this product.")

        # This is the only place we should subtract from stock
        all_products[product_id]['stock'] -= quantitytobuy

        order_summary(product_id, name, quantitytobuy)

        exit(0)
    except ValueError as e:
        print(f"\nAn error has occured: {e}\nPlease make sure the input is valid, try putting a valid value like a number")
    
def add_products():
    try:
        product_id = int(input("Enter New Product ID: "))

        # Check if product ID already exists
        if product_id in all_products:
            raise ValueError(f"Product ID already exists for ID {product_id} with product name {all_products[product_id]['name']}, please try again.")

        product_name = input("Enter Product Name: ")

        # Check if product name is empty
        if product_name == "":
            raise ValueError("Product name cannot be empty, please try again.")

        product_stock = int(input("Enter Product Stock: "))

        # If the product stock is empty then its 0
        if product_stock == "":
            product_stock = 0

        product_price = float(input("Enter Product Price: "))

        # If the product price is empty then its free (aka 0)
        if product_price == "":
            product_price = 0.00

        all_products[product_id] = {
            "name": product_name,
            "stock": product_stock,
            "price": product_price
        }

        # Print the brief summary of the product added
        print("-" * 40)
        print("PRODUCT ADDED SUMMARY:")
        print(" " * 35)
        print(f"Product ID: {product_id}")
        print(f"Name: {product_name}")
        print(f"Stock: {product_stock}")
        print(f"Price: ₱{product_price}")
        print("-" * 40, end="\n")

        print("Product added successfully!")

        exit(0)
    except ValueError as e:
        #clear_screen()
        print(f"\nAn error has occured: {e}\nPlease make sure the input is valid, try putting a valid value like a number")

def main():
    banner()
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        display_all()
    elif choice == "2":
        buy_product()
    elif choice == "3":
        add_products()
    elif choice == "4":
        print("Exiting the program. Have a great day!")
        exit(0)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()