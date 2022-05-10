import random
print("Number Guessing GAme!!")
number = random.randint(0, 9)
chances = 0

print("Guess a number between 1 to 9")

while chances < 5:
    numberGuess = int(input("Enter your number:"))

    if numberGuess == number:
        print("Congratulations! You Won!!")
        break

    elif numberGuess < number:
        print("Your number was too low")

    elif numberGuess > number:
        print("Your number was too high")

    chances += 1

if not chances < 5:
    print("You lose, the number was ", number)
