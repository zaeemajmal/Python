import random
options = ["Rock","Paper","Scissors"]
print(options)
User_choice = input("Enter a choice- ")
Computer_choice = random.choice(options)
if Computer_choice == User_choice:
    print("It is a draw")
elif Computer_choice == "Rock" and User_choice == "Paper":
    print("You win!!") 
elif Computer_choice == "Paper" and User_choice == "Scissors":
    print("You win!!")     
elif Computer_choice == "Scissors" and User_choice == "Rock":
    print("You win!!") 
elif Computer_choice == "Rock" and User_choice == "Scissors":
    print("You lost!") 
elif Computer_choice == "Paper" and User_choice == "Rock":
    print("You lost!")     
elif Computer_choice == "Scissors" and User_choice == "Paper":
    print("You lost!") 
else:
    print("Invalid Input")  
print("The computer choice was",Computer_choice)      