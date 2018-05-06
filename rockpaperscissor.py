# rockpaperscissors.py (By: Tomás Antunes)

lang = input("Language(available languages: pt, en): ")

import time
import random

game_random = random.SystemRandom()

if lang == "en":
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
        # print(comp)
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
        # print(comp1)
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
            

    time.sleep(1)
                
    if human_score == 2:
        print("Human Won! Congrats! See you next time! :)")
        done = True
    elif comp_score == 2:
        done = True
        print("You lost! Next time will be better! See you next time! :)")
    else:
        done = False
        
elif lang == "pt":
    print("Bem-vindo ao Pedra Papel ou Tesoura! Divirta-se humano!")
    print("(Escolhas possíveis: pedra, papel, tesoura)")
    time.sleep(1)

    human_score = 0
    comp_score = 0

    playedFirst = False
    while not playedFirst:
        print("Primeira ronda")
        time.sleep(1)
        comp_choices = ["pedra", "papel", "tesoura"]
        comp = game_random.choice(comp_choices)
        # print(comp)
        human = input("Pedra Papel ou Tesoura: ")
        if human == "pedra" and comp == "tesoura":
            human_score = human_score + 1
            comp_score = comp_score + 0
            print("A Pedra destrói a Tesoura")
            time.sleep(1)
            print("Humano: " , human_score)
            print("Computador: " , comp_score)
            playedFirst = True
            time.sleep(1)
        elif human == "tesoura" and comp == "pedra":
            human_score = human_score + 0
            comp_score = comp_score + 1
            print("A Pedra destrói a Tesoura")
            time.sleep(1)
            print("Humano: " , human_score)
            print("Computador: " , comp_score)
            playedFirst = True
            time.sleep(1)
        elif human == "papel" and comp == "pedra":
            human_score = human_score + 1
            comp_score = comp_score + 0
            print("A Pedra fica coberta de Papel")
            time.sleep(1)
            print("Humano: " , human_score)
            print("Computador: " , comp_score)
            playedFirst = True
            time.sleep(1)
        elif human == "pedra" and comp == "papel":
            human_score = human_score + 0
            comp_score = comp_score + 1
            print("A Pedra fica coberta de Papel")
            time.sleep(1)
            print("Humano: " , human_score)
            print("Computador: " , comp_score)
            playedFirst = True
        elif human == "tesoura" and comp == "papel":
            human_score = human_score + 1
            comp_score = comp_score + 0
            print("A Tesoura corta o Papel")
            time.sleep(1)
            print("Humano: " , human_score)
            print("Computador: " , comp_score)
            playedFirst = True
            time.sleep(1)
        elif human == "papel" and comp == "tesoura":
            human_score = human_score + 0
            comp_score = comp_score + 1
            print("A Tesoura corta o Papel")
            time.sleep(1)
            print("Humano: " , human_score)
            print("Computador: " , comp_score)
            playedFirst = True
            time.sleep(1)
        elif human == "pedra" and comp == "pedra":
            human_score = human_score + 0
            comp_score = comp_score + 0
            print("Nada acontece.")
            time.sleep(1)
            print("Humano: " , human_score)
            print("Computador: " , comp_score)
            playedFirst = False
            time.sleep(1)
        elif human == "papel" and comp == "papel":
            human_score = human_score + 0
            comp_score = comp_score + 0
            print("Nada acontece.")
            time.sleep(1)
            print("Humano: " , human_score)
            print("Computador: " , comp_score)
            playedFirst = False
            time.sleep(1)
        elif human == "tesoura" and comp == "tesoura":
            human_score = human_score + 0
            comp_score = comp_score + 0
            print("Nada acontece.")
            time.sleep(1)
            print("Humano: " , human_score)
            print("Computador: " , comp_score)
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
        print("Segunda ronda")
        time.sleep(1)
        comp_choices1 = ["pedra", "papel", "tesoura"]
        comp1 = game_random.choice(comp_choices1)
        # print(comp1)
        human = input("Pedra Papel ou Tesoura: ")
        if human == "pedra" and comp1 == "tesoura":
            human_score = human_score + 1
            comp_score = comp_score + 0
            print("A Pedra destrói a Tesoura")
            time.sleep(1)
            print("Humano: " , human_score)
            print("Computador: " , comp_score)
            playedSecond = True
            time.sleep(1)
        elif human == "tesoura" and comp1 == "pedra":
            human_score = human_score + 0
            comp_score = comp_score + 1
            print("A Pedra destrói a Tesoura")
            time.sleep(1)
            print("Humano: " , human_score)
            print("Computador: " , comp_score)
            playedSecond = True
            time.sleep(1)
        elif human == "papel" and comp1 == "pedra":
            human_score = human_score + 1
            comp_score = comp_score + 0
            print("A Pedra fica coberta de Papel")
            time.sleep(1)
            print("Humano: " , human_score)
            print("Computador: " , comp_score)
            playedSecond = True
            time.sleep(1)
        elif human == "pedra" and comp1 == "papel":
            human_score = human_score + 0
            comp_score = comp_score + 1
            print("A Pedra fica coberta de Papel")
            time.sleep(1)
            print("Humano: " , human_score)
            print("Computador: " , comp_score)
            playedSecond = True
            time.sleep(1)
        elif human == "tesoura" and comp1 == "papel":
            human_score = human_score + 1
            comp_score = comp_score + 0
            print("A Tesoura corta o Papel")
            time.sleep(1)
            print("Humano: " , human_score)
            print("Computador: " , comp_score)
            playedSecond = True
            time.sleep(1)
        elif human == "papel" and comp1 == "tesoura":
            human_score = human_score + 0
            comp_score = comp_score + 1
            print("A Tesoura corta o Papel")
            time.sleep(1)
            print("Humano: " , human_score)
            print("Computador: " , comp_score)
            playedSecond = True
        elif human == "pedra" and comp1 == "pedra":
            human_score = human_score + 0
            comp_score = comp_score + 0
            print("Nada acontece.")
            time.sleep(1)
            print("Humano: " , human_score)
            print("Computador: " , comp_score)
            playedSecond = False
            time.sleep(1)
        elif human == "papel" and comp1 == "papel":
            human_score = human_score + 0
            comp_score = comp_score + 0
            print("Nada acontece.")
            time.sleep(1)
            print("Humano: " , human_score)
            print("Computador: " , comp_score)
            playedSecond = False
            time.sleep(1)
        elif human == "tesoura" and comp1 == "tesoura":
            human_score = human_score + 0
            comp_score = comp_score + 0
            print("Nada acontece.")
            time.sleep(1)
            print("Humano: " , human_score)
            print("Computador: " , comp_score)
            playedSecond = False
            time.sleep(1)
        elif human_score == 2 or comp_score == 2:
            break
        else:
            playedSecond = False
            time.sleep(1)
            

    time.sleep(1)
                
    if human_score == 2:
        print("O humano ganhou! Parabéns! Até à próxima! :)")
        done = True
    elif comp_score == 2:
        done = True
        print("Perdeste! Para a próxima fazes melhor! Até à próxima! :)")
    else:
        done = False
else:
    print("Error. That language is not available.")
