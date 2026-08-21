import random  
number=random.randint(1,1000)
guesses=0
run=True
while run :
    guesses +=1
    guess=int(input("Enter the number(between 1 to 1000):"))
    if guess<number :
        print(f" {guess} is lesser than Number")
    elif guess>number :
        print(f" {guess} is greater than Number")
    else :
        print(f"Your guess is correct")
        run=False
print(f"It took {guesses} number of guesses")        