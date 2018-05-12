# millionare.py (By: Tomás A.)

# This game has a total of 8 questions, with multiple answers (more to come)

import time
import random
from random import randint

playerBank = 0

print("Who wants to be a super millionare?")

myName = input("What's your name little man? ")

print("Welcome to the show, ", myName, "!")
print("The first prize, for a correct answer is $1,000 and it goes all the way up till $10,000,000! Shall we start?")

time.sleep(1)

num = input("Choose a number beteween 1 and 2: ")

# first question
if num == "1":
    print("The first question, for $1000, will be...")
    time.sleep(random.randint(1,2))
    print("Which of these former U.S. Presidents appeared on the television series Laugh-In?")
    print("Possible answers: a) Lyndon Johnson; b) Richard Nixon; c) Jimmy Carter; d) Gerald Ford")
    firstAnswer = input("Your choice: ")
    print("Your choice is...")
    time.sleep(random.randint(1,4))
    if firstAnswer == "b":
        print("Cooooorect! You jsut maid $1.000!")
        playerBank = playerBank + 1000
        print(myName, "bank: $", playerBank)
    else:
        print("Your answer is wrong! You will do better next time! See you!")
elif num == "2":
    print("The first question, for $1000, will be...")
    time.sleep(random.randint(1,2))
    print("What letter must appear at the beginning of the registration number of all non-military aircraft in the U.S.?")
    print("Possible answers: a) N; b) A; c) U; d) L")
    firstAnswer = input("Your choice: ")
    print("Your choice is...")
    time.sleep(random.randint(1,4))
    if firstAnswer == "a":
        print("Cooooorect! You jsut maid $1.000!")
        playerBank = playerBank + 1000
        print(myName, "bank: $", playerBank)
    else:
        print("Your answer is wrong! You will do better next time! See you!")


time.sleep(random.randint(1,3))

# second question
if playerBank > 0 and num == "1":
    print("The sencond question, for $5000, will be...")
    time.sleep(random.randint(1,2))
    print("The Earth is approximately how many miles away from the Sun?")
    print("Possible answers: a) 9.3 million; b) 39 million; c) 93 million; d) 193 million")
    secondAnswer = input("Your choise: ")
    print("Your choice is...")
    time.sleep(random.randint(1,4))
    if secondAnswer == "c":
        print("Cooooorect! You jsut maid $5.000!")
        playerBank = playerBank + 5000
        print(myName, "bank: $", playerBank)
    else:
        print("Your answer is wrong! You will do better next time! See you!")
elif playerBank > 0 and num == "2":
    print("The sencond question, for $5000, will be...")
    time.sleep(random.randint(1,2))
    print("In the children's book series, where is Paddington Bear originally from?")
    print("Possible answers: a) India; b) Peru; c) Canada; d) Iceland")
    secondAnswer = input("Your choise: ")
    print("Your choice is...")
    time.sleep(random.randint(1,4))
    if secondAnswer == "b":
        print("Cooooorect! You jsut maid $5.000!")
        playerBank = playerBank + 5000
        print(myName, "bank: $", playerBank)
    else:
        print("Your answer is wrong! You will do better next time! See you!")

time.sleep(random.randint(1,3))

# third question
if playerBank > 1000 and num == "1":
    print("The third question, for $100.000, will be...")
    time.sleep(random.randint(1,2))
    print("Which insect shorted out an early supercomputer and inspired the term «computer bug»?")
    print("Posible answers: a) Moth; b) Roach; c) Fly; d) Japanese beetle")
    thirdAnswer = input("Your choice: ")
    print("Your choice is...")
    time.sleep(random.randint(1,4))
    if thirdAnswer == "a":
        print("Cooooorect! You jsut maid $100000!")
        playerBank = playerBank + 100000
        print(myName, "bank: $", playerBank)
    else:
        print("Your answer is wrong! You will do better next time! See you!")
elif playerBank > 1000 and num == "2":
    print("The third question, for $100.000, will be...")
    time.sleep(random.randint(1,2))
    print("«Nephelococcygia» is the practice of doing what?")
    print("Posible answers: a) Finding shapes in clouds; b) Sleeping with your eyes open; c) Breaking glass with your voice; d) Swimming in freezing water")

time.sleep(random.randint(1,3))

# fourth question
if playerBank > 6000 and num == "1":
    print("The fourth question, for $10.000.000, will be...")
    time.sleep(random.randint(1,2))
    print("Which of the following landlocked countries is entirely contained within another country?")
    print("Posible answers: a) Lesotho; b) Burkina Faso; c) Mongolia; d) Luxembourg")
    fourthAnswer = input("Your choice: ")
    print("Your choice is...")
    time.sleep(random.randint(1,4))
    if fourthAnswer == "a":
        print("Cooooorect! You jsut maid $100000!")
        playerBank = playerBank + 10000000
        print(myName, "bank: $", playerBank)
    else:
        print("Your answer is wrong! You will do better next time! See you!")
elif playerBank > 6000 and num == "1":
    print("The fourth question, for $10.000.000, will be...")
    time.sleep(random.randint(1,2))
    print("The U.S. icon «Uncle Sam» was based on Samuel Wilson, who worked during the War of 1812 as a what?")
    print("Possible answers: a) Meat inspector; b) Mail delieverer; c) Historian; d) Weapons mechanic")
    fourthAnswer = input("Your choice: ")
    print("Your choice is...")
    time.sleep(random.randint(1,4))
    if fourthAnswer == "a":
        print("Cooooorect! You jsut maid $100000!")
        playerBank = playerBank + 10000000
        print(myName, "bank: $", playerBank)
    else:
        print("Your answer is wrong! You will do better next time! See you!")

time.sleep(random.randint(1,3))

# victory
if playerBank == 10106000:  # max on bank
    print("Congrats! You just won «Who wants to be a super millionare?» and you made $10.106.000! You are rich now! Have fun spending the money on things you don't need!")




