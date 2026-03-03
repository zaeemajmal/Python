n = int(input("Enter a number of subjects- "))
sum = 0
list = []
for i in range(n):
    s = int(input("Enter marks- "))
    list.append(s)
for j in list:
    sum  = sum + j 
a = sum/n    
print(round(a,5))     