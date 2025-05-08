#Exercise number 3
#I need to ask the user for a number
#The program will tell the user if the number is even or odd

number = int(input("Please enter a number, we will tell you if the number is even or odd:"))

if number % 2 == 0:
    print ("The number is even.")

else: 
    print ("The number is odd.")