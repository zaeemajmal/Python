num = int(input("Enter the number- "))
last = int(input("Enter the number till which you need multiples of the number- "))
count = 0
for i in range(last+1):
    count = num * i
    print(num," X ",i," = ",count)

