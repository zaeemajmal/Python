Lower_range = int(input("Enter the lower range- "))
Upper_range = int(input("Enter the upper range- "))
temp = Lower_range
num = 0
print(" The Even numbers in the range are- ", end=" ")
for i in range(Lower_range, Upper_range + 1):
    num = temp % 2
    if num == 0:
        print(temp, end="  ")
    temp+=1
print("\n The Odd numbers in the range are- ", end=" ") 
temp = Lower_range   
for a in range(Lower_range, Upper_range + 1):
    num = temp % 2
    if num != 0:
        print(temp, end="  ")
    temp+=1    
    

    
