import random
import string

length=int(input("Enter the length of the password:"))
characters=string.ascii_letters+string.digits+string.punctuation
password=""
for x in range(0,length):
    password+=random.choice(characters)

print(f"Your password is ({password})")    
