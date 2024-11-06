import random
rock=1
paper=2
secisor=3

computer=random.choice([1,2,3])
revdict={1:"Rock",2:"Paper",3:"Secisor"}
you=input("Enter you choice (R,P,S): ")
youDict={
  "r":1,
  "R":1,
  "p":2,
  "P":2,
  "s":3,
  "S":3
}
your=youDict[you]
print(f"Computer choose {revdict[computer]}\nYou choose {revdict[your]}")
if(computer==your):
  print("Game Draw! Play again")
else:
    if(computer==1 and your==2): 
      print("you Win!")
    elif(computer==1 and your==3):  
      print("you Lose")
    elif(computer==2 and your==1):  
      print("you lose!")
    elif(computer==2 and your==3):  
      print("you win!")
    elif(computer==3 and your==1):  
      print("you win!")
    elif(computer==3 and your==2):  
      print("you lose")
    else:
      print("somthing went wrong! try again")