def add():
    work=input("Enter the work you want to add:")
    do_list.append(work)
    print("work had been added")

def remove_task():
    if len(do_list)==0:
        print("list is empty")
    else :
        view()
        choice=int(input("Enter the index of the work to remove:"))
        if choice<1 or choice>len(do_list):
            print("Invalid choice.") 
        else :
            context=do_list.pop(choice-1)
            print(context)
            print(f"work has been removed")      

def view():
    if len(do_list)==0:
            print("No works in list.") 
    else :        
        print("***********")
        print("Works to do:")
        for index,work in enumerate(do_list,start=1):
            print(index,work)
        print("***********")    

do_list=[]
run=True
while run:
    print("******************")
    print("Enter 1 to add a work")
    print("Enter 2 to remove a work")
    print("Enter 3 to view all the works")
    print("Enter 4 to exit")
    choice1=(input("Enter your choice(between 1 to 4):"))
    match choice1 :
        case 1:
            add()
        case 2:
            remove_task()
        case 3:
            view()
        case 4:
            run=False 
        case _:
            print("wrong choice")
    print("******************")        
           
