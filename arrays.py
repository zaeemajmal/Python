import array as a
a = a.array("i",[1,2,3,4,5,6,66,7,76,6])
print(a)
for i in range(9,-1,-1):
    print(a[i])
a.reverse()
print(a)
print(a.count(6))