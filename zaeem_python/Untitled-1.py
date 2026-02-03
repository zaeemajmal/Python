print("HI WELCOME TO THE CAFE.")
Name = input("What is your name?  ")
print("Welcome in " + Name)
print("Menu:\n" + "Cappuchino - $150\n" + "Black tea - $129\n" + "Green tea - 70\n" + "Coffee - $59\n" + "Cookies - $22\n" + "Tea - $10\n")


def Option_Select2():

    Order = input("What else do you want?  ")
    if Order == "Cappuchino" :
        print("Wait a minute. The order will come to you.")
        print("The order is $150")
        return 150
  
    elif Order == "Black tea" :
        print("Wait a minute. The order will come to you.")
        print("The order is $129")
        return 29

    elif Order == "Green tea" :
        print("Wait a minute. The order will come to you.")
        print("The order is $70")
        return 70 

    elif Order == "Coffee" :
        print("Wait a minute. The order will come to you.")
        print("The order is $59")   
        return 59

    elif Order == "Cookies" :
        print("Wait a minute. The order will come to you.")
        print("The order is $22")
        return 22 

    elif Order == "Tea" :
        print("Wait a minute. The order will come to you.")
        print("The order is $10")
        return 10 

    else :
        print("Sorry I couldn't understand that. Could you repeat it.")
        return Option_Select2()
    





def Option_Select():

    Order = input("What do you want?  ")
    if Order == "Cappuchino" :
       print("Wait a minute. The order will come to you.")
       print("The order is $150")
       return 150

    elif Order == "Black tea" :
       print("Wait a minute. The order will come to you.")
       print("The order is $129")
       return 129

    elif Order == "Green tea" :
       print("Wait a minute. The order will come to you.")
       print("The order is $70")
       return 70

    elif Order == "Coffee" :
       print("Wait a minute. The order will come to you.")
       print("The order is $59")
       return 59   

    elif Order == "Cookies" :
       print("Wait a minute. The order will come to you.")
       print("The order is $22")
       return 22 

    elif Order == "Tea" :
       print("Wait a minute. The order will come to you.")
       print("The order is $10")
       return 10 

    else :
       print("Sorry I couldn't understand that. Could you repeat it.")
       return Option_Select()
    

question = input("Do you want anything? ") 
if question == "Yes" :
    A = Option_Select()
    B = Option_Select2()

else:
    A = 0
    B = 0

C = A + B

print("The total amount is $" + str(C))   



   



