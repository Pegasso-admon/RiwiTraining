#Exercise number 6
#Guessing a number: We need to set a hidden number then ask the user to guess it.
#Finally, tell the user if their number was greater than or smaller than the hidden number. 

UserNumber = (int(input("Please enter a number between 1 and 10 to see if you can guess the winning number: ")))

HiddenNumber = int(7)

if UserNumber == HiddenNumber: 
    print("OMG, you guessed it, congrats!")

elif UserNumber > HiddenNumber:
    print("Close! Try a smaller one. The number you entered was greater than the winning number.")

else: 
    print("Close! Try a bigger one. The number you entered was smaller than the winning number.")