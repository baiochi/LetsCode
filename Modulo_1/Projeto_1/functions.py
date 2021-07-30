# Functions
import random
from time import sleep
import os

# Customized colors
# code extracted from https://gist.github.com/richardbwest/17674f84961e975d47cf106da9728dd2
COLORS = {
    "black":"\u001b[30;1m",
    "red": "\u001b[31;1m",
    "green":"\u001b[32m",
    "yellow":"\u001b[33;1m",
    "blue":"\u001b[34;1m",
    "cyan": "\u001b[36m",
    "white":"\u001b[37m",
}
def colorText(text):
    for color in COLORS: text = text.replace("[[" + color + "]]", COLORS[color])
    return text


"""
Load game file, search in saves folder and format the file to a dictionary
"""
def loadGame(gameFile):
    path = r"C:\Users\joaob\OneDrive\Documents\GitHub\LetsCode\Modulo_1\Projeto\saves"
    # list all files inside saves folder
    print("File(s) in folder:")
    for index, item in enumerate(os.listdir(path)): print(f"{str(index+1)} - {item.replace('.txt','')}")
    
    # collect user input for fileName
    while True:
        try:
            choice = int(input("Which file you want to load? (Type 0 to return) "))
            if choice == 0:
                return gameFile, True
            elif choice > len(os.listdir(path)):
                print("File not found. Please try again.")
            else:
                fileName = ''.join([item for index, item in enumerate(os.listdir(path))\
                                    if choice-1 == index])
                break
        except ValueError:
            print("Invalid input.", end=" ")
    
    # read file and formats into a dictionary
    try:
        # read file
        f = open(path + "\\" + fileName, "r", encoding="utf-8")
        data = f.read().replace('\'', '').replace('[','').replace(']','').split('\n')
        f.close()

        # create dictonary
        roundCount = data[0].split(':')
        easy = data[1].strip(" ").split(':')
        normal = data[2].strip(" ").split(':')
        hard = data[3].strip(" ").split(':')
        debug = data[4].strip(" ").split(':')
        
        dictonary = {
            roundCount[0] : int(roundCount[1]),
            easy[0] : easy[1].replace(" ","").split(','),
            normal[0] : normal[1].replace(" ","").split(','),
            hard[0] : hard[1].replace(" ","").split(','),
            debug[0] : debug[1].replace(" ","").split(',')
        }

        print(colorText(f"File [[yellow]]{fileName}[[white]] loaded successfully!"))
        sleep(2)

        return dictonary, False
    
    except IndexError:
        print(colorText(f"File [[yellow]]{fileName}[[white]] may be in wrong format or corrupted"))
    except ValueError:
        print(colorText(f"File [[yellow]]{fileName}[[white]] may be in wrong format or corrupted"))
    sleep(2)

    return gameFile, False
"""
Save current game state in a txt file at "saves" folder
"""
def saveGame(gameFile):
    path = r"C:\Users\joaob\OneDrive\Documents\GitHub\LetsCode\Modulo_1\Projeto\saves"
    print("File(s) in folder:")
    for index, item in enumerate(os.listdir(path)): print(f"{str(index)} - {item.replace('.txt','')}")
        
    while True:
        fileName = input("Please input the name of the file: ")
        if fileName + ".txt" in os.listdir(path):
            choice = input(colorText("[[red]]This file already exists, are you sure to overwrite data?[[white]] (Yes/No/Return) ")).upper()
            if choice == "YES":
                break
            elif choice == "NO":
                continue
            elif choice == "RETURN":
                return print("Saving not completed.")
            else:
                print("Invalid input.")
        else:
            break
    
    # save file
    with open(path + "\\" + fileName + ".txt", 'w') as file:  
        for key, value in gameFile.items():  
            file.write(f'{key}:{value}\n')
    file.close()
    print(colorText("[[cyan]]Saved successfully![[white]]"))
    sleep(1)

"""
Read the file and stores in a list. Check if the list has already finished.
"""
def readList(fileName, gameFile, level):
    file = open(fileName, 'r')
    wordList = [item for item in file.read().upper().split('\n')]
    file.close()
    if verifyList(wordList, gameFile, level):
        return print("You already finished this level!")
    else:
        return wordList, level
