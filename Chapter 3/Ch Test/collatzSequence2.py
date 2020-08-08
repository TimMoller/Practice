def collatz(number):
    if (number % 2) == 0:
        return (number // 2)
    else:
        return ((number * 3) + 1)

guess = int(input("Enter a number: "))

while True:
    try:
        if collatz(guess) != 1:
            print(collatz(guess))
            guess = int(input("Enter another number: "))
        else:
            break
    except ValueError:
        continue

print(collatz(guess))
