Bill = 0

def total_calc(bill):
    if Bill <= 100:
      total = bill + (bill/5)
    elif Bill <=  200:
       total = bill + (bill/10)
    elif Bill <=  500:
       total = bill + (bill/25)   
    elif Bill <=  1000:
       total = bill + (bill/30)  
    else:
         total =  total = bill + (bill/40) 
    print("Total- ",Bill)
    print("Grand Total- ",round(total, 2))  
Bill = int(input("Enter your bill's amount- ")) 
total_calc(Bill)