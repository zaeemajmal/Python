Number1 = float(input("Enter a number: "))
Number2 = float(input("Enter a number: "))

Operation = input(" What Calculation do you want to perform (Add, Subtract, Multiply or Divide): ")

if Operation == "Add" or Operation == "add":
    Result = Number1 + Number2

elif Operation == "Subtract" or Operation == "subtract":
    Result = Number1 - Number2    

elif Operation == "Multiply" or Operation == "multiply":
    Result = Number1 * Number2

elif Operation == "Divide" or Operation == "divide":
    Result = Number1 / Number2    

else:
    print("Error")
    quit()

print("The Answer is " + str(Result))    