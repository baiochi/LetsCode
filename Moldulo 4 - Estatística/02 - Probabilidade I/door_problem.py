import numpy as np

n = 10000

carros = np.random.randint(0, high = 3, size = n) + 1

escolha = np.random.randint(0, high = 3, size = n) + 1

ganha_ficando = 0
ganha_trocando = 0

for i in range(n):
    portas = [1,2,3]
 
    portas.remove(escolha[i])
    if carros[i] != escolha[i]:
        portas.remove(carros[i])

    porta_aberta = portas[np.random.randint(len(portas))]

    portas_2 = [1,2,3]

    portas_2.remove(porta_aberta)

    portas_2.remove(escolha[i])
    escolha_final = portas_2[0]

    if carros[i] == escolha[i]:
        ganha_ficando += 1
    
    if carros[i] == escolha_final:
        ganha_trocando += 1
