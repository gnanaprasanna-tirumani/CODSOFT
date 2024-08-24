import random
again='y'
while again=='y' or again=='Y':
    user_choice=int(input("rock-0\npaper-1\nscissors-2\n"))
    computer_choice=random.randint(0,2)
    if(computer_choice==0):
        print("computer choose rock")
    elif(computer_choice==1):
        print("computer choose paper")
    elif(computer_choice==2):
        print("computer choose scissors")
    else:
        print("invalid option\n")
        exit
    if(user_choice==computer_choice):
        print("it was a tie")
    elif(computer_choice==2 and user_choice==0):
        print("computer won")
    elif(computer_choice==0 and user_choice==2):
        print("you won")
    elif(user_choice+1==computer_choice):
        print("computer wins")
    elif(computer_choice<user_choice):
        print("you won")
    again=input("do you want to continue(y/Y):")

