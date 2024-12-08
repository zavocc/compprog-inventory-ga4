all_products = [
    [1, "Milk", 50, 295],
    [2, "Tobleron", 20, 140],
    [3, "Lollipop", 10, 3],
    [4, "Happy", 100, 5],
    [5, "Canburry", 120, 280]
    [6, "Fries", 30, 45]
    [7,  "Mentos", 15, 30]
    [8, "Cornetto", 20, 35]
    [9, "Oreo", 9, 48]
    [10, "Cheese Curls", 10, 15]
]

def banner():
    print("__________________________________")
    print("\tLola Nening's Store")
    print("__________________________________")
    print("\t1. Show All Products")
    print("\t2. Buy Product")
    print("\t3. Add Products")
    print("\t4. Exit")
    print("__________________________________")

def display_all():
    print("SNO\tProduct\t\tIn Stock\tPrice")
    for item in all_products:
        print("{0}\t{1}\t\t{2}\t\t{3}".format(item[0], item[1], item[2], item[3]))

def order_summary(product, 
    print("__________________________________)
    print("\tLola Nening's Store")
    print("__________________________________")
    print(f"Order Summary (Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')})")
    print(f"Customer Name: {name}")
    print(f"Product: {product[1]}")
    print(f"Quantity: 1")  
    print(f"Total Price: {product[3]}")
    print("_________________________________")
    print("Thank you for shopping with us!")

def buy_product():
    display_all()
    try:
        product_id = int(input("Enter the Product ID to buy: "))
        product = next((item for item in all_products if item[0] == product_id), None)
        if product:
            name = input("Enter your name: ")
            if product[2] > 0:  
                product[2] -= 1
                order_summary(product, name)
            else:
                print("Sorry, this product is out of stock.")
        else:
            print("Invalid Product ID. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid Product ID.")

def add_products():
    try:
        product_id = int(input("Enter New Product ID: "))
        product_name = input("Enter Product Name: ")
        product_stock = int(input("Enter Product Stock: "))
        product_price = float(input("Enter Product Price: "))
        all_products.append([product_id, product_name, product_stock, product_price])
        print("Product added successfully!")
    except ValueError:
        print("Invalid input. Please try again.")

def main():
    while True:
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
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()