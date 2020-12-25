# Program to play snake water and gun 
import random


def game(a,b):
    if(a==b):
        return None
    if(a=='s'):
        if(b=='w'):
            return False
        elif(b=='g'):
            return True
    if(a=='w'):
        if(b=='s'):
            return True
        elif(b=='g'):
            return False
    if(a=='g'):
        if(b=='s'):
            return False
        elif(b=='w'):
            return True

print("Comp Turn: Snake(s) Water(w) or Gun(g) ?")
randNo= random.randint(1,3)
if randNo == 1:
    comp='s'
elif randNo == 2:
    comp='w'
elif randNo == 3:
    comp='g'


b=input("Players Turn: Snake(s) Water(w) or Gun(g) ?")

match=game(comp,b)

print(f"Comp choose {comp}")
print(f"You choose {b}")

if(match== None):
    print("Game is Tie")
elif(match):
    print("Game is Won By You")
else:
     print("You Lose")

