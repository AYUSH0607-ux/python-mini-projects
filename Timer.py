import time

def timer(number):
    seconds=number%60
    minutes=int(number/60)%60
    hours=int(number/3600)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    
number=int(input("How many seconds do u want to keep the timer:"))
for num in range(number,0,-1):
    print(timer(num))
    time.sleep(1)
print("Time has completed")