N = int(input("Enter number- "))
i = 1
sum = 0
while i <= N:
    sum = sum+i
    i = i+1
    print(sum)


#same with for    

N = int(input("Enter number- "))
sum = 0
for i in range(1,N+1):
   sum = sum+i
   print(sum)