import random 
run=True
while run:
        list=("rock","paper","scissors")
        computer_choice=random.choice(list)
        user_choice=input("enter user choice:").lower()
        print(f"computer choice={computer_choice}")

        if user_choice not in list :
            print("invalid choice")
        elif user_choice==computer_choice :
             print("Tie")
        elif user_choice=="rock" and computer_choice=="scissors":
             print("You win")
        elif user_choice=="paper" and computer_choice=="rock":
            print("You win")
        elif user_choice=="scissors" and computer_choice=="paper":
            print("You win")
        else :
            print("You lost")
        x=input("enter do y want to countinue or not(YES or NO):").lower()
        if x=="yes":
            run=True
        else :
            run=False
      