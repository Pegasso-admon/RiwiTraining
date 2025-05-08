#Exercise number 10 
#I need to ask the user for a number 
#Then the program needs to tell the user if the number is between 1 and 10

UserNumber = int(input("Please enter a number: "))

if UserNumber >= 1 and UserNumber <= 10:
    print("The number that you enter is between 1 to 10")

else: 
    print("The number that you enter is not between 1 to 10")