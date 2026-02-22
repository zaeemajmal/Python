num = int(input("Enter a number- "))
sum = 0
temp = num
for i in range(1,num+1):
    temp =  1 / i
    sum = sum + temp
print(round(sum,5))    

    

