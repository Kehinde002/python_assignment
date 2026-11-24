word = input("Enter a word: ")

for letter in word:
    if letter == ' ':
        print()
    else:
        print(letter, end="")

