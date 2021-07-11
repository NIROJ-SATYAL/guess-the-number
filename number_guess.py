import random
import os


random_choice=random.randrange(1,101)

def easy():
    choose=input("type 'hard 'for hard  game and 'easy' for easy game:").lower()
    if choose=="hard":
        i=5
    elif choose=="easy":
        i=10
    else:
        print("type again")

    
    while i>=1:
       
        print(f"you have only {i} times")
        i=i-1
        user_guess=int(input("enter your guessing number:"))
        
        if user_guess>random_choice:
            print("Too high")
                
                
        elif user_guess<random_choice:
            print("Too low")
        elif user_guess==random_choice:
            print(f"you win.number is:{random_choice}")
            exit()
            
                

        
    print("sorry::time out")
    print(f"guessing number is:{random_choice}")


end=True
while end:
    play=input("do you want to play again:(yes or no):").lower()

    if play=="yes":
        os.system("clear")
        name=input("enter your name:")
        print(f"ok! {name}! let's play a number guessing game!!!!!!")
        print("guess the number between 1 to 100")
        easy()
    elif play=="no":
        end=False
    else:
        print("type only yes or no:")

