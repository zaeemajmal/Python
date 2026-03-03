n = int(input("Enter a number of string- "))
list = []
for i in range(n):
    s = input("Enter string-")
    list.append(s)
for f in list:
    if len(f) > 0 and f[0] == f[-1]:
        print(f)