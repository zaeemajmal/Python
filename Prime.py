lower = int(input("Input lower range- "))
upper = int(input("Input upper range- "))
for num in range(lower, upper + 1):
    for i in range(2,num):
      if num % i == 0:
        break
    else:
        print(num)
        


        