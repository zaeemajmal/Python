l = [1,1,1,1,2,23,3,5]
l1 = [2,4,3,5,6,7,8,6]
def add(x,y):
    return x+y
def mul(x,y):
    return x*y
mapped = map(add,l,l1)
print(list(mapped))
mapped = map(mul,l,l1)
print(list(mapped))
