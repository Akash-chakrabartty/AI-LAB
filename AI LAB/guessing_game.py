

import random

secret = random.randint(1, 100)
attempts = 0

print("I have chosen a number between 1 and 100.")
print("Try to guess it!")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print("🎉 Correct! The number was", secret)
        print("You guessed it in", attempts, "attempts.")
        break
