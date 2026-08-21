shop={"tomato" : 20,
      "onion" : 30,
      "potato":25,
      "chips":30,
      "chocolate":100,
      "soda":10,
      "cup noodles":50,
      "ice cream":100
      }
cart=[]
cart_value=0
quantity=[]
run=True
while run :
    item=input("Enter the things u want to purchase:").lower()
    cart.append(item)
    num=int(input("Enter the quantity of the product(Each vegetable is 1KG,others are 1 quantity):"))
    quantity.append(num)
    choice=input("Do you want to countinue or not(y or n)").lower()
    if choice=="n":
        run=False   
i=0
for i in range(0,len(cart)):
    item=cart[i]
    qty=quantity[i]
    if item in shop:
        value=shop[item]*qty
        print(f"{item}={value}")
        cart_value+=value
    else :
        print(f"{item} is not in the shop")    
print(f"Total is {cart_value}")    
        
