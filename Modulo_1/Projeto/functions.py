# Functions
import random

# read file and transform into a list with all uppercase characters
def readList(fileName):
    l = []
    with open(fileName, "r") as file:
        for line in file:
            l.append(line[:-1].upper())
    return l

# select difficulty
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
            return wordList
        elif choice == 2:
            print("Dificuldade -> Media")
            wordList = readList('Modulo_1\Projeto\medium_list.txt')
            return wordList
        elif choice == 3:
            print("Dificuldade -> Dificil")
            wordList = readList('Modulo_1\Projeto\hard_list.txt')
            return wordList
        else:
            print("Se ja esta dificil escolher um numero, imagina jogar...")

def printHang(fails, hits, word):
    if fails == 0:
        print("+----+")
        print("│")
        print("│")
        print("│")
        print("│")
    elif fails == 1:
        print("+----+")
        print("│    ☺")
        print("│")
        print("│")
        print("│")
    elif fails == 2:
        print("+----+")
        print("│    Ꝺ")
        print("│    │")
        print("│")
        print("│")
    elif fails == 3:
        print("+----+")
        print("│    Ꝺ")
        print("│   /│")
        print("│")
        print("│")
    elif fails == 4:
        print("+----+")
        print("│    Ꝺ")
        print("│   /│\\")
        print("│")
        print("│")
    elif fails == 5:
        print("+----+")
        print("│    Ꝺ")
        print("│   /│\\")
        print("│   /")
        print("│")
    elif fails == 6:
        print("+----+")
        print("│    Ꝺ")
        print("│   /│\\")
        print("│   / \\")
        print("│")

def printCorrectWords(hits, word):
    current = ''
    for i in range(len(word)):
        if word[i] in hits:
            current += word[i]
        else:
            current += '_'
    print("> Palavra: " + current)

def printWrongWords(wrongList):
    print("> Tentativas: ")
    for i in range(len(wrongList)):
        print(wrongList[i] + "  ", end="")
    print('')

# verify if letter has already been typed
def letterCheck(hits, wrongList) :
    while True:
        letter = input("Escolha uma letra: ").upper()
        if len(letter) > 1 or type(letter) != str:
            print("Dado inválido!")
        elif letter in hits or letter in wrongList:
            print("Letra já escolhida")
        else:
            break
    return letter

# verify if letter is a correct answer
def validateLetter(letter, word, hits, fails, wrongList):
    if letter in word:
        print("Acerto miserávi!")
        hits.append(letter)
    else:
        print("Errou!")
        wrongList.append(letter)
        fails += 1

    return hits, fails, wrongList

# Start new game
def playGame(wordList):
    fails = 0
    hits = []
    wrongList = []
    print("\nIniciando o jogo...")
    word = random.choice(wordList)
    #print("A palavra escolhida foi: ", word, "!")

    while True:
        printHang(fails, hits, word)
        printCorrectWords(hits, word)
        printWrongWords(wrongList)
        letter = letterCheck(hits, wrongList)
        hits, fails, wrongList = validateLetter(letter, word, hits, fails, wrongList)
        
        if len(set(hits)) == len(set(word)): # win state
            if fails==0:
                print("Perfect!")
            else: 
                print("Parabains!")
            break
        elif fails > 5: #game over
            printHang(fails, hits, word)
            print("You're dead.")
            break

        # clear consle
    #return
