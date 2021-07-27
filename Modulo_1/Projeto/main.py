
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

# prank()

while continuar:

    print(colorText("[[red]]\n\
       __                         __         ____                     \n\
      / /___  ____ _____     ____/ /___ _   / __/___  ______________ _\n\
 __  / / __ \/ __ `/ __ \   / __  / __ `/  / /_/ __ \/ ___/ ___/ __ `/\n\
/ /_/ / /_/ / /_/ / /_/ /  / /_/ / /_/ /  / __/ /_/ / /  / /__/ /_/ / \n\
\____/\____/\__, /\____/   \__,_/\__,_/  /_/  \____/_/   \___/\__,_/  \n\
           /____/                                                     \n\
\n[[white]]"))
    print(colorText(f"  -> MENU <-\n\
Escolha uma opcao:\n\
[[blue]]1[[white]] - Iniciar Jogo   {level}\n\
[[blue]]2[[white]] - Mudar dificuldade\n\
[[blue]]3[[white]] - Sair"))
    try:
        menuOpc = int(input())
    except ValueError:
       print("Opcao inválida! Digite novamente: ")
       sleep(1)
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
        sleep(1)
    
    pass
