# guessthenumber.py (By: Tomás Antunes)

#concepts: Random, Integer (int), print, while loops, string (str)

import random

def main():
    print("Guess a number between 1 and 100.")
    randomNumber = random.randint(1, 100) #escolhe um numero aleatorio de 1 a 100
    found = False  # variavel para saber se o utilizador acertou ou nao

    while not found:
        userGuess = int(input("Your Guess: "))
        if userGuess == randomNumber:
            print("Nice you have passed to level 2!")
            found = True
        elif userGuess > randomNumber:
            print("Guess Lower!")
        else:
            print("Guess Higher!")

    print("Guess a number between 1 and 500.")
    randomness = random.randint(1, 500) # escolhe um numero aleatorio de 1 a 500
    found = False

    while not found:
        userGuessTwo = int(input("Your Guess: "))
        if userGuessTwo == randomness:
            print("Nice you have passed to level 3!")
            found = True
        elif userGuessTwo > randomness:
            print("Guess Lower!")
        else:
            print("Guess Higher!")

    print("Guess a number between 1 and 1000.")
    stupid = random.randint(1, 1000)
    found = False
    print("This one is harder so I will give you a hint! ;)")

    while not found:
        print(stupid - 11)
        userGuessThree = int(input("Your Guess: "))
        if userGuessThree == stupid:
            print("Nice! Thanks for playing my game!")
            found = True
        elif userGuessThree > stupid:
            print("Guess Lower!")
        else:
            print("Guess Higher!")







if __name__ == "__main__":
    main()
