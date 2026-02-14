def circumfrence(r):
    C = 2 * (22/7) * r
    return C
  
def area(r):
    A = (22/7) * r * r
    return A


radius = float(input("Enter the radius- "))

C = circumfrence(radius)
A = area(radius)
print("The circumfrence of the circle is ", round(C,2))
print("The area of the circle is ", round(A,2))





  
