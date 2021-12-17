from tabulate import tabulate

def inicializarJogo():
    # Inteiro para contar em qual rodada estamos
    rodada = 0
    # Flag que é acionada para finalizar o jogo
    acabou = False
    # String para acompanhar qual o jogador da vez
    jogador = 'X'
    # Dicionário para registro do jogo
    tabuleiro = {
                " ": ["1", "2", "3"],
                "A": ["", "", ""],
                "B": ["", "", ""],
                "C": ["", "", ""]
            }
    return rodada, acabou, jogador, tabuleiro

def validaEntradaCorreta(letra, numero):
    """
    Confere se as coordenadas recebidas estão dentro das opções válidas
    Parâmetros: letra, numero
    Retorno: True(Opção válida)/False(Opção inválida)
    """
    if letra not in ["A", "B", "C"] or numero not in ["1", "2", "3"]:
        return False
    else:
        return True

def validaEntradaDisponivel(tabuleiro, letra, numero):
    """
    Confere se a coordenada recebida está disponível
    Parâmetros: tabuleiro, letra, numero
    Retorno: True(Disponivel)/False(Indisponivel)
    """
    if tabuleiro[letra][numero-1] != "":
        return False
    else:
        return True

def validaEntrada(tabuleiro, letraNumero):
    """
    Valida entrada do usuário para possíveis erros de digitação, cordenadas inválidas ou já utilizadas
    Parâmetros: tabuleiro, letraNumero (coordenadas da jogada)
    Retorno: letra e numero (coordenadas da jogada validadas)
    """
    # Valida digitações fora do esperado
    try:
        letra, numero = letraNumero.upper().split()
    except:
        return validaEntrada(tabuleiro, input(f"Coordenada inválida, digite uma válida: "))
    # Se entrada correta e disponível retorna, caso contrário chama a função novamente
    if validaEntradaCorreta(letra, numero):
        if validaEntradaDisponivel(tabuleiro, letra, int(numero)):
            return letra, int(numero)
        else:
            return validaEntrada(tabuleiro, input(f"Coordenadas indisponíveis, digite uma livre: ")) 
    else:
        return validaEntrada(tabuleiro, input(f"Coordenada inválida, digite uma válida: "))  

def jogada(tabuleiro):
    """
    Pede a jogada ao usuario e aplica ao tabuleiro
    Parâmetros: tabuleiro
    Retorno: tabuleiro
    """
    letra, numero = validaEntrada(tabuleiro, input(f"Vez do jogador: "))

    tabuleiro[letra][numero-1] = "O"

    return tabuleiro

def parabenizaGanhador(tabuleiro, jogadorGanhou):
    """
    Imprime o tabuleiro e parabeniza o ganhador
    Parâmetros: tabuleiro e jogador que ganhou
    """
    imprimiTabuleiro(tabuleiro)
    # Parabenização invertida pois jogador da vez veio depois da jogada onde a vitória ocorreu
    if jogadorGanhou == "X":
        print("A máquina ganhou!")
    else:
        print("O jogador ganhou! (Não deve acontecer)")

def imprimiTabuleiro(tabuleiro):
    """
    Imprime o tabuleiro utilizando o tabulate para estilização
    Parâmetros: tabuleiro
    """
    #print(tabulate(tabuleiro, headers="keys", tablefmt="fancy_grid"))
    print(tabuleiro['A'])
    print(tabuleiro['B'])
    print(tabuleiro['C'])

