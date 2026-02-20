v = False 
num1 = 0
while not v:
    try:
     num = int(input("Enter num- "))
     
     while num % 2 == 0:
        num1 = num1 + 1
        print("Bye" , num1)
        v = True
    except ValueError as ex:
       print("Error", ex)       
        