def collatz(y):
    try:
        if y % 2 == 0:
            print(int(y/2))
            return int(y/2)
        else:
            print(int(y*3+1))
            return int(y*3 +1)
    except ValueError:
        print('Error: Invalid Value, the program should take in integers.')

print('Please enter a number and the Collatz sequence will be printed')
guess = int(input())

while guess != 1:
    guess = collatz(guess)
