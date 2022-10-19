import random

def Play_Rock_Paper_Scissor():
    your_choice = input("please  Enter the 'r' as Rock 'p' as Paper and 's' as Scissor?:  ")
    computer_choice = random.choice (['r','p','s'])
    
    if your_choice==computer_choice:        
        print('the play is equal (play again)')
    elif (your_choice=='r' and computer_choice=='s')or(your_choice=='p' and computer_choice=='r')\
    or(your_choice=='s' and computer_choice=='p'):
        print('congrajulation you win')   
    else:
        print('sorry you lose game')

print(Play_Rock_Paper_Scissor())
    
