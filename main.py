import clearConsoleCMD  # Clear Console command
import playerCount  #Asks number of players
import animation  # Welcome to Louis' Poker House animation
import flop  # Flop program
import cardAssign  # assigns player cards
import os
import time as s
import pyautogui

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def ttnc():
    timer = 0
    while timer < 2:
        print(".")
        s.sleep(0.3)
        clearConsole()
        print("..")
        s.sleep(0.3)
        clearConsole()
        print("...")
        s.sleep(0.3)
        clearConsole()
        timer += 1


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


playerCount
clearConsoleCMD
animation
flop
cardAssign

ipbal = (playerCount.players).copy()
x = 0
cntr = 0
initBets = 0
round = 0
while x == 0:
    balWant = int(input("What balance would you like for each player?: "))
    for k in ipbal:
        ipbal[k] = balWant  # to replace values with balance
    clearConsole()
    while cntr < len(playerCount.players):
        for i in playerCount.players:
            print(f"{i}, your cards are: ")
            print(f"{bcolors.BOLD}{playerCount.players[i]}{bcolors.ENDC}")
            print(f"Your balance is: \n{bcolors.BOLD}{ipbal[i]}{bcolors.ENDC}")
            nextP = input("Next player? yes/no: ").lower
            if nextP == "no":
                x = 0
            else:
                ttnc()
                clearConsole()
                cntr = cntr + 1
                if cntr >= len(playerCount.players):
                    x = 1
                    cntr = 20
                    continue
# shows stats
currentBlind = (playerCount.players).copy()

def rotateBlind():
  for h in range(len(currentBlind)):
    blind = input(f"Player: {i} choose the small blind")
    continue
rotateBlind()


print(currentBlind)
  
    