number = input("Enter a number- ")
i = len(str(number))-1
sum = 0
number = str(number)
while i >= 0:
    sum = sum + int(number[i])
    i = i - 1
print(sum)    