#Exercise number 5
#I need to create a list with some names 
#Then ask the user for his name 
#Then I need to use "if", to tell the user if its in the list that I created at the begginning or is not in the list

InvitedList = ["SAMUEL", "Samuel", "samuel", "PEPITO", "Pepito", "pepito", "FULANO", "Fulano", "fulano"]

UserName = input("Please enter (only) your name to see if you are invited :D: ")

if UserName in InvitedList:
    print("You are invited!")

else:
    print("You are not invited :(")