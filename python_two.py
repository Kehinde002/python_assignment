count = 0
total = 0

number = int(input("Enter a number: "))

while number != -1:
    count += 1
    total += number
    average = total / count
    print(average)
    number = int(input())

