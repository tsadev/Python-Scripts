# rockpaperscissors.py (By: Tomás Antunes)

import time
import random

lang = input("Language(available languages: pt, en): ")

game_random = random.SystemRandom()

def rockpaperscissorEN():
    print("You are now playing Rock Paper Scissors! Have Fun!")
    print("(Possible choices: rock, paper, scissor)")
    time.sleep(1)

    human_score = 0
    comp_score = 0

    playedFirst = False
    while not playedFirst:
        print("First Round")
        time.sleep(1)
        comp_choices = ["rock", "paper", "scissor"]
        comp = game_random.choice(comp_choices)
        print(comp)
        human = input("Rock Paper or Scissor: ")
        if human == "rock" and comp == "scissor":
            human_score = human_score + 1
            comp_score = comp_score + 0
            print("Rock destroys scissor")
            time.sleep(1)
            print("Human: " , human_score)
            print("Computer: " , comp_score)
            playedFirst = True
            time.sleep(1)
        elif human == "scissor" and comp == "rock":
            human_score = human_score + 0
            comp_score = comp_score + 1
            print("Rock destroys scissor")
            time.sleep(1)
            print("Human: " , human_score)
            print("Computer: " , comp_score)
            playedFirst = True
            time.sleep(1)
        elif human == "paper" and comp == "rock":
            human_score = human_score + 1
            comp_score = comp_score + 0
            print("Rock gets covered with paper")
            time.sleep(1)
            print("Human: " , human_score)
            print("Computer: " , comp_score)
            playedFirst = True
            time.sleep(1)
        elif human == "rock" and comp == "paper":
            human_score = human_score + 0
            comp_score = comp_score + 1
            print("Rock gets covered with paper")
            time.sleep(1)
            print("Human: " , human_score)
            print("Computer: " , comp_score)
            playedFirst = True
        elif human == "scissor" and comp == "paper":
            human_score = human_score + 1
            comp_score = comp_score + 0
            print("Scissor cuts paper")
            time.sleep(1)
            print("Human: " , human_score)
            print("Computer: " , comp_score)
            playedFirst = True
            time.sleep(1)
        elif human == "paper" and comp == "scissor":
            human_score = human_score + 0
            comp_score = comp_score + 1
            print("Scissor cuts paper")
            time.sleep(1)
            print("Human: " , human_score)
            print("Computer: " , comp_score)
            playedFirst = True
            time.sleep(1)
        elif human == "rock" and comp == "rock":
            human_score = human_score + 0
            comp_score = comp_score + 0
            print("Nothing happens")
            time.sleep(1)
            print("Human: " , human_score)
            print("Computer: " , comp_score)
            playedFirst = False
            time.sleep(1)
        elif human == "paper" and comp == "paper":
            human_score = human_score + 0
            comp_score = comp_score + 0
            print("Nothing happens")
            time.sleep(1)
            print("Human: " , human_score)
            print("Computer: " , comp_score)
            playedFirst = False
            time.sleep(1)
        elif human == "scissor" and comp == "scissor":
            human_score = human_score + 0
            comp_score = comp_score + 0
            print("Nothing happens")
            time.sleep(1)
            print("Human: " , human_score)
            print("Computer: " , comp_score)
            playedFirst = False
            time.sleep(1)
        elif human_score == 2 or comp_score == 2:
            break
        else:
            playedFirst = False
            time.sleep(1)

    time.sleep(2)

    playedSecond = False
    while not playedSecond:
        print("Second round")
        time.sleep(1)
        comp_choices1 = ["rock", "paper", "scissor"]
        comp1 = game_random.choice(comp_choices1)
        print(comp1)
        human = input("Rock Paper or Scissor: ")
        if human == "rock" and comp1 == "scissor":
            human_score = human_score + 1
            comp_score = comp_score + 0
            print("Rock destroys scissor")
            time.sleep(1)
            print("Human: " , human_score)
            print("Computer: " , comp_score)
            playedSecond = True
            time.sleep(1)
        elif human == "scissor" and comp1 == "rock":
            human_score = human_score + 0
            comp_score = comp_score + 1
            print("Rock destroys scissor")
            time.sleep(1)
            print("Human: " , human_score)
            print("Computer: " , comp_score)
            playedSecond = True
            time.sleep(1)
        elif human == "paper" and comp1 == "rock":
            human_score = human_score + 1
            comp_score = comp_score + 0
            print("Rock gets covered with paper")
            time.sleep(1)
            print("Human: " , human_score)
            print("Computer: " , comp_score)
            playedSecond = True
            time.sleep(1)
        elif human == "rock" and comp1 == "paper":
            human_score = human_score + 0
            comp_score = comp_score + 1
            print("Rock gets covered with paper")
            time.sleep(1)
            print("Human: " , human_score)
            print("Computer: " , comp_score)
            playedSecond = True
            time.sleep(1)
        elif human == "scissor" and comp1 == "paper":
            human_score = human_score + 1
            comp_score = comp_score + 0
            print("Scissor cuts paper")
            time.sleep(1)
            print("Human: " , human_score)
            print("Computer: " , comp_score)
            playedSecond = True
            time.sleep(1)
        elif human == "paper" and comp1 == "scissor":
            human_score = human_score + 0
            comp_score = comp_score + 1
            print("Scissor cuts paper")
            time.sleep(1)
            print("Human: " , human_score)
            print("Computer: " , comp_score)
            playedSecond = True
        elif human == "rock" and comp1 == "rock":
            human_score = human_score + 0
            comp_score = comp_score + 0
            print("Nothing happens")
            time.sleep(1)
            print("Human: " , human_score)
            print("Computer: " , comp_score)
            playedSecond = False
            time.sleep(1)
        elif human == "paper" and comp1 == "paper":
            human_score = human_score + 0
            comp_score = comp_score + 0
            print("Nothing happens")
            time.sleep(1)
            print("Human: " , human_score)
            print("Computer: " , comp_score)
            playedSecond = False
            time.sleep(1)
        elif human == "scissor" and comp1 == "scissor":
            human_score = human_score + 0
            comp_score = comp_score + 0
            print("Nothing happens")
            time.sleep(1)
            print("Human: " , human_score)
            print("Computer: " , comp_score)
            playedSecond = False
            time.sleep(1)
        elif human_score == 2 or comp_score == 2:
            break
        else:
            playedSecond = False
            time.sleep(1)

    if human_score != 2 or comp_score != 2:
        playedExtraOne = False
        while not playedExtraOne:
            print("Third round")
            time.sleep(1)
            comp_choices1 = ["rock", "paper", "scissor"]
            comp1 = game_random.choice(comp_choices1)
            print(comp1)
            human = input("Rock Paper or Scissor: ")
            if human == "rock" and comp1 == "scissor":
                human_score = human_score + 1
                comp_score = comp_score + 0
                print("Rock destroys scissor")
                time.sleep(1)
                print("Human: " , human_score)
                print("Computer: " , comp_score)
                playedExtraOne = True
                time.sleep(1)
            elif human == "scissor" and comp1 == "rock":
                human_score = human_score + 0
                comp_score = comp_score + 1
                print("Rock destroys scissor")
                time.sleep(1)
                print("Human: " , human_score)
                print("Computer: " , comp_score)
                playedExtraOne = True
                time.sleep(1)
            elif human == "paper" and comp1 == "rock":
                human_score = human_score + 1
                comp_score = comp_score + 0
                print("Rock gets covered with paper")
                time.sleep(1)
                print("Human: " , human_score)
                print("Computer: " , comp_score)
                playedExtraOne = True
                time.sleep(1)
            elif human == "rock" and comp1 == "paper":
                human_score = human_score + 0
                comp_score = comp_score + 1
                print("Rock gets covered with paper")
                time.sleep(1)
                print("Human: " , human_score)
                print("Computer: " , comp_score)
                playedExtraOne = True
                time.sleep(1)
            elif human == "scissor" and comp1 == "paper":
                human_score = human_score + 1
                comp_score = comp_score + 0
                print("Scissor cuts paper")
                time.sleep(1)
                print("Human: " , human_score)
                print("Computer: " , comp_score)
                playedExtraOne = True
                time.sleep(1)
            elif human == "paper" and comp1 == "scissor":
                human_score = human_score + 0
                comp_score = comp_score + 1
                print("Scissor cuts paper")
                time.sleep(1)
                print("Human: " , human_score)
                print("Computer: " , comp_score)
                playedExtraOne = True
            elif human == "rock" and comp1 == "rock":
                human_score = human_score + 0
                comp_score = comp_score + 0
                print("Nothing happens")
                time.sleep(1)
                print("Human: " , human_score)
                print("Computer: " , comp_score)
                playedExtraOne = False
                time.sleep(1)
            elif human == "paper" and comp1 == "paper":
                human_score = human_score + 0
                comp_score = comp_score + 0
                print("Nothing happens")
                time.sleep(1)
                print("Human: " , human_score)
                print("Computer: " , comp_score)
                playedExtraOne = False
                time.sleep(1)
            elif human == "scissor" and comp1 == "scissor":
                human_score = human_score + 0
                comp_score = comp_score + 0
                print("Nothing happens")
                time.sleep(1)
                print("Human: " , human_score)
                print("Computer: " , comp_score)
                playedExtraOne = False
                time.sleep(1)
            elif human_score == 2 or comp_score == 2:
                break
            else:
                playedExtraOne = False
                time.sleep(1)

            

    time.sleep(1)
                
    if human_score == 2:
        print("Human Won! Congrats! See you next time! :)")
    elif comp_score == 2:
        print("You lost! Next time will be better! See you next time! :)")
   
