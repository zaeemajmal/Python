import random
import time
print("-->Welcome to hand cricket V 0.1<--")
team_name = input("Enter team name- ")
print("Now time for the toss")
who_chooses_toss = random.randint(1,2)
print(who_chooses_toss)
Coin = ["Heads","Tails"]
Bat_or_bowl = ["Bat","Bowl"]
toss = random.choice(Coin)
if who_chooses_toss == 1:
    ai_choose = random.choice(Coin)
    print("AI Chooses-",ai_choose)
    print("Toss loading...")
    time.sleep(2) 
     
       
    if ai_choose == toss:
        print("AI won the toss!")
        ai_choose = random.choice(Bat_or_bowl)
        time.sleep(2)
        if ai_choose == "Bat":
            print("AI chooses to bat!")
           
        else:
            print("AI chooses to field")
            print("You choose to bat!")
                
        
    else:
        print("You won the toss!")
        bat_or_Bowl = input("Enter choice Bat or bowl")
        time.sleep(2)
        if bat_or_Bowl == "Bat":
            print("You choose to bat!")
            
        else:
            print("You choose to field")
            
        
else:
    choose = str(input("Enter Heads or Tails- "))   
    print("You Choose",choose)
    print("Toss loading",end="")
    time.sleep(2) 
    print("...") 
    time.sleep(2)   
    if choose == toss:
        print("You won the toss!")
        bat_or_Bowl = input("Enter choice Bat or bowl")
        time.sleep(2)
        if bat_or_Bowl == "Bat":
            print("You choose to bat!")
        else:
            print("You choose to field") 
    else:
        print("AI won the toss!")
        ai_choose = random.choice(Bat_or_bowl)
        time.sleep(2)
        if ai_choose == "Bat":
            print("AI chooses to bat!")
        else:
            print("AI chooses to field")    

total_wickets = int(input("Enter total wickets- "))
total_balls = int(input("Enter number of Balls- "))












