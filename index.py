print("WELCOME TO MY GUESSING GAME 🙏 ")
print("I AM CHECKING YOUR GUESSING SKILL.")
name=input("Enter your name :- ")
print("HELLO !",name)
import random
Computer_Number=random.randrange(1,6)
Attempt=3
sol=0
print("Choose the number between 1 t0 5")
while Attempt>0:
    User_Number=int(input("Enter the number:- "))
    print("NOW YOU ONLY PLAY",Attempt,"TIMES")
    if User_Number>Computer_Number:
       
        print(User_Number, "your guess number too high")
    elif User_Number<Computer_Number:
      
        print(User_Number, "your guess number too low")
    else:
        print(Computer_Number, "Computer Number")
        print(User_Number, "your guess number is correct 👍")
        print("🥳 HURRY YOU WIN THE GAME 🥳")
        sol=1
        break
    Attempt-=1
if sol==0:
    print("THANKS FOR PLAYING, BETTER LUCK NEXT TIME")

      



        