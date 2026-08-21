def deposit(balance):
    money=float(input("Enter the money to deposit:₹"))
    balance +=money
    print(f"₹{money} has been deposited.")
    return balance
    
def withdraw(balance):
    money=float(input("Enter the money to withdraw:₹"))  
    if money>balance:
        print("Insufficent money")
    else:  
        balance -=money
        print(f"₹{money} has been withdrawn.")
    return balance

def check_balance(balance):
    print(f"Bank Balance:{balance}.")


bank_balance=0
run=True
while run:
    print("******************")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Check Balance")
    print("4.Exit") 
    choice=int(input("Enter the your choice:"))
    match choice:
        case 1:
            bank_balance=deposit(bank_balance)
        case 2:
            bank_balance=withdraw(bank_balance)
        case 3:        
            check_balance(bank_balance)
        case 4:
            run=False    
