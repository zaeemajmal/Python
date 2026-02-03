num = int(input("Enter Number- "))
sum_digits= 0
temp= num

while temp > 0:
    digits= temp% 10
    sum_digits+=digits
    temp//= 10
print(sum_digits)    


    