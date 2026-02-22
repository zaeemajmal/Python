try:
    age = int(input("Enter your age- "))
    if  age % 2 == 0:
      print("The age is even")  
    else:
      print("The age is odd")
except ValueError as ex:
    print("Error-",ex)    
      

