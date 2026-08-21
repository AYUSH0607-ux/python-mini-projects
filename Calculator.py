print("Enter '+' for Addition")
print("Enter '-' for Subtraction")
print("Enter '*' for Multiplication")
print("Enter '/' for Division ")
choice=input("What you want to perform:")
if choice== "+" :
    x=float(input("Enter the numbers:"))
    y=float(input("Enter the other number:"))

    print(f"Addition is {x+y:.2f}")    

elif choice=="-":
    x=float(input("Enter the numbers:"))
    y=float(input("Enter the other number:"))
    print(f"Substraction is {x-y:.2f}")

elif choice=="*":
    x=float(input("Enter the numbers:"))
    y=float(input("Enter the other number:"))
    print(f"Multiplication is {x*y:.2f}")

elif choice== "/":
    x=float(input("Enter the divident:"))
    y=float(input("Enter the divisor:"))
    if y==0:
        print("0 can be used as a divisor choose another diviser")
        y=float(input("Enter the divisor:"))
        print(f"Division is {x/y:.2f}") 
    else:
        print(f"Division is {x/y:.2f}")    

else :
    print("Invalid choice")
    
