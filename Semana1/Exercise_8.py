#Exercise number 8
#I need to ask the user for his weight and height 
#Then calculate the BMI of the user using the formula 
#Then show to the user: 
#"Low weight" if the user is under 18.5, "Normal", if its between 18.5 and 24.9
#"Over weight" if its between 25 and 29.9 and finally obesity if its higher or the same as 30

height = float(input("Please enter your height (Remember to use . when you add the height):"))
weight = float(input("Please enter your weight (Remember to use . when you add the weight):"))

BMI = weight / (height ** 2)

if BMI < 18.5:
    print("Low weight, go eat something :D")

elif BMI >= 18.5 and BMI <= 24.9: 
    print("You are in good shape, keep it up!")

elif BMI >= 25 and BMI <= 29.9:
    print("You have over weight, go do some exercise!")

else: 
    print("You have obesity, please fix your life")