def confereGanhador(tabuleiro, jogador):
    """
    Confere linhas, colunas e diagonais pelo padrão de vitória
    Parâmetros: tabuleiro
    Retorno: True(Vitória)/False(Sem vitória)
    """
    # Confere Colunas
    if tabuleiro["A"].count("X") == 3 or tabuleiro["A"].count("O") == 3 or \
       tabuleiro["B"].count("X") == 3 or tabuleiro["B"].count("O") == 3 or \
       tabuleiro["C"].count("X") == 3 or tabuleiro["C"].count("O") == 3:
        parabenizaGanhador(tabuleiro, jogador)
        return True
    # Confere Linhas
    elif tabuleiro["A"][0] == tabuleiro["B"][0] == tabuleiro["C"][0] and tabuleiro["A"][0] != "" or \
         tabuleiro["A"][1] == tabuleiro["B"][1] == tabuleiro["C"][1] and tabuleiro["A"][1] != "" or \
         tabuleiro["A"][2] == tabuleiro["B"][2] == tabuleiro["C"][2] and tabuleiro["A"][2] != "":
        parabenizaGanhador(tabuleiro, jogador)
        return True
    # Confere Diagonais
    elif tabuleiro["A"][0] == tabuleiro["B"][1] == tabuleiro["C"][2] or tabuleiro["C"][0] == tabuleiro["B"][1] == tabuleiro["A"][2] and tabuleiro["B"][1] != "":
        parabenizaGanhador(tabuleiro, jogador)
        return True
    return False

def confereEmpate(tabuleiro):
    """
    Confere se há espaços disponíveis no tabuleiro
    Parâmetros: tabuleiro
    Retorno: True(Empate)/False(Sem empate)
    """
    if "" not in tabuleiro["A"] and "" not in tabuleiro["B"] and "" not in tabuleiro["C"]:
        imprimiTabuleiro(tabuleiro)
        print("O jogo empatou!")
        return True
    else:
        return False

def confereFim(tabuleiro, jogador):
    """
    Confere se os possiveis finais (vitória de alguma parte) ou empate ocorreram
    Parâmtros: tabuleiro, jogador (que fez a última jogada)
    Retorno: True(Acabou o jogo)/ False(Não acabou o jogo)
    """
    acabou = False
    acabou = confereGanhador(tabuleiro, jogador)
    if not acabou:
        acabou = confereEmpate(tabuleiro)
    return acabou

def empatarJogo(tabuleiro):
    """
    Procura o único espaço não jogado no tabuleiro
    Parâmetros: tabuleiro
    Retorno: letra e numero (coordenadas)
    """
    for key, item in tabuleiro.items():
        for index in range(len(item)):
            if item[index] == '':
                return key, index

