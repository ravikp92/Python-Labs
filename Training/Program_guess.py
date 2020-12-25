# Guess the number 
import random

randNumber=random.randint(1,5)
print(randNumber)
userGuess=None
guess=0
while(userGuess!=randNumber):
    userGuess=int(input("Enter your number between 1 to 5: "))
    guess+=1
    if(userGuess==randNumber):
        print("Your guess is  right!")
    else:
        if(userGuess<randNumber):
            print("Your guess is wrong! Please guess larger number")
        else:
            print("Your guess is wrong! Please Guess smaller number")
        

print(f"You guess the right number in  {guess} guesses")