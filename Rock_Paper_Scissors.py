import os; os.system("cls") 
import random

play=0

name=input("Enter your name : ")
print()

global computer_score
computer_score=0

global user_score
user_score=0

def rps():

            


    # Random_choice
    lst=["Rock","Paper","Scissors"]
    computer=random.choice(lst)

    # Rock_paper_scissor_input    
    print("Rock paper Scissors Shoot !!!")
    rps_inp=input("Enter R, P or S : ")
    user=rps_inp.lower()

    # Rock
    if computer=="Rock" and user=="s":
        print(f"\nRock beats Scissors. {name.capitalize()} lost the match !!!")
        global computer_score
        computer_score+=1

    elif computer=="Rock" and user=="p":
        
        print(f"\nPaper beats Rock. {name.capitalize()} won the match !!!")
        global user_score
        user_score+=1     
    
    elif computer=="Rock" and user=="r":
        print("\nTie !!!")


    # Paper
    elif computer=="Paper" and user=="r":
        print(f"\nPaper beats Rock. {name.capitalize()} lost the match !!!")
        computer_score+=1

    elif computer=="Paper" and user=="s":
        print(f"\nScissors beats Paper. {name.capitalize()} won the match !!!")
        user_score+=1

    elif computer=="Paper" and user=="p":
        print("\nTie !!!")


    # Scissors
    elif computer=="Scissors" and user=="p":
        print(f"\nScissors beats Paper. {name.capitalize()} lost the match !!!")
        computer_score+=1

    elif computer=="Scissors" and user=="r":
        print(f"\nRock beats Scissors. {name.capitalize()} won the match !!!")
        user_score+=1

    elif computer=="Scissors" and user=="s":
        print("\nTie !!!")

    # Invalid_handle
    else:
        print("Enter R, P or S only !!!\n")

    # Results
    print("Computer score :",computer_score)
    print(name.capitalize(),":",user_score,"\n")

       
# Results    
print("Computer score :",computer_score)
print(name.capitalize(),":",user_score,"\n")

while play<10:
    rps()
    play+=1



























































