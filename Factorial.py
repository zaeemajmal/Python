def Factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * Factorial(x-1)
num = int(input("Enter num- "))   
print(Factorial(num)) 
