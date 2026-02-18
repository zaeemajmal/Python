string =  input("Enter a string- ")
for i in range(len(string)):
    if string[i] == "a" or string[i] == "A":
        break
    elif string[i] == "e" or string[i] == "E":
        break
    elif string[i] == "i" or string[i] == "I":
        break
    elif string[i] == "o" or string[i] == "O":
        break
    elif string[i] == "u" or string[i] == "U":
        break
    else:
        print(string[i], end="")


    
