# Imports
from functions import *

continuar = True
wordList = readList("Modulo_1\Projeto\medium_list.txt")

print("Bem vindo ao Jogo da Forca.\n")

while continuar:
    
    # escolhendo as opcoes do menu
    menuOpc = int(input(">>> MENU <<<\nEscolha uma opcao:\n1 - Iniciar Jogo\n2 - Mudar dificuldade\n3 - Sair\n"))

    # iniciando o jogo
    if menuOpc == 1:
        playGame(wordList)

    elif menuOpc == 2:
        # clear_output(wait = True)
        wordList = changeLevel()
        
    # saindo do programa
    elif menuOpc == 3:
        # clear_output(wait = True)
        print("\nSaindo... Obrigado por jogar!")
        continuar = False
        
    # verificacao inválido
    else:
        print("Opcao inválida! Digite novamente: ")
        

        
        