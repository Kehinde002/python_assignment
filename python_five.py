import random

secret_number = random.randint(1, 100)
count = 0
guess = 0

while guess != secret_number:
    guess = int(input("Guess a number (1-100): "))
    count += 1

print(f"Finally got it right after {count} attempt")

