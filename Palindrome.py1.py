
def i(r):
    s = 0
    e = len(r)-1
    while s < e:
        if r[s] != r[e]:
          return False
        
        s+=1
        e-=1
    return True
t = (9,8,7,8,7)  
if (i(t)):
    print("It is a flip flop")
else:
    print("It is not a flip flop")    
    
    
    
       
        
    







    