def rockpaperscissorPT():
    print("Bem-vindo ao Pedra Papel ou Tesoura! Divirta-se humano!")
    print("(Escolhas possíveis: pedra, papel, tesoura)")
    time.sleep(1)

    human_scorez = 0
    comp_scorez = 0

    playedThird = False
    while not playedThird:
        print("Primeira ronda")
        time.sleep(1)
        comp_choices2 = ["pedra", "papel", "tesoura"]
        comp2 = game_random.choice(comp_choices2)
        print(comp2)
        human = input("Pedra Papel ou Tesoura: ")
        if human == "pedra" and comp2 == "tesoura":
            human_scorez = human_scorez + 1
            comp_scorez = comp_scorez + 0
            print("A Pedra destrói a Tesoura")
            time.sleep(1)
            print("Humano: " , human_scorez)
            print("Computador: " , comp_scorez)
            playedThird = True
            time.sleep(1)
        elif human == "tesoura" and comp2 == "pedra":
            human_scorez = human_scorez + 0
            comp_scorez = comp_scorez + 1
            print("A Pedra destrói a Tesoura")
            time.sleep(1)
            print("Humano: " , human_scorez)
            print("Computador: " , comp_scorez)
            playedThird = True
            time.sleep(1)
        elif human == "papel" and comp2 == "pedra":
            human_scorez = human_scorez + 1
            comp_scorez = comp_scorez + 0
            print("A Pedra fica coberta de Papel")
            time.sleep(1)
            print("Humano: " , human_scorez)
            print("Computador: " , comp_scorez)
            playedThird = True
            time.sleep(1)
        elif human == "pedra" and comp2 == "papel":
            human_scorez = human_scorez + 0
            comp_scorez = comp_scorez + 1
            print("A Pedra fica coberta de Papel")
            time.sleep(1)
            print("Humano: " , human_scorez)
            print("Computador: " , comp_scorez)
            playedThird = True
        elif human == "tesoura" and comp2 == "papel":
            human_scorez = human_scorez + 1
            comp_scorez = comp_scorez + 0
            print("A Tesoura corta o Papel")
            time.sleep(1)
            print("Humano: " , human_scorez)
            print("Computador: " , comp_scorez)
            playedThird = True
            time.sleep(1)
        elif human == "papel" and comp2 == "tesoura":
            human_scorez = human_scorez + 0
            comp_scorez= comp_scorez + 1
            print("A Tesoura corta o Papel")
            time.sleep(1)
            print("Humano: " , human_scorez)
            print("Computador: " , comp_scorez)
            playedThird = True
            time.sleep(1)
        elif human == "pedra" and comp2 == "pedra":
            human_scorez = human_scorez + 0
            comp_scorez = comp_scorez + 0
            print("Nada acontece.")
            time.sleep(1)
            print("Humano: " , human_scorez)
            print("Computador: " , comp_scorez)
            playedThird = False
            time.sleep(1)
        elif human == "papel" and comp2 == "papel":
            human_scorez = human_scorez + 0
            comp_scorez = comp_scorez + 0
            print("Nada acontece.")
            time.sleep(1)
            print("Humano: " , human_scorez)
            print("Computador: " , comp_scorez)
            playedThird = False
            time.sleep(1)
        elif human == "tesoura" and comp2 == "tesoura":
            human_scorez = human_scorez + 0
            comp_scorez = comp_scorez + 0
            print("Nada acontece.")
            time.sleep(1)
            print("Humano: " , human_scorez)
            print("Computador: " , comp_scorez)
            playedThird = False
            time.sleep(1)
        elif human_scorez == 2 or comp_scorez == 2:
            break
        else:
            playedThird = False
            time.sleep(1)

    time.sleep(2)

    playedFourth = False
    while not playedFourth:
        print("Segunda ronda")
        time.sleep(1)
        comp_choices3 = ["pedra", "papel", "tesoura"]
        comp3 = game_random.choice(comp_choices3)
        print(comp3)
        human = input("Pedra Papel ou Tesoura: ")
        if human == "pedra" and comp3 == "tesoura":
            human_scorez = human_scorez + 1
            comp_scorez = comp_scorez + 0
            print("A Pedra destrói a Tesoura")
            time.sleep(1)
            print("Humano: " , human_scorez)
            print("Computador: " , comp_scorez)
            playedFourth = True
            time.sleep(1)
        elif human == "tesoura" and comp3 == "pedra":
            human_scorez = human_scorez + 0
            comp_scorez = comp_scorez + 1
            print("A Pedra destrói a Tesoura")
            time.sleep(1)
            print("Humano: " , human_scorez)
            print("Computador: " , comp_scorez)
            playedFourth = True
            time.sleep(1)
        elif human == "papel" and comp3 == "pedra":
            human_scorez = human_scorez + 1
            comp_scorez = comp_scorez + 0
            print("A Pedra fica coberta de Papel")
            time.sleep(1)
            print("Humano: " , human_scorez)
            print("Computador: " , comp_scorez)
            playedFourth = True
            time.sleep(1)
        elif human == "pedra" and comp3 == "papel":
            human_scorez = human_scorez + 0
            comp_scorez = comp_scorez + 1
            print("A Pedra fica coberta de Papel")
            time.sleep(1)
            print("Humano: " , human_scorez)
            print("Computador: " , comp_scorez)
            playedFourth = True
            time.sleep(1)
        elif human == "tesoura" and comp3 == "papel":
            human_scorez = human_scorez + 1
            comp_scorez = comp_scorez + 0
            print("A Tesoura corta o Papel")
            time.sleep(1)
            print("Humano: " , human_scorez)
            print("Computador: " , comp_scorez)
            playedFourth = True
            time.sleep(1)
        elif human == "papel" and comp3 == "tesoura":
            human_scorez = human_scorez + 0
            comp_scorez = comp_scorez + 1
            print("A Tesoura corta o Papel")
            time.sleep(1)
            print("Humano: " , human_scorez)
            print("Computador: " , comp_scorez)
            playedFourth = True
        elif human == "pedra" and comp3 == "pedra":
            human_scorez = human_scorez + 0
            comp_scorez = comp_scorez + 0
            print("Nada acontece.")
            time.sleep(1)
            print("Humano: " , human_scorez)
            print("Computador: " , comp_scorez)
            playedFourth = False
            time.sleep(1)
        elif human == "papel" and comp3 == "papel":
            human_scorez = human_scorez + 0
            comp_scorez = comp_scorez + 0
            print("Nada acontece.")
            time.sleep(1)
            print("Humano: " , human_scorez)
            print("Computador: " , comp_scorez)
            playedFourth = False
            time.sleep(1)
        elif human == "tesoura" and comp3 == "tesoura":
            human_scorez = human_scorez + 0
            comp_scorez = comp_scorez + 0
            print("Nada acontece.")
            time.sleep(1)
            print("Humano: " , human_scorez)
            print("Computador: " , comp_scorez)
            playedFourth = False
            time.sleep(1)
        elif human_scorez == 2 or comp_scorez == 2:
            break
        else:
            playedFourth = False
            time.sleep(1)
    
    playedExtraTwo = False
    if human_scorez != 2 or comp_scorez != 2:
        while not playedExtraTwo:
            print("Terceira ronda")
            time.sleep(1)
            comp_choices4 = ["pedra", "papel", "tesoura"]
            comp4 = game_random.choice(comp_choices4)
            print(comp4)
            human = input("Pedra Papel ou Tesoura: ")
            if human == "pedra" and comp4 == "tesoura":
                human_scorez = human_scorez + 1
                comp_scorez = comp_scorez + 0
                print("A Pedra destrói a Tesoura")
                time.sleep(1)
                print("Humano: " , human_scorez)
                print("Computador: " , comp_scorez)
                playedExtraTwo = True
                time.sleep(1)
            elif human == "tesoura" and comp4 == "pedra":
                human_scorez = human_scorez + 0
                comp_scorez = comp_scorez + 1
                print("A Pedra destrói a Tesoura")
                time.sleep(1)
                print("Humano: " , human_scorez)
                print("Computador: " , comp_scorez)
                playedExtraTwo = True
                time.sleep(1)
            elif human == "papel" and comp4 == "pedra":
                human_scorez = human_scorez + 1
                comp_scorez = comp_scorez + 0
                print("A Pedra fica coberta de Papel")
                time.sleep(1)
                print("Humano: " , human_scorez)
                print("Computador: " , comp_scorez)
                playedExtraTwo = True
                time.sleep(1)
            elif human == "pedra" and comp4 == "papel":
                human_scorez = human_scorez + 0
                comp_scorez = comp_scorez + 1
                print("A Pedra fica coberta de Papel")
                time.sleep(1)
                print("Humano: " , human_scorez)
                print("Computador: " , comp_scorez)
                playedExtraTwo = True
                time.sleep(1)
            elif human == "tesoura" and comp4 == "papel":
                human_scorez = human_scorez + 1
                comp_scorez = comp_scorez + 0
                print("A Tesoura corta o Papel")
                time.sleep(1)
                print("Humano: " , human_scorez)
                print("Computador: " , comp_scorez)
                playedExtraTwo = True
                time.sleep(1)
            elif human == "papel" and comp4 == "tesoura":
                human_scorez = human_scorez + 0
                comp_scorez = comp_scorez + 1
                print("A Tesoura corta o Papel")
                time.sleep(1)
                print("Humano: " , human_scorez)
                print("Computador: " , comp_scorez)
                playedExtraTwo = True
            elif human == "pedra" and comp4 == "pedra":
                human_scorez = human_scorez + 0
                comp_scorez = comp_scorez + 0
                print("Nada acontece.")
                time.sleep(1)
                print("Humano: " , human_scorez)
                print("Computador: " , comp_scorez)
                playedExtraTwo = False
                time.sleep(1)
            elif human == "papel" and comp4 == "papel":
                human_scorez = human_scorez + 0
                comp_scorez = comp_scorez + 0
                print("Nada acontece.")
                time.sleep(1)
                print("Humano: " , human_scorez)
                print("Computador: " , comp_scorez)
                playedExtraTwo = False
                time.sleep(1)
            elif human == "tesoura" and comp4 == "tesoura":
                human_scorez = human_scorez + 0
                comp_scorez = comp_scorez + 0
                print("Nada acontece.")
                time.sleep(1)
                print("Humano: " , human_scorez)
                print("Computador: " , comp_scorez)
                playedExtraTwo = False
                time.sleep(1)
            elif human_scorez == 2 or comp_scorez == 2:
                break
            else:
                playedExtraTwo = False
                time.sleep(1)


    time.sleep(1)
                
    if human_scorez == 2:
        print("O humano ganhou! Parabéns! Até à próxima! :)")
    elif comp_scorez == 2:
        print("Perdeste! Para a próxima fazes melhor! Até à próxima! :)")

if lang == "pt":
    rockpaperscissorPT()
elif lang == "en":
    rockpaperscissorEN()
else:
    print("Error. That language is not available.")
