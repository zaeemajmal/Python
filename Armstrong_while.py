num = int(input("Enter a number to check if it is an amstrong number- "))
sum=0
length = len(str(num))
i = 0
digit = 0
temp = num
while i < length:
    digit = temp%10
    sum+=digit**length
    temp//= 10
    i +=1
if sum == num:
    print(num," is an Armstrong number") 
else:
    print(num," is not an Armstrong number")       

    
    


