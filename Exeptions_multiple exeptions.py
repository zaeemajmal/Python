try:
   if 0 == 0:
    num = int(input("Enter a number- "))
    num1 = int(input("Enter a number- "))
    print(result = num / num1)
except ValueError as ex:
    print("Exception", ex)
except IndentationError as ex:
    print("Exeption", ex, " please check your indentation")
finally:
    print("Done")
    


