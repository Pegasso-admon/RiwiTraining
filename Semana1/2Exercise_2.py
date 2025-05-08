#Exercise number 2
#I need to create a list with 5 numbers 
#Then ask the user for a number and verify if that number is in the list using "in"

NumbersList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

UserNumber = int(input("Hi, please enter a number, we will tell you if its in the list :D: "))

if UserNumber in NumbersList:
    print("The number is in the list!")

else:
    print("The number is not in the list :(")
