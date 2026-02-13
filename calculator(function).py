print("Addition(1)")
print("Subtraction(2)")
print("Multiplication(3)")
print("Division(4)")
operation = input("Enter the operation- ")
def Add(num1,num2):
    return num1 + num2
def Sub(num1,num2):
    return num1 - num2
def Multiply(num1,num2):
    return num1 * num2
def Divide(num1,num2):
    return num1 / num2
num1 = int(input("Enter number- "))
num2 = int(input("Enter number- "))
if operation == '1':
    print(Add(num1,num2))
elif operation == '2':
    print(Sub(num1,num2)) 
elif operation == '3':
    print(Multiply(num1,num2))
elif operation == '4':
    print(Divide(num1,num2))   
else:
    print("Invalid")     
        
