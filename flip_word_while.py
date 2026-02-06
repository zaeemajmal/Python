word = input("Enter a word: ")
flipped = ""
length = len(word) - 1

while length >= 0:
    flipped = flipped + word[length]
    length = length -1
print("Flipped word:", flipped)