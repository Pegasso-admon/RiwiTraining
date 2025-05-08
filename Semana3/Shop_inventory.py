# Objective: Develop a program to manage an inventory of products in a store.
# Aplying the following: Functions with parameters, lambda functions and data structures as lists, tuples and dictionaries.

""" 
Crear un programa que permita:
- Añadir productos:

    a. Cada producto debe estar definido por su nombre, precio y cantidad disponible
    b. Esta información será almacenada de modo que el inventario pueda crecer dinámicamente

- Consultar productos:

    a. Se debe poder buscar un producto por su nombre y obtener detalles como su precio y cantidad disponible
    b. Si el producto no está en el inventario, se debe notificar adecuadamente

- Actualizar productos: 
    a. El programa debe permitir al usuario seleccionar un producto e introducir un nuevo precio, asegurando que este se actualice correctamente en el inventario

- Eliminar productos: 
    a. El programa debe permitir al usuario eliminar productos del inventario de manera segura

- Calcular el valor total del inventario

    a. El programa debe calcular el valor total de los productos en inventario y mostrarlo al usuario
    b. Para ello, utilizarás una función anónima (lambda) que facilite este cálculo.

"""

# Needs: 
# The program must be designed modularly
# Store the products in a dictionary ---> The name of the product must be the key, and the price and quantity must be the values.<--- Must be store in a tuple
# CRUD 


# We will start creating an empty dictionary, the key will be the name of the product and the value will be a tuple with price and quantity

inventory = {} 

# I will define the first function "add_product" -->It is designed to add new products to the inventory

def add_product(name, price, quantity): 
    if name in inventory: 
        print("The product already exists, please use the update option if you want to change the data.")
    else: 
        inventory[name] = (price, quantity)
        print(f"Product '{name}' correctly added.")

# Additionally, I will define the second function "search_product" --> It is designed to search the name of a product in the inventory and also gives product
# details, such as the price and the quantity 

def search_product(name): 
    if name in inventory: 
        price, quantity = inventory[name]
        print(f"{name} - Price: ${price} - Quantity: {quantity}")
    else: 
        print("Product not found in the inventory.")

# Then, I will define a third function "update_price" --> It is designed to update the price of a existing product in the inventory 
# It will take two parameters: the "name" of the product that I would like to update the price and "new_price" will be the new price to be assigned to the product 

def update_price(name, new_price):
    if name in inventory:
        _, quantity = inventory[name]
        inventory[name] = (new_price, quantity)
        print(f"Price of '{name}' correctly updated.")
    else: 
        print("Product not found.")

# Then, I will define a fourth function "delete_product" --> It is designed to delete a existing product in the inventory

def delete_product(name):
    if name in inventory:
        del inventory[name]
        print(f"Product '{name}' has been deleted.")
    else:
        print("Product not found.")

# Then I will define a fifth function "calculate_total_value" --> It is intended to calculate the total value of all products currently in inventory 
# it scrolls through all the products in the inventory, multiplies the price by the quantity of each, and sums these values to obtain and display the total value of the inventory.

def calculate_total_value():
    total = sum(map(lambda item: item[0] * item[1], inventory.values()))
    print(f"The total value of the inventory is: ${total}")

# I will define a function to validate the name, it must contain lettes and spaces
def validate_name(name):
    return all (word.isalpha() for word in name.split())

# Now I will define the function of the interactive menu
# It will show the interactive menu to manage the inventory

def menu(): 
    while True:
        print("\n|-|-|-|-|Shop Inventory|-|-|-|-|")
        print("1. Add product.")
        print("2. Search product.")
        print("3. Update price.")
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
                price = float(input("Please enter the price of the prodcut: "))
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
            name = input("Please enter the name of the product that you are trying to update the price: ")
            if not validate_name(name): 
                print("Error! Please enter a valid name(remember that it must be written in letters only.)")
                continue
            try: 
                new_price = float(input("Please enter the new price: "))
                if new_price <0: 
                    print("Error 444! Remember that the price must be a positive number.")
                    continue
                update_price(name, new_price)
            except ValueError:
                print("Error 505! Please enter a valid price.")

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