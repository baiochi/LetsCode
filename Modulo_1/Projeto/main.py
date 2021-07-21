# Imports
from functions import *

continuar = True
wordList = readList("Modulo_1\Projeto\medium_list.txt")

print("Bem vindo ao Jogo da Forca.\n")

while continuar:

    menuOpc = int(input(">>> MENU <<<\nEscolha uma opcao:\n1 - Iniciar Jogo\n2 - Mudar dificuldade\n3 - Sair\n"))
    if menuOpc == 1:
        playGame(wordList)
    elif menuOpc == 2:
        wordList = changeLevel() 
    elif menuOpc == 3:
        print("\nSaindo... Obrigado por jogar!")
        continuar = False
    else:
        print("Opcao inválida! Digite novamente: ")
        

        
        