try:
    num = int(input("Enter a number of cricket team"))
    if num != 11:
        raise Exception("A cricket team should have 11 players")
    else:
        print("we are good")
except Exception as e:
    print(e)
            
        