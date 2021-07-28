
"""
Projeto Módulo I - The Hang Game
@author: João Baiochi
"""
# Imports
from functions import *

continuar = True
loadSuccess = False
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



prank()

while continuar:

    os.system("cls")
    if loadSuccess:
        game = "Continue"
    else:
        game = "New Game"

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
[[blue]]3[[white]] - Change Difficulty  [{level}]\n\
[[blue]]4[[white]] - Exit"))

    try:
        menuOpc = int(input())
    except ValueError:
       print("Invalid option! Type again: ")
       sleep(1)
       continue
    # New game
    if menuOpc == 1:
        if verifyList(wordList, gameFile, level):
            print("You already finished this level, please change difficulty in menu.")
            sleep(2)
        else:
            playGame(wordList, gameFile, level)
    
    # Open a save file
    elif menuOpc == 2:
        gameFile, loadSuccess = loadGame(gameFile)

    # Change difficulty
    elif menuOpc == 3:
        os.system("cls")
        wordList, level = changeLevel(gameFile)
    
    # Exit
    elif menuOpc == 4:
        print(colorText("\n[[cyan]]Bye! Thanks for playing![[white]]"))
        continuar = False
    # Wrong input
    else:
        print("Invalid option! Type again: ")
        sleep(1)
    
    pass
