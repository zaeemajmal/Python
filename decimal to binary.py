num = int(input("Enter a number you want to convert from decimal to binary- "))
binary = ""
i = num
if num==0:
    binary = "0"
else:
    while i >= 1:
     reminder = i % 2     
     binary = str(reminder) + binary    
     i = i // 2    
print(binary)     
 