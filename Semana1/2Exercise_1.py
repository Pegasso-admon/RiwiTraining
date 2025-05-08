#Exercise number 1
#I need to ask the user for three numbers
#Then use conditionals "if", to say which of those numbers is smaller

UserNumber1 = int(input("Please enter a number: "))
UserNumber2 = int(input("Please enter a number: "))
UserNumber3 = int(input("Please enter a number: "))

if UserNumber1 < UserNumber2 and UserNumber1 < UserNumber3:
    print("The first number that you enter is the smallest one: ", UserNumber1)

elif UserNumber2 < UserNumber1 and UserNumber2 < UserNumber3:
    print("The second number that you enter is the smallest one: ", UserNumber2)

elif UserNumber3 < UserNumber1 and UserNumber3 < UserNumber2:
    print("The third number that you enter is the smallest one: ", UserNumber3)

else:
    print("Oops! You repeated the numbers, try again!")