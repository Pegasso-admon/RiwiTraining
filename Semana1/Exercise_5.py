#Exercise number 5
#I need to ask the user for the total amount of an account.
#Then ask for the tipping percentage that the user wants to tip (10,15,20)
#Then calculate and show the amount of the tip 

account = float(input("Please enter the total amount of the account: "))

TipPercentage = int(input("How much would you like to tip? (10, 15 or 20) Please dont be a jerk :D= "))

TipAmount = account * (TipPercentage / 100)

print("The tip amount is: $" + str(TipAmount))



