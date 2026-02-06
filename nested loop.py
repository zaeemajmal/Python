Word = input("Enter a word- ")
Character = input("Enter a character- ")
i = 0
count = 0
while i < len(Word):
    if Word[i] == Character:
        count+=1
    i+=1    
print("The number of occurances is ", Character,"is ",count)


Word = input("Enter a word- ")
Character = input("Enter a character- ")
count = 0
for i in Word:
    if i == Character:
        count+=1
        
print("The number of occurances is ", Character,"is ",count)
