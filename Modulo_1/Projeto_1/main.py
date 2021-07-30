
"""
Projeto Módulo I - The Hang Game
@author: João Baiochi
"""
# Imports
from functions import *

continuar = True
newGame = True
file = open("Modulo_1\Projeto\word_list\debug_list.txt", 'r')
wordList = [item for item in file.read().split('\n')]
file.close()
level = "Debug"
gameFile = {
    'round': 0,
    'Easy': [],
    'Normal': [],
    'Hard': [],
    'Debug': []
}



#prank()

while continuar:

    os.system("cls")
    if newGame:
        game = "New Game"
    else:
        game = "Continue"

    print(colorText("[[red]]\n\
       __                         __         ____                     \n\
      / /___  ____ _____     ____/ /___ _   / __/___  ______________ _\n\
 __  / / __ \/ __ `/ __ \   / __  / __ `/  / /_/ __ \/ ___/ ___/ __ `/\n\
/ /_/ / /_/ / /_/ / /_/ /  / /_/ / /_/ /  / __/ /_/ / /  / /__/ /_/ / \n\
\____/\____/\__, /\____/   \__,_/\__,_/  /_/  \____/_/   \___/\__,_/  \n\
           /____/                                                     \n\
\n[[white]]"))
    print(colorText(f" MAIN MENU\n\
[[blue]]1[[white]] - {game}\n\
[[blue]]2[[white]] - Load Game\n\
[[blue]]3[[white]] - Save Game\n\
[[blue]]4[[white]] - Change Difficulty  [{level}]\n\
[[blue]]5[[white]] - Exit"))

    try:
        menuOpt = int(input())
    except ValueError:
       print("Invalid option! Type again: ")
       sleep(1)
       continue
    # New game
    if menuOpt == 1:
        if verifyList(wordList, gameFile, level):
            print("You already finished this level, please change difficulty in menu.")
            sleep(2)
        else:
            playGame(wordList, gameFile, level)
            newGame = False
    
    # Open a save file
    elif menuOpt == 2:
        gameFile, newGame = loadGame(gameFile)
    
    # Save current game
    elif menuOpt == 3:
        try:
            choice = input("Save the current game? (Yes/No)").upper()
        except ValueError:
            print("Invalid value.")
        if choice == 'YES':
            saveGame(gameFile)
        elif choice == 'NO':
            continue
        else:
            print("Invalid value.")
        sleep(1)
    # Change difficulty
    elif menuOpt == 4:
        os.system("cls")
        wordList, level = changeLevel(gameFile)
    
    # Exit
    elif menuOpt == 5:
        print(colorText("\n[[cyan]]Bye! Thanks for playing![[white]]"))
        continuar = False
    # Wrong input
    else:
        print("Invalid option! Type again: ")
        sleep(1)
    
    pass
