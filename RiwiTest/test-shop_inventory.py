#Shop inventory
#I need to create a program that allows the user to manage a store's inventory.
#To  keep track of available products, their quantity and prices updated. 
#Also, the program must calculate the total value of the inventory.

"""
Add products: With name, price and available quantity.
Search products: By name and show (name, price, quantity).
Delete products: The program must delete a product that is not available anymore.
Calculate the total value of the inventory: The program must multiply the price by the quantity of each product and display the accumulated value.
"""

#First, I will start creating an empty dictionary. The name will be the key and the value will be a tuple of price and quantity.

inventory = {}

#Then, I will define all the functions that will help me with the CRUD that will be shown to the user later.

def add_product(name, price, quantity): 
    """This evaluates whether the product name added by the user already exists.
    Otherwise, it must be added to the inventory with its price and quantity value."""

    if name in inventory: 
        print("Oops! The product already exists.")
    else: 
        inventory[name] = (price, quantity) 
        print(f"Product '{name}' correctly added.")

def search_product(name): 
    """Basically, it is like saying "If the name you gave me is in the inventory", 
    I will index it through its values. If not, display a friendly message saying you couldn't find it."""
    if name in inventory: 
        price, quantity = inventory[name] 
        print(f"{name} - Price: ${price:.2f} - Quantity: {quantity}")
    else: 
        print("Product not found in the inventory.") 

def update(name, new_price, new_quantity): 
    """It searches for the product in the inventory by the name that the user gave and if it exists it will change the tuple.
    If the user gave an incorrect name or entered a product that is not in the inventory, it must show a friendly message."""
    if name in inventory:
        price, quantity = inventory[name] 
        inventory[name] = (new_price, new_quantity) 
        print(f"Price and quantity of '{name}' correctly updated.")
    else: 
        print("Product not found.") 

def delete_product(name):
    """
    First it ask for the product that the user wants to delete then it just delete the
    """
    if name in inventory:
        del inventory[name]
        print(f"Product '{name}' has been deleted.")
    else:
        print("Product not found.")

def calculate_total_value(): 
    """
    It scrolls through all the products in the inventory, 
    multiplies the price by the quantity of each, and sums these values to obtain and display the total value of the inventory.
    """
    total = sum(map(lambda item: item[0] * item[1], inventory.values())) 
    print(f"The total value of the inventory is: ${total:.2f}")

def validate_name(name):
    """
    It validates if the entry of the user is written only with letters and also receives spaces.
    """
    return all (word.isalpha() for word in name.split())

#Then I will ask for 5 products to add to the empty dictionary.

def menu():

    while len(inventory) < 5: 
        print("|-|-|-|-|Before we start, let’s add 5 products|-|-|-|-|")
        name = input("Please enter the name of the product that you would like to add: ")
        try: 
            price = float(input("Please enter the price of the product: "))
            quantity = int(input("Please enter the quantity: "))
            if price < 0 or quantity < 0:
                print("Error 333! Price and quantity must be positive numbers.")
                continue
            add_product(name, price, quantity)
        except ValueError:
            print("Error 404! Please enter valid values.")

    while True:
        print("\n|-|-|-|-|Shop Inventory|-|-|-|-|")
        print("1. Add product.")
        print("2. Search product.")
        print("3. Update product.")
        print("4. Delete product.")
        print("5. Calculate the total value.")
        print("6. Exit.")

        option = input("Please enter an option (1-6): ")

        if option == '1': 
            name = input("Please enter the name of the product that you would like to add: ")
            if not validate_name(name): 
                print("Error 303! Please enter a valid name(remember that it must be written in letters only.)")
                continue
            try: 
                price = float(input("Please enter the price of the product: "))
                quantity = int(input("Please enter the quantity: "))
                if price < 0 or quantity < 0:
                    print("Error 333! Price and quantity must be positive numbers.")
                    continue
                add_product(name, price, quantity)
            except ValueError: 
                print("Error 404! Please enter valid values.")
        
        elif option == '2':
            name = input("Please enter the name of the product that you are looking for: ")
            search_product(name)
        
        elif option == '3':
            name = input("Please enter the name of the product that you are trying to update the price and quantity: ")
            if not validate_name(name): 
                print("Error! Please enter a valid name.")
                continue
            try: 
                new_price = float(input("Please enter the new price: "))
                new_quantity = int(input("Please enter the new quantity: "))
                if new_price < 0: 
                    print("Error 444! Remember that the price must be a positive number.")
                    continue
                update(name, new_price, new_quantity)
            except ValueError:
                print("Error 505! Please enter a valid value.")

        elif option == '4':
            name =input("Please enter the name of the product that you want to delete: ")
            delete_product(name)

        elif option == '5':
            calculate_total_value()

        elif option == '6': 
            print("Thanks for using the program, see you soon!")
            break
        else: 
            print("Invalid option, try again!")

menu()



