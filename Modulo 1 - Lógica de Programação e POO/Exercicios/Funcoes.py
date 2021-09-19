import random

cardValues = {
    'A' : 1,
    'J' : 10,
    'Q' : 10,
    'K' : 10,
    1 : 1,
    2 : 2,
    3 : 3,
    4 : 4,
    5 : 5,
    6 : 6,
    7 : 7,
    8 : 8,
    9 : 9,
    10 : 10,
}

class Player():

    def __init__(self, name) -> None:
        self.name = name
        self.score = 0
        self.state = 'in'
    
    def getName(self):
        return self.name
    
    def getScore(self):
        return self.score
    
    def getState(self):
        return self.state
        
    def updateScore(self, score):
        self.score += score
    
    def setState(self, state):
        self.state = state



def createDeck():

    return ['A',*range(0,11),'J','Q','K'] * 2

def pickCard(deck):
    # random select a card
    card = random.sample(deck,1)[0]
    # remove that card from deck
    deck.remove(card)
    return card

def verifyScore(players):

    validPlayers = []
    blackjack = 0
    _continue = False

    # display current score
    for player in players:
        if player.getState() == 'in':
            print(f'Player: {player.getName()}, score: {player.getScore()}')
            _continue = True
        elif player.getState() == 'out':
            print(f'Player: {player.getName()}, score: {player.getScore()}')
            # store score and name in a tuple
            validPlayers.append((player.getScore(),player.getName()))
        elif player.getState() == 'blackjack':
            print(f'Player: {player.getName()}, hit a blackjack!')
            validPlayers.append((player.getScore(),player.getName()))
            blackjack += 1
        else:
            print(f'Player: {player.getName()}, is out!') 

    # skip verification and continue the game
    if _continue:
        return True

    # verify two or more winners
    if blackjack > 1:
        print('Draw!')
    # display the winner
    elif blackjack <= 1:
        print(f'The winner is {max(validPlayers)[1]}, with {max(validPlayers)[0]} points!')
        return False
    

def playRound(player, deck):

    print(f'Player {player.getName()} turn.')
    choice = input(f'Current score: {player.getScore()}, buy card? (Y/N)')
    
    if choice.upper() == 'Y':
        card = pickCard(deck)
        deck.remove(card)
        player.updateScore(cardValues[card])
        if player.getScore() > 21:
            print(f'Player {player.getName()} is out! Score: {player.getScore()}')
            player.setState('lose')
        elif player.getScore() == 21:
            print(f'Player {player.getName()} hit a Black Jack!')
            player.setState('blackjack')
    else:
        player.setState('out')

def initGame():

    playersNumber = int(input('How many players?'))
    players = []
    for index in range(playersNumber):
        players.append(Player( name = input(f'Type the name of the player {index+1}: ')))
    
    print('Creating deck...')
    deck = createDeck()
    
    _continue = True
    while _continue:

        for player in players:
            print(player.getState())
            if player.getState() == 'in':
                playRound(player, deck)

        _continue = verifyScore(players)

def main():
    end = False

    while not end:

        choice = input('Play a game? (Y/S)')
        if choice.upper() == 'Y':
            initGame()
        else:
            end = True


main()