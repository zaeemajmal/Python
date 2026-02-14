def cube(num):
    return num**3
def divisible(num):
    if num % 3 == 0:
        return cube(num)
    else:
        return False
Num =  int(input("Enter a value- "))  
print(divisible(Num))


