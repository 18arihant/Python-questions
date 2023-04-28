# snake water gun game
def game():
    if (choice[a]==ch):
        print("No one wins, its a tie")
    elif (choice[a]=='s'and ch=='w'):
        print("computer wins")
    elif (choice[a]=='w'and ch=='s'):
        print("you wins")
    elif (choice[a]=='g'and ch=='s'):
        print("computer wins")
    elif (choice[a]=='s'and ch=='g'):
        print("you wins")
    elif (choice[a]=='g'and ch=='w'):
        print("you wins")
    elif (choice[a]=='w'and ch=='g'):
        print("computer wins")
    
    
    
print("Welcome to snake--water--gun game")
choice= ["s","w","g"]
print("Choices are--> sanke or water or gun")
print('''type s--snake
      w--water
      g--gun''')

import random
a=random.randint(0,2)
print("computer input:",choice[a])
c=input("Enter a choice:")
ch=c.lower()
game()



