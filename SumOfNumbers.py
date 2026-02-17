# Using recursion find the sum of numbers till n
def Add(n):
  if n == 0:
    return 0
  else:
    return n + Add(n - 1)
   

upper_range = int(input("Enter a number- "))
output = Add(upper_range)

print(output)

