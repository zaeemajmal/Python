dict = {"Name": "Zaeem","Age": 11,"Class": 5}
dict["Gender"] = "Male"
print(dict.popitem())
print(dict)
for k,v in dict.items():
    print(k,":",v)
print(dict["Age"])    