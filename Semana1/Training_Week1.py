#Product validation system
#I need to create a program that calculates the total cost of a purchase 
#4 Essentials--->
#Name of the product 
#The unit price 
#The quantity of the product 
#The percentage of the discount if there is one
#Price and quantity must be positive numbers and the discount must be in the range of 0 and 100    

#First I need to ask the user to enter the data 
ProductName = input("Please enter the product name that you would like to purchase: ")

#Then I need to validate the unit price(How much does one unit of the product cost)

while True:
    try:
        UnitPrice = float(input("Please enter the price of one unit of the product that you would like to purchase: "))
        if UnitPrice <= 0: 
                print("Oops! Please enter a positive number.")
        else: 
             break
    except ValueError :
        print("Oops! Please enter a valid number.")

#Then I need to validate the product quantity

while True:
    try: 
        ProductQuantity = int(input("Please enter the quantity of the product that you are going to purchase: "))
        if ProductQuantity <= 0:
            print("Oops! Please enter a positve number.")
        else:
            break
    except ValueError:
        print("Oops! Please enter a valid number.")

#Then I need to validate that the discount is in the range 

while True:
     try: 
        ProductDiscount = float(input("Please enter the discount that the product has: "))
        if 0 <= ProductDiscount <= 100: 
            break
        else:
            print("Please enter a number between 0 and 100,  try again.")
     except ValueError:
         print("Please enter a valid number.")

#Then I need to calculate total cost of the purchase

NoDiscount = UnitPrice * ProductQuantity
Discount = NoDiscount * (ProductDiscount / 100)
TotalAmount = NoDiscount - Discount

#Then I need to show the bill to the user showing the following: 
#Product name, unit price, the product quantity, the price without discount, the price with discount

print(f"""Here is your bill
       
You purchased: {ProductName}.

The unit price of the product that you purchased was: {UnitPrice: .2f}.
       
The amount of products you purchased was: {ProductQuantity}  

The total price without discount was: {NoDiscount: .2f}

The discount was: {Discount: .2f}

The total cost of the purchase was: {TotalAmount: .2f}
       
""" )           

    