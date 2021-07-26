# Functions
import random
from time import sleep
import os

# read file and transform into a list with all uppercase characters
"""
Faz a leitura da arquivo e armazena em uma lista
"""
def readList(fileName):
    l = []
    with open(fileName, "r") as file:
        for line in file:
            l.append(line[:-1].upper())
    return l

"""
Seleciona a dificuldade do jogo, alterando qual arquivo será selecionado.
Return:
    list::wordList : lista com as palavras escolhidas
    str : Nome da dificuldade
"""
def changeLevel():
    # building...
    print("Escolha a dificuldade:")
    print("1 - Facil")
    print("2 - Medio(padrao)")
    print("3 - Dificil")
    while True:
        choice = int(input())
        if choice == 1:
            print("Dificuldade -> Facil")
            wordList = readList('Modulo_1\Projeto\easy_list.txt')
            return wordList, "[Easy]"
        elif choice == 2:
            print("Dificuldade -> Media")
            wordList = readList('Modulo_1\Projeto\medium_list.txt')
            return wordList, "[Normal]"
        elif choice == 3:
            print("Dificuldade -> Dificil")
            wordList = readList('Modulo_1\Projeto\hard_list.txt')
            return wordList, ["Hard"]
        else:
            print("Opcao inválida, digita novamente.")

"""
Desenha a forca conforme o progesso do jogo
@params:
    int::fails : determina o desenho atual da forca
"""
def printHang(fails):
    if fails == 0:
        print("\
        +----+   \n\
        │        \n\
        │        \n\
        │        \n\
        │        \n")
    elif fails == 1:
        print("\
        +----+   \n\
        │    ☻   \n\
        │        \n\
        │        \n\
        │        \n")
    elif fails == 2:
        print("\
        +----+   \n\
        │    ☻   \n\
        │    │   \n\
        │        \n\
        │        \n")
    elif fails == 3:
        print("\
        +----+   \n\
        │    ☻   \n\
        │   /│   \n\
        │        \n\
        │        \n")
    elif fails == 4:
        print("\
        +----+   \n\
        │    ☻   \n\
        │   /│\\ \n\
        │        \n\
        │        \n")
    elif fails == 5:
        print("\
        +----+   \n\
        │    ☻   \n\
        │   /│\\ \n\
        │   /    \n\
        │        \n")
    elif fails == 6:
        print("\
        +----+   \n\
        │    ☻   \n\
        │   /│\\ \n\
        │   / \\ \n\
        │        \n")

"""
Imprime apenas as letras certas, deixando "_" nas que ainda não foram descobertas.

@params
    list::hits : lista de letras corretas
    str::word : palavra que será executada a verificacao
"""
def printCorrectWords(hits, word):
    current = ''
    for i in range(len(word)):
        if word[i] in hits:
            current += word[i]
        else:
            current += '_'
    print("> Palavra:    " + current)

"""
Imprime apenas as letras das tentativas erradas.

@params
    list::wrongList : lista com as letras erradas
"""
def printWrongWords(wrongList):
    print("> Tentativas: ", end=" ")
    for i in range(len(wrongList)):
        print(wrongList[i] + "  ", end="")
    print('\n')

"""
Recebe o input do usuário e verifica se a letra inserida é válida 
ou se já foi verificada anteriormente.

@params:
    list::hits : lista de letras corretas
    list::wrongList : lista com as letras erradas
"""
def verifyInput(hits, wrongList) :
    while True:
        letter = input("Escolha uma letra: ").upper()
        if len(letter) > 1 or letter.isnumeric():
            print("Dado inválido, digite apenas uma letra.")
        elif letter in hits or letter in wrongList:
            print("Letra já escolhida.")
        else:
            break
    return letter

"""
Verifica se a letra inserida faz parte da palavra

@params:
    str::letter : letra recebida pelo usuário
    str::word : palavra que será executada a verificacao
    list::hits : lista de letras corretas
    int::fails : usada como contador para as letras erradas
    list::wrongList : lista com as letras erradas 
"""
def validateLetter(letter, word, hits, fails, wrongList):
    if letter in word:
        print("Acerto miserávi!")
        sleep(1)
        hits.append(letter)
    else:
        print("Errou!")
        sleep(1)
        wrongList.append(letter)
        fails += 1

    return hits, fails, wrongList

# Start new game
def playGame(wordList):

    # cria contador, listas vazias e usando random para escolher a palavra
    fails = 0
    hits = []
    wrongList = []
    word = random.choice(wordList)
    print("\nIniciando o jogo...")

    while True:
        
        # Impressão dos dados
        printHang(fails)
        printCorrectWords(hits, word)
        printWrongWords(wrongList)
        # Input do usuário e validacao dos dados
        letter = verifyInput(hits, wrongList)
        hits, fails, wrongList = validateLetter(letter, word, hits, fails, wrongList)
        
        # Verifica se o usuário acertou a palavra inteira ou se esgotou as tentativas
        if len(set(hits)) == len(set(word)): # win state
            if fails==0:
                print("Perfect!")
                sleep(5)
            else: 
                print("Parabains!")
                sleep(5)
            break
        elif fails > 5: # game over
            os.system("cls")
            printHang(fails)
            print("E morreu...\n")
            print("A palavra correta era: " + word)
            sleep(3)
            break

        os.system("cls")
        pass
