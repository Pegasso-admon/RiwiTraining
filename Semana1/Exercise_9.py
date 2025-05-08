#Exercise number 9
#I need to ask the user for a year
#Determine if it is a leap year

UserYear = int(input("Please enter a year (we will tell you if its a leap year): "))

if(UserYear % 4 == 0 and UserYear % 100 != 0)or(UserYear % 400 == 0):
    print("The year that you enter its a leap year :D!")

else: 
    print("The year that you enter is not a leap year D:")