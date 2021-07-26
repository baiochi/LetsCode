
"""
Projeto Módulo I - Jogo da Forca

@author: João Baiochi
"""
# Imports
from functions import *
from time import sleep
import os

os.system("cls")

continuar = True
wordList = readList("Modulo_1\Projeto\medium_list.txt")
level = "[Normal]"

while continuar:

    print("\n\
       __                         __         ____                     \n\
      / /___  ____ _____     ____/ /___ _   / __/___  ______________ _\n\
 __  / / __ \/ __ `/ __ \   / __  / __ `/  / /_/ __ \/ ___/ ___/ __ `/\n\
/ /_/ / /_/ / /_/ / /_/ /  / /_/ / /_/ /  / __/ /_/ / /  / /__/ /_/ / \n\
\____/\____/\__, /\____/   \__,_/\__,_/  /_/  \____/_/   \___/\__,_/  \n\
           /____/                                                     \n\
\n")

    try:
        menuOpc = int(input(f"  -> MENU <-\n\
Escolha uma opcao:\n\
1 - Iniciar Jogo   {level}\n\
2 - Mudar dificuldade\n\
3 - Sair\n"))
    except ValueError:
       print("Opcao inválida! Digite novamente: ")
       sleep(2)
       continue
    if menuOpc == 1:
        playGame(wordList)
    elif menuOpc == 2:
        os.system("cls")
        wordList, level = changeLevel()
        os.system("cls")
    elif menuOpc == 3:
        print("\nSaindo... Obrigado por jogar!")
        continuar = False
    else:
        print("Opcao inválida! Digite novamente: ")
        sleep(2)
    
    pass
