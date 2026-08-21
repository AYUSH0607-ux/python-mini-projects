import random
symbols=("☠️","🦅","🐬","❤️")
amount=int(input("Enter your amount:₹"))
run=True

while run:
    slot=[]
    bet=int(input("Enter your bet:₹"))
    if 0<bet<=amount:
        for i in range(0,3):
            emoji=random.choice(symbols)
            slot.append(emoji)
            print(emoji,end="  ")
        print()    
        if slot[0]==slot[1]==slot[2]:
            print(f"You won ₹{10*bet}")
            amount+=10*bet
        else :
            print("You lost")
            amount-=bet
        run1=input("Enter 'y' to continue or 'n' to stop:") 
        if run1=="n":
            run=False

    else :
        print("Insufficient money")
        run=False

print(f"Your total amount is ₹{amount}")        
