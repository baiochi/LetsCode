lista = [[1,1,1,[2,1,[1,1,2]],1],[1,1,1,[2,1,[1,1,1]],1],1]

def somaLista(lista):
    soma = 0
    for i in lista:
        if type(i)==list:
            soma += somaLista(i)
        else:
            soma += i
    return soma

print(somaLista(lista))

def somaListaComprehension(*lista):
    return sum(somaListaComprehension(*i) if isinstance(i, list) else i for i in lista)
                                             
print(somaListaComprehension(lista,[1,1,1,[1,1]]))