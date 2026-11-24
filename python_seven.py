word = input("Enter a word: ")
reversed_word = ""

for character in word:
    reversed_word = character + reversed_word

print(reversed_word, end="")

