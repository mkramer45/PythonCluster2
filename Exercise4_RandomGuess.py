import random

randomNumber = random.randint(1,9)

guessedNumber = []

while True:
    userGuess = input("Guess the Number! ")
    guessedNumber.append(userGuess)

    if userGuess == "exit":
        del guessedNumber[-1]

        break
    elif int(userGuess) > randomNumber:
        print("Number is too high!")
    elif int(userGuess) < randomNumber:
        print("Number is too low! ")
    else:
        print("You guessed correct! ")
    break