"""
Verify in the current game file difficulty if all words have been completed.
"""
def verifyList(wordList, gameFile, level):
    if [item for item in wordList if item not in gameFile[level]]==[]:
        return True
    else:
        return False
"""
Select game difficulty, choosing a file by each level.
Return:
    list::wordList : list with choosen words
    str : level name
"""
def changeLevel(gameFile):
    fileDict = {
        'Easy' : "Modulo_1\Projeto\word_list\easy_list.txt",
        'Normal' : "Modulo_1\Projeto\word_list\\normal_list.txt",
        'Hard' : "Modulo_1\Projeto\word_list\hard_list.txt",
        'Debug' : "Modulo_1\Projeto\word_list\debug_list.txt",
    }
    print("Choose game difficulty:")
    for i in range(len(fileDict.keys())): print("> " + list(fileDict)[i])

    while True:
        try:
            choice = input().capitalize()
            for i in range(len(fileDict.keys())):
                if choice == list(fileDict)[i]: 
                    return readList(fileDict[choice], gameFile, choice)
        except ValueError:
            print("\nInvalid option, please type again: ", end="")
        finally:
            print("\nWrong input, please type again: ", end="")

"""
Draw the hang and members as the game progress.

@params:
    int::fails : determines the current drawing of the hang
"""
def printHang(fails):
    if fails == 0:
        print("\
        ______   \n\
        │⁄   │   \n\
        │        \n\
        │        \n\
        │        \n\
        │        \n\
      ============")
    elif fails == 1:
        print("\
        ______   \n\
        │⁄   │   \n\
        │    ☻   \n\
        │        \n\
        │        \n\
        │        \n\
      ============")
    elif fails == 2:
        print("\
        ______   \n\
        │⁄   │   \n\
        │    ☻   \n\
        │    │   \n\
        │        \n\
        │        \n\
      ============")
    elif fails == 3:
        print("\
        ______   \n\
        │⁄   │   \n\
        │    ☻   \n\
        │   /│   \n\
        │        \n\
        │        \n\
      ============")
    elif fails == 4:
        print("\
        ______   \n\
        │⁄   │   \n\
        │    ☻   \n\
        │   /│\\ \n\
        │        \n\
        │        \n\
      ============")
    elif fails == 5:
        print("\
        ______   \n\
        │⁄   │   \n\
        │    ☻   \n\
        │   /│\\ \n\
        │   /    \n\
        │        \n\
      ============")
    elif fails == 6:
        print("\
        ______   \n\
        │⁄   │   \n\
        │    ☻   \n\
        │   /│\\ \n\
        │   / \\ \n\
        │        \n\
      ============")

"""
Print only the corret typed words, leaving '_' character for undiscovered ones

@params
    list::hits : correct letters already typed
    str::word : word which will be checked
"""
def printCorrectWords(hits, word):
    current = ''
    for i in range(len(word)):
        if word[i] in hits:
            current += word[i]
        else:
            current += '_'
    print(colorText("> [[cyan]]Word:[[white]]    " + current))

"""
Print only letters from failed attempts.

@params
    list::wrongList : correct letters already typed
"""
def printWrongWords(wrongList):
    print(colorText("> [[red]]Attempts:[[white]] "), end=" ")
    for i in range(len(wrongList)):
        print(wrongList[i] + "  ", end="")
    print('\n')

"""
Collect the input from the user and verify if the typed letter is valid
or if was already typed.

@params:
    list::hits : correct letters already typed
    list::wrongList : list with the wrong attempt letters
"""
def verifyInput(hits, wrongList) :
    while True:
        letter = input("Type a letter: ").upper()
        if len(letter) > 1 or not letter.isalpha():
            print("Invalid value, type only a letter.")
        elif letter in hits or letter in wrongList:
            print("Letter already chosen.")
        else:
            break
    return letter

