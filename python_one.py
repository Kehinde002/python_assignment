word = input("Enter a word: ")
reversed_word = ""

for character in word:
    reversed_word = character + reversed_word

if reversed_word == word:
    print("its a palindrome")
else:
    print(" its not a palindrome")

