#Exercise number 7
#I need to ask the user to enter two numbers
#After that, the program will print the bigger one and if the numbers are the same the program will mention it

number1 = int(input("Please enter a number: "))
number2 = int(input("Please enter a number: "))

if number1 > number2: 
    print(number1, "is bigger than", number2)

elif number2 > number1:
    print(number2, "is bigger than", number1)

elif number1 == number2:
    print("The numbers are the same.")