def jogadaMaquina(tabuleiro, jogada):
    """
    Processa a jogada que deve ser feita pela máquina
    Parâmetros: tabuleiro, rodada (Contagem de quantas jogadas foram feitas)
    Retorno: tabuleiro
    """
    #print("Vez da máquina...")
    if jogada == 1:
        tabuleiro["A"][0] = "X"
    
    if jogada == 2:
        # jogada inicial 1: cima(A2), baixo(C2) ou direita(B3)'
        if tabuleiro["A"][1] == 'O' or tabuleiro["C"][1] == 'O' or tabuleiro["B"][2]:
            tabuleiro["C"][0] = "X"
        # jogada inicial 2: esquerda(B1)
        if tabuleiro["B"][0] == 'O':
            tabuleiro["A"][2] = "X"
        # jogada inicial 3: topo direito(A3)
        if tabuleiro["A"][2] == 'O':
            tabuleiro["C"][2] = "X"
        # jogada inicial 4: fundo esquerdo(C1)
        if tabuleiro["C"][0] == 'O':
            tabuleiro["C"][2] = "X"
        # jogada inicial 5: fundo direito(C3)
        if tabuleiro["C"][2] == 'O':
            tabuleiro["C"][0] = "X"
        # jogada inicial 6: meio(B2)
        if tabuleiro["B"][1] == 'O':
            tabuleiro["C"][2] = "X"

    if jogada == 3:
        # jogada inicial 1: verifica se o jogador evitou fechar a coluna
        if tabuleiro["B"][0] == '' and tabuleiro["C"][0] == 'X':
            tabuleiro["B"][0] = "X" # win
        # jogada inicial 1: continua o jogo
        if tabuleiro['B'][1] == '' and tabuleiro['C'][2] == '':
            tabuleiro["B"][1] = "X" 
        # jogada inicial 2: verifica se o jogador evitou fechar a linha
        if tabuleiro["A"][1] == '' and tabuleiro["A"][2] == 'X':
            tabuleiro["A"][1] = "X" # win
        # jogada inicial 2: continua o jogo
        if tabuleiro["B"][1] == '' and tabuleiro["A"][2] == 'X':
            tabuleiro["A"][2] = "X"
        # jogada inicial 3 ou 4: verifica se o jogador fechou a diagonal
        if tabuleiro["B"][1] == '' and tabuleiro["C"][2] == 'X':
            tabuleiro["B"][1] = 'X' # win
        # jogada inicial 3 ou 6: continua o jogo
        if tabuleiro["A"][2] == 'O' and tabuleiro["B"][1] == 'O'\
            and tabuleiro["C"][0] == '':
            tabuleiro["C"][0] = 'X'
        # jogada inicial 4: continua o jogo
        if tabuleiro["C"][0] == 'O' and tabuleiro["B"][1] == 'O'\
            and tabuleiro["A"][2] == '':
            tabuleiro["A"][2] = 'X'
        # jogada inicial 5: verifica se o jogador fechou a coluna A
        if tabuleiro["B"][0] == '' and tabuleiro["C"][0] == 'X' and tabuleiro["B"][1] == '':
            tabuleiro["B"][0] = 'X'
        # jogada inicial 5: continua o jogo
        if tabuleiro["B"][1] == '' and tabuleiro["C"][2] == 'O':
            tabuleiro["A"][2] = 'X'
        # jogada inicial 6 -> 6.1: evita o jogador ganhar na diagonal ('' - O - O):
        if tabuleiro["C"][0] == '' and tabuleiro["B"][1] == 'O'\
            and tabuleiro["A"][2] == 'O':
            tabuleiro["C"][0] = 'X'
        # jogada inicial 6 -> 6.2: evita o jogador ganhar na diagonal (O - O - ''):
        if tabuleiro["C"][0] == 'O' and tabuleiro["B"][1] == 'O'\
            and tabuleiro["A"][2] == '':
            tabuleiro["A"][2] = 'X'
        # jogada inicial 6: evitar fechar coluna 2 (O - O - ''):
        if tabuleiro["A"][1] == 'O' and tabuleiro["B"][1] == 'O'\
            and tabuleiro["C"][1] == '':
            tabuleiro["C"][1] = 'X'
        # jogada inicial 6: evitar fechar coluna 2 ('' - O - O):
        if tabuleiro["A"][1] == '' and tabuleiro["B"][1] == 'O'\
            and tabuleiro["C"][1] == 'O':
            tabuleiro["A"][1] = 'X'
        # jogada inicial 6: evitar fechar linha B (O - O - ''):
        if tabuleiro["B"][0] == 'O' and tabuleiro["B"][1] == 'O'\
            and tabuleiro["B"][2] == '':
            tabuleiro["B"][2] = 'X'
        # jogada inicial 6: evitar fechar linha B ('' - O - O):
        if tabuleiro["B"][0] == '' and tabuleiro["B"][1] == 'O'\
            and tabuleiro["B"][2] == 'O':
            tabuleiro["B"][0] = 'X'

    if jogada == 4:
        # jogada inicial 1: finaliza o jogo alternativa A3
        if tabuleiro["B"][1] == 'X' and tabuleiro["A"][2] == '':
            tabuleiro["A"][2] = "X"
        # jogada inicial 1 ou 2: finaliza o jogo alternativa C3
        if tabuleiro["B"][1] == 'X' and tabuleiro["C"][2] == '':
            tabuleiro["C"][2] = "X"
        # jogada inicial 2: finaliza o jogo alternativa C1
        if tabuleiro["B"][1] == 'X' and tabuleiro["C"][0] == '':
            tabuleiro["C"][0] = "X"
        # jogada inicial 3 ou 6.1: finaliza o jogo alternatia B1 (verifica coluna 1)
        if tabuleiro["B"][0] == '' and tabuleiro["C"][0] == 'X':
            tabuleiro["B"][0] = "X"
        # jogada inicial 3 ou 6.1: finaliza o jogo alternatia C2 (verifica linha C)
        if tabuleiro["C"][0] == 'X' and tabuleiro["C"][1] == ''\
            and tabuleiro["C"][2] == 'X':
            tabuleiro["C"][1] = "X"
        # jogada inicial 4, 5 ou 6.2: finaliza o jogo alternatia A2 (verifica linha A)
        if tabuleiro["A"][1] == '' and tabuleiro["A"][2] == 'X':
            tabuleiro["A"][1] = "X"
        # jogada inicial 4 ou 6.2: finaliza o jogo alternatia B3 (verifica coluna 3)
        if tabuleiro["A"][2] == 'X' and tabuleiro["B"][2] == ''\
            and tabuleiro["C"][2] == 'X':
            tabuleiro["B"][2] = "X"
        # jogada inicial 5: finaliza o jogo alternatia B2 (confere diagonal C1 - A3)
        if tabuleiro["C"][0] == 'X' and tabuleiro["B"][1] == ''\
            and tabuleiro["A"][2] == 'X':
            tabuleiro["B"][1] = "X"
        # jogada inicial 6 -> 6.1: evita o jogador ganhar na diagonal ('' - O - O):
        if tabuleiro["C"][0] == '' and tabuleiro["B"][1] == 'O'\
            and tabuleiro["A"][2] == 'O':
            tabuleiro["C"][0] = 'X'
        # jogada inicial 6 -> 6.2: evita o jogador ganhar na diagonal (O - O - ''):
        if tabuleiro["C"][0] == 'O' and tabuleiro["B"][1] == 'O'\
            and tabuleiro["A"][2] == '':
            tabuleiro["A"][2] = 'X'

    if jogada == 5:
        # ultima rodada, verifica se o jogador não marcou a coluna 1:
        if tabuleiro["B"][0] == '' and tabuleiro["C"][0] == 'X':
            tabuleiro["B"][0] = "X"
        # ultima rodada, verifica se o jogador não marcou a coluna 3:
        elif tabuleiro["A"][2] == 'X' and tabuleiro["B"][2] == ''\
            and tabuleiro["C"][2] == 'X':
            tabuleiro["B"][2] = "X"
        # ultima rodada, verifica se o jogador não marcou a linha A:
        elif tabuleiro["A"][1] == '' and tabuleiro["A"][2] == 'X':
            tabuleiro["A"][1] = "X"
        # ultima rodada, verifica se o jogador não marcou a linha C:
        elif tabuleiro["C"][0] == 'X' and tabuleiro["C"][1] == ''\
            and tabuleiro["C"][2] == 'X':
            tabuleiro["C"][1] = "X"
        # empata o jogo se não tiver como vencer:
        else:
            linha, coluna = empatarJogo(tabuleiro)
            tabuleiro[linha][coluna] = 'X'

    return tabuleiro

# Flag que é acionada para encerrar o programa
fimJogo = False

print("Instruções:\nDigite as coordenadas da sua jogada no formato letra e numero (Exs: 'A 1', 'B 2', 'C 3', etc)\n")
# Loop enquanto jogo não acabar que cicla em jogada da maquina e jogada do 
# usuario com as devidas validações de entrada e fim de jogo

while not fimJogo:
    rodada, acabou, jogador, tabuleiro = inicializarJogo()
    while not acabou:
        rodada += 1
        print(f'Rodada: {rodada}')
        tabuleiro = jogadaMaquina(tabuleiro, rodada)
        imprimiTabuleiro(tabuleiro)
        acabou = confereFim(tabuleiro, "X")
        if not acabou:
            tabuleiro = jogada(tabuleiro)
            #imprimiTabuleiro(tabuleiro)
            acabou = confereFim(tabuleiro, "O")

    if input("Continuar jogando?(s/n)") == 'n':
        fimJogo = True
