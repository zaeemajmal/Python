rows = int(input("Enter the number of rows- "))
n= 1
for i in range(rows):
    for j in range(i+1):
        print(n,end=" ")
        n+=1
    print("")    
        
