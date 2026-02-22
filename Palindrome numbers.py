num = str(input("Enter a number- "))
temp = ""
num_temp = 0

while num_temp <= int(num):
   for a in range(len(str(num_temp))-1,-1,-1):
        temp = temp + num[a]
   num_temp+=1     
  
   if temp == num:
      print(temp)
   else:
      pass      
   
    