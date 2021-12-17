""""
Super Desafio! - Faça um jogo de BlackJack usando funções: o BlackJack, ou Vinte e Um, 
é um jogo em que os jogadores podem comprar cartas livremente, enquanto tiverem menos de 21 pontos. 
No nosso jogo, o Ás vale um ponto; as cartas de 2 a 10 valem o número de pontos que elas representam; 
e Valete, Dama e Rei valem 10 pontos cada. Ganha o jogador que tiver o maior número de pontos, 
desde que este seja menor ou igual a 21. Nosso jogo deve ter as seguintes funções:

a. Função principal: a função que vamos chamar para iniciar o jogo. Essa função não irá receber 
nem retornar nenhuma variável. Ela deve perguntar o número de jogadores participantes e o nome 
de cada um. Em seguida ela chama as outras funções do jogo.

b. Função para criar o baralho: essa função deve criar um baralho (uma lista) com as cartas do baralho.

c. Função para a jogada: essa função deve receber o nome do jogador que irá realizar a jogada e, 
caso ele ainda esteja ativo (tenha menos de 21 pontos e ainda não tenha desistido de comprar cartas) 
deve perguntar se ele quer comprar uma carta. Se ele responder que sim, a função deve chamar a próxima 
função para sortear uma carta e somar o valor retornado na pontuação do jogador; se ele responder que não, 
a função deve desativar o jogador para que ele não possa mais comprar cartas; Essa função só deve ser chamada 
enquanto houver jogadores ativos.

d. Função para o sorteio: essa função retira uma carta aleatória do baralho e retorna o número de pontos 
que essa carta vale.

e. Função verificação: verifica e indica qual/quais jogador/jogadores tem o maior número de pontos, 
que seja menor ou igual a 21.
"""

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

    return ['A',*range(1,11),'J','Q','K'] * 2

def pickCard(deck):
    # random select a card
    card = random.sample(deck,1)[0]
    print(f'Card picked: {card}')
    # remove that card from deck
    deck.remove(card)
    return card

def verifyScore(players):

    validPlayers = []
    blackjack = 0
    _continue = False

    # display current score
    print('\n\u001b[36mRound summary:\u001b[37m')
    for player in players:
        if player.getState() == 'in':
            print(f'Player: {player.getName()}, score: {player.getScore()}')
            _continue = True
        elif player.getState() == 'out':
            print(f'Player: {player.getName()}, score: {player.getScore()}')
            # store score and name in a tuple
            validPlayers.append((player.getScore(),player.getName()))
        elif player.getState() == 'blackjack':
            print(f'Player: {player.getName()}, blackjack!')
            validPlayers.append((player.getScore(),player.getName()))
            blackjack += 1
        else:
            print(f'Player: {player.getName()}, is out!')
    print()

    # skip verification and continue the game
    if _continue:
        return True

    # verify two or more winners
    if blackjack > 1:
        print('\u001b[32mDraw game!\u001b[37m')
    # display the winner
    elif blackjack == 1 or validPlayers is not None:
        print(f'\u001b[32mThe winner is {max(validPlayers)[1]}, with {max(validPlayers)[0]} points!\u001b[37m')
    else:
        print('\u001b[32mNo winners in this game.\u001b[37m')
    
    return False
    

def playRound(player, deck):

    print(f'Player {player.getName()} turn.')
    choice = input(f'\u001b[36mCurrent score: {player.getScore()}, buy card? (Y/N)\u001b[37m')
    
    if choice.upper() == 'Y':
        card = pickCard(deck)
        player.updateScore(cardValues[card])
        if player.getScore() > 21:
            print(f'Player {player.getName()} is out! Score: {player.getScore()}')
            player.setState('lose')
        elif player.getScore() == 21:
            print(f'\u001b[31mPlayer {player.getName()} hit a Black Jack!\u001b[37m')
            player.setState('blackjack')
    else:
        player.setState('out')

def initGame():

    playersNumber = int(input('How many players? (Max 4)'))
    while playersNumber not in [1,2,3,4]:
        playersNumber = int(input('Invalid number, please type again:\nHow many players? (Max 4)'))
    players = []
    for index in range(playersNumber):
        players.append(Player( name = input(f'Type the name of the player {index+1}: ')))
    
    print('Creating deck...')
    deck = createDeck()
    
    _continue = True
    while _continue:

        for player in players:
            if player.getState() == 'in':
                playRound(player, deck)

        _continue = verifyScore(players)

def main():
    end = False

    while not end:

        choice = input('Play a game? (Y/S) ')
        if choice.upper() == 'Y':
            initGame()
        else:
            end = True


main()