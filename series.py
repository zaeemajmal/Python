num = int(input("Enter a number- "))
sum = 1
n = 2
temp = num
for i in range(1,num+1):
    temp =  1 / n
    n = n + n
    sum = sum + temp
print(round(sum,5))    