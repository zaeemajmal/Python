import random
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
Password = ""
n  = int(input("Enter the number of charachters- "))
for i in range(n):
    Password = Password + random.choice(char)
print("The Password is-",Password)