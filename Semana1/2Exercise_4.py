#Exercise number 4
#I need to ask the user for his age
#If the age of the user is smaller than 0 or higher than 120, then print "No valid age, try again!"
#If it is between the correct range, then print "Valid age, keep it up!"

UserAge = int(input("Please enter your age :D: "))

if UserAge < 0 or UserAge > 120:
    print("No valid age, try again!")

else:
    print("Valid age, keep it up!")

