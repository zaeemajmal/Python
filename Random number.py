import random
i = 1
n = random.randint(1,10)
while i == 1:
    num = int(input('Guess the number between 1 to 10- ')) 
    if n == num:
        i = 0
    else:
        print("Guess again!")
print("You win!")    