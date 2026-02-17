string = input("Enter a string or number- ")
character = input("Enter what you want to find- ")
length = len(string)
length-=1
for i in string:
    if i == character:
        print("Character found")
        break
    else:
        pass

        