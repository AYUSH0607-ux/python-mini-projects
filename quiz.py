quiz=["1.What is the radius of Earth ?",
      "2.What is the value of 'g' in gravitaional force ?",
      "3.What is the battery used in most of the computers ?",
      "4.what is orange in the below options ?",
      "5.Which of the most purchased laptop ?",
      "6.What is the highest Mountain ?"]


answer=["A.6371 KM  B.6375 KM  C.6451 KM  D.None of the above",
        "A.9.8 m/s² B.9.6 m/s²  C.9.9 m/s²  D.None of the above",
        "A.Lithium ion Battery  B.Carbon Battery  C. Zinc Battery  D.Nickel Battery",
        "A.Colour  B.Fruit  C.Orange Paint D.Invisible",
        "A.Asus  B.Macbook  C.HP  D.Lenovo",
        "A.MT.Everset  B.K2  C.Kanchenjunga  D.Makala"
        ]

correct_answer=0
correct=["A","A","A","A","A","A"]
for i in range(len(quiz)):
    print("********************")
    print(quiz[i])
    print(answer[i])
    ans=input("Enter your answer:").upper()
    if ans==correct[i]:
        print("Your answer is correct")
        correct_answer+=1  
    else :
        print("your answer is incorrect")    
    print("********************")    

print(f"Your percentage is {correct_answer/len(quiz)*100:.2f}%")    
