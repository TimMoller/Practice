# this is a guess the number Game:
import random
secretNumber = random.randint(1, 20)
print("I'm thinking of a number between 1 and 20")

# ask the player to guess 6 times
for guessesTaken in range(1, 7):
    print("take a guess:")
    guess = int(input())

    if guess < secretNumber:
        print("Too low, guess again.")
    elif guess > secretNumber:
        print("Too high, guess again.")
    else:
        break   #This condition is the correct guess

if guess == secretNumber:
    print("Congratulations you guessed the secret number in " + str(guessesTaken) + ' guesses!')
else:
    print("Eish, the number that i was thinking of was " + str(secretNumber))
