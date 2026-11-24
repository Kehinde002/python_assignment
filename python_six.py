word = input("Enter a word: ")

for character in range(0, len(word), 2):
    print(word[character], end="")

