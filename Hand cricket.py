import random
print("Welcome to Hand Cricket!")
print("Enter which level you want to play:")
print("Easy")
print("Medium")
print("Hard")
Level = input()
target = None
if Level == "Easy" or Level == "easy":
    Choice = input("You choose to Bat or Field- ")
    total_wickets = int(input("Enter total wickets- "))
    if Choice == "Bat" or Choice == "bat":
        runs = 0
        wickets = 0
        while wickets != total_wickets:
            choice = int(input('Enter number from 0 to 10- '))
            ai_choice = random.randint(0,10)
            if choice == ai_choice:
                wickets = wickets + 1
            else:
                runs = runs + choice
            print(runs," - ",wickets)
        print("All out, now time to field!")  
        target = runs
        ai_runs = 0
        ai_wickets = 0
        while target > ai_runs or ai_wickets != total_wickets:
            choice = int(input('Enter number from 0 to 10- '))
            ai_choice = random.randint(0,10)
            if ai_choice == choice:
                ai_wickets = ai_wickets + 1
            else:
                ai_runs = ai_runs + ai_choice
            print(ai_runs," - ",ai_wickets)
        
    elif Choice == "Field" or Choice == "field":
        ai_runs = 0
        ai_wickets = 0
        while ai_wickets != total_wickets:
            choice = int(input('Enter number from 0 to 10- '))
            ai_choice = random.randint(0,10)
            if ai_choice == choice:
                ai_wickets = ai_wickets + 1
            else:
                ai_runs = ai_runs + ai_choice
            print(ai_runs," - ",ai_wickets)
        print("All out good job now time to bat!")
        target = ai_runs    
        runs = 0
        wickets = 0
        while runs < target or wickets != total_wickets:
            choice = int(input('Enter number from 0 to 10- '))
            ai_choice = random.randint(0,10)
            if choice == ai_choice:
                wickets = wickets + 1
            else:
                runs = runs + choice
            print(runs," - ",wickets)
        
elif Level == "Medium" or Level == "medium":
    Choice = input("You choose to Bat or Field- ")
    total_wickets = int(input("Enter total wickets- "))
    if Choice == "Bat" or Choice == "bat":
        runs = 0
        wickets = 0
        while wickets != total_wickets:
            choice = int(input('Enter number from 0 to 10- '))
            if choice == 0:
                ai_choice = random.randint(0,choice+2)
            if choice == 1:
                ai_choice = random.randint(0,choice+2)
            else:
                ai_choice = random.randint(choice-2,choice+2)    
                
            if choice == ai_choice:
                wickets = wickets + 1
            else:
                runs = runs + choice
            print(runs," - ",wickets)
        print("All out, now time to field!")
        target = runs  
        ai_runs = 0
        ai_wickets = 0
        while ai_runs < target or ai_wickets != total_wickets:
            choice = int(input('Enter number from 0 to 10- '))
            if choice == 0:
                ai_choice = random.randint(0,choice+2)
            if choice == 1:
                ai_choice = random.randint(0,choice+2)
            else:
                ai_choice = random.randint(choice-2,choice+2)
                
            if ai_choice == choice:
                ai_wickets = ai_wickets + 1
            else:
                ai_runs = ai_runs + ai_choice
            print(ai_runs," - ",ai_wickets)
            
    elif Choice == "Field" or Choice == "field":
        ai_runs = 0
        ai_wickets = 0
        while ai_wickets != total_wickets:
            choice = int(input('Enter number from 0 to 10- '))
            if choice == 0:
                ai_choice = random.randint(0,choice+2)
            if choice == 1:
                ai_choice = random.randint(0,choice+2)
            else:
                ai_choice = random.randint(choice-2,choice+2)
                
            if ai_choice == choice:
                ai_wickets = ai_wickets + 1
            else:
                ai_runs = ai_runs + ai_choice
            print(ai_runs," - ",ai_wickets)
        print("All out good job now time to bat!")
        target = ai_runs    
        runs = 0
        wickets = 0
        while wickets != total_wickets or runs < target:
            choice = int(input('Enter number from 0 to 10- '))
            if choice == 0:
                ai_choice = random.randint(0,choice+2)
            if choice == 1:
                ai_choice = random.randint(0,choice+2)
            else:
                ai_choice = random.randint(choice-2,choice+2)
                
            if choice == ai_choice:
                wickets = wickets + 1
            else:
                runs = runs + choice
            print(runs," - ",wickets)
        
elif Level == "Hard" or Level == "hard":
    Choice = input("You choose to Bat or Field- ")
    total_wickets = int(input("Enter total wickets- "))
    if Choice == "Bat" or Choice == "bat":
        runs = 0
        wickets = 0
        while wickets != total_wickets:
            choice = int(input('Enter number from 0 to 10- '))
            if choice == 0:
                ai_choice = random.randint(0,choice+1)
            if choice == 1:
                ai_choice = random.randint(0,choice+1)
            else:
                ai_choice = random.randint(choice-1,choice+1)    
                
            if choice == ai_choice:
                wickets = wickets + 1
            else:
                runs = runs + choice
            print(runs," - ",wickets)
        print("All out, now time to field!")
        target = runs  
        ai_runs = 0
        ai_wickets = 0
        while ai_wickets != total_wickets or ai_runs < target:
            choice = int(input('Enter number from 0 to 10- '))
            if choice == 0:
                ai_choice = random.randint(0,choice+1)
            if choice == 1:
                ai_choice = random.randint(0,choice+1)
            else:
                ai_choice = random.randint(choice-1,choice+1)
                
            if ai_choice == choice:
                ai_wickets = ai_wickets + 1
            else:
                ai_runs = ai_runs + ai_choice
            print(ai_runs," - ",ai_wickets)
        
    elif Choice == "Field" or Choice == "field":
        ai_runs = 0
        ai_wickets = 0
        while ai_wickets != total_wickets:
            choice = int(input('Enter number from 0 to 10- '))
            if choice == 0:
                ai_choice = random.randint(0,choice+1)
            if choice == 1:
                ai_choice = random.randint(0,choice+1)
            else:
                ai_choice = random.randint(choice-1,choice+1)
                
            if ai_choice == choice:
                ai_wickets = ai_wickets + 1
            else:
                ai_runs = ai_runs + ai_choice
            print(ai_runs," - ",ai_wickets)
        print("All out good job now time to bat!")    
        runs = 0
        wickets = 0
        while wickets != total_wickets or runs < target:
            choice = int(input('Enter number from 0 to 10- '))
            if choice == 0:
                ai_choice = random.randint(0,choice+1)
            if choice == 1:
                ai_choice = random.randint(0,choice+1)
            else:
                ai_choice = random.randint(choice-1,choice+1)
                
            if choice == ai_choice:
                wickets = wickets + 1
            else:
                runs = runs + choice
            print(runs," - ",wickets)
           
          
else:
    print("Invalid input")
      
if ai_runs > runs:
    print("AI won! Try again!")  
elif runs > ai_runs:
    print("You won! Great!")  
elif runs == ai_runs:
    print("Match Drawn!")                                  
              
                    

