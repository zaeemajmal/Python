phone_book = {}
name = ""

for i in range(int(input("Enter how many contacts you want to add- "))):
    name = input("Enter the contact name- ")
    phone_book[name] = int(input("Enter phone number- "))
for key, value in phone_book.items():
    print(f"{key}: {value}")
delete = input("Enter what contact you want to delete- ")    
del phone_book[delete]
if phone_book == {}:
    print("Phone book is empty")
else:
    print(phone_book)    