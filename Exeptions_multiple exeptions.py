try:
    num = int(input("Enter a number- "))
    num1 = int(input("Enter a number- "))
    print(result = num / num1)
except ValueError as ex:
    print("Exception", ex)
except ArithmeticError as ex:
    print("Exeption", ex)
finally:
    print("Done")
    


