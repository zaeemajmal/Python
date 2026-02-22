num = str(input("Enter a number- "))
temp = ""
try:
    for i in range(len(num)-1,-1,-1):
      temp = temp + num[i]
except ValueError as ex:
   print("Error", ex)   
if temp == num:
   print("It is a palindrome number")
else:
   print("The number is not a palindrome number")         
    