"""
Checks if the letter belongs to the word

@params:
    str::letter : letter typed by the user
    str::word : word which will be checked
    list::hits : correct letters already typed
    int::fails : used as counter for the wrong words
    list::wrongList : list with the wrong attempt letters
"""
def validateLetter(letter, word, hits, fails, wrongList):
    if letter in word:
        print(colorText("[[cyan]]Correct![[white]]"))
        sleep(1)
        hits.append(letter)
    else:
        print(colorText("[[red]]Wrong![[white]]"))
        sleep(1)
        wrongList.append(letter)
        fails += 1

    return hits, fails, wrongList

"""
Checks if the letter belongs to the word

@params:
    str::gameFile : current state of the game
"""
def continueGame(gameFile) :
    # Choose to save the game
    while True:
        try:
            choice = input("Save the current game? (Yes/No)").upper()
        except ValueError:
            print("Invalid value.")
        if choice == 'YES':
            saveGame(gameFile)
            break
        elif choice == 'NO':
            break
        else:
            print("Invalid value.")
    
    # Choose to continue playing or return to menu
    while True:
        try:
            choice = input("Play another round? (Yes/No)").upper()
        except ValueError:
            print("Invalid value.")
        if choice == 'YES':
            return True
        elif choice == 'NO':
            print("Returning to main menu...")
            sleep(2)
            return False
        else:
            print("Invalid value.")

"""
Main function for initialize  the game
@params:
    list::wordList : list with the wrong attempt letters
    dict::gameFile : current state of the game (new or loaded)
    str::level : difficulty of the game, used to append the word in save file if user wins the game
"""
def playGame(wordList, gameFile, level):
    # create counter, empty lists, and randomly selects a word
    playingGame = True
    gameFile['round'] += 1
    fails = 0
    hits = []
    wrongList = []
    word = random.choice(wordList)
    print("\nStarting game...")
    sleep(2)
    #os.system('cls')

    while playingGame:
        
        # Data print
        printHang(fails)
        printCorrectWords(hits, word)
        printWrongWords(wrongList)
        # User input and data validation
        letter = verifyInput(hits, wrongList)
        hits, fails, wrongList = validateLetter(letter, word, hits, fails, wrongList)
        
        # Verify if the user find the complete word or run out of tries
        if len(set(hits)) == len(set(word)): # win state
            gameFile[level].append(word) # add completed word to the list
            print(colorText(f"You completed the word: [[yellow]]{word.upper()}[[white]] !"))
            if fails==0:
                print(colorText("[[green]]Perfect game![[white]]"))
                sleep(1)
            
            if continueGame(gameFile):
                # resets all variables to a new game and
                # avoid selecting an already played word
                word = [item for item in wordList if item not in gameFile[level]]
                # check if the list is empty
                if word == []:
                    print("You completed all words from this level, please select another on main menu.")
                    sleep(2)
                    playingGame = False # back to main menu
                else:
                    word = random.choice(word)
                    gameFile['round'] += 1
                    fails = 0
                    hits = []
                    wrongList = []
                    print("Starting round " + str(gameFile['round']) + " ...")
                    sleep(2)
                
            else:
                playingGame = False # back to main menu
        
        elif fails > 5: # game over
            os.system("cls")
            printHang(fails)
            print(colorText("[[red]]Game over...[[white]]\n"))
            print("A palavra correta era: " + colorText("[[green]]" + word + "[[white]]"))
            sleep(3)
            break

        os.system("cls")
        pass




def prank():
    os.system("cls")
    print(colorText("[[red]]\n\
   ___                            _          _   _        _  _            \n\
  |_  |                          | |        | | | |      | || |           \n\
    | |  ___    __ _   ___     __| |  __ _  | | | |  ___ | || |__    __ _ \n\
    | | / _ \  / _` | / _ \   / _` | / _` | | | | | / _ \| || '_ \  / _` |\n\
/\__/ /| (_) || (_| || (_) | | (_| || (_| | \ \_/ /|  __/| || | | || (_| |\n\
\____/  \___/  \__, | \___/   \__,_| \__,_|  \___/  \___||_||_| |_| \__,_|\n\
                __/ |                                                     \n\
               |___/                                                      \n[[white]]"))
    sleep(5)
    os.system("cls")
    print("mentira kkk")
    sleep(1)
    os.system("cls")