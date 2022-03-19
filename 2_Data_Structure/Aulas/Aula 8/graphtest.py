class Graph():

    def __init__(self):
        self.adjMatrix = {}
    
    def __repr__(self) -> str:
        pass
    
    def add(self, node):
        self.adjMatrix[node] = {}
    
    def connect(self, origin, destiny, weight = 1):
        self.adjMatrix[origin][destiny] = weight
        self.adjMatrix[destiny][origin] = weight
        
    def busca_profundidade(self, origem, visitados=None):
        # Criando lista de visitados vazia na primeira iteracao
        if visitados is None:
            visitados = []

        # Pegando os nós adjacentes, que são as chaves do meu dicionario interno
        visitados.append(origem)
        for adjacente in self.adjacencia[origem].keys():
            if adjacente not in visitados:
                self.busca_profundidade(adjacente, visitados)
        return visitados
    
    def busca_profundidade_verifica_caminho(self, origem, destino, visitados=None):
        # Criando lista de visitados vazia na primeira iteracao
        if visitados is None:
            visitados = []
            
        if origem == destino:
            return True
        
        # Pegando os nós adjacentes, que são as chaves do meu dicionario interno
        visitados.append(origem)
        for adjacente in self.adjacencia[origem].keys():
            if adjacente not in visitados:
                if self.busca_profundidade_verifica_caminho(adjacente, destino, visitados):
                    return True
                
        return False
    
    def busca_profundidade_exibe_caminho(self, origem, destino):
        predecessor={origem: None}  
        
        if self._busca_profundidade_exibe_caminho(origem, destino, predecessor=predecessor):
            pred = predecessor[destino]
            caminho_invertido = [destino]
            while pred is not None:
                caminho_invertido.append(pred)
                pred = predecessor[pred]

            caminho = ''
            for no in caminho_invertido[::-1]:
                caminho += f'{no} -> '
            return caminho[:-3]
    
    def _busca_profundidade_exibe_caminho(self, origem, destino, visitados=None, predecessor=None):
        # Criando lista de visitados vazia na primeira iteracao
        if visitados is None:
            visitados = []
        
        if predecessor is None:
            predecessor = {origem: None}
            
        if origem == destino:
            return True
        
        # Pegando os nós adjacentes, que são as chaves do meu dicionario interno
        visitados.append(origem)
        for adjacente in self.adjacencia[origem].keys():
            if adjacente not in visitados:
                predecessor[adjacente] = origem
                if self._busca_profundidade_exibe_caminho(adjacente, destino, visitados, predecessor):
                    return True
                
        return False

    # Breadth-first search
    def BFSearch(self, origin):
        # add origin node to queue
        queue = [origin]
        # create visited nodes list
        visited = []
        # while the list is not empty
        while len(queue) > 0:
            # extract the first element of the queue
            currentNode = queue.pop(0)
            # add this element into the visited list
            visited.append(currentNode)
            # visit the adjacent elements of this node
            for adjacent in self.adjMatrix[currentNode].keys():
                # node not in visited list and in queue
                if adjacent not in queue + visited:
                    # add this adjacent node to queue
                    queue.append(adjacent)
        return visited
    # Verify path with Breadth-first search, return True or False
    def BFSverifyPath(self, origin, destiny):
        # add origin node to queue
        queue = [origin]
        # create visited nodes list
        visited = []
        
        # while the list is not empty
        while len(queue) > 0:
            # extract the first element of the queue
            currentNode = queue.pop(0)
            # add this element into the visited list
            visited.append(currentNode)
            # visit the adjacent elements of this node
            for adjacent in self.adjMatrix[currentNode].keys():
                # node not in visited list and in queue
                if adjacent not in queue + visited:
                    # add this adjacent node to queue
                    queue.append(adjacent)
                # return true if the destintion has been reached
                if adjacent == destiny:
                    return True
        # return false if there is no connection
        return False
    # Show path with Breadth-first search, return pathway
    def BFSshowPath(self, origin, destiny):
        # add origin node to queue
        queue = [origin]
        # create visited nodes list
        visited = []
        # create predecessor list
        predecessor = {origin: None}
        
        # while the list is not empty
        while len(queue) > 0:
            # extract the first element of the queue
            currentNode = queue.pop(0)
            # add this element into the visited list
            visited.append(currentNode)
            # visit the adjacent elements of this node
            for adjacent in self.adjMatrix[currentNode].keys():

                # node not in list
                if adjacent not in queue + visited:
                    # add the current node to predecessor dict
                    predecessor[adjacent] = currentNode
                    # add adjacent node to queue
                    queue.append(adjacent)

                # destiation reached, show path
                if adjacent == destiny:
                   # building path in inverted order
                    path = [destiny]
                    # until reach the origin
                    while currentNode is not None:
                        # add the current node
                        path.append(currentNode)
                        # update node from its prvious connection
                        currentNode = predecessor[currentNode]
                    # back to original order
                    path.reverse()
                    # aux list for append separator character
                    result = ['->'] * (len(path) * 2 - 1)
                    # add all elements in path to aux lit
                    result[0::2] = path
                    # convert the list to a more readable string
                    return ' '.join([str(elem) for elem in result])
                
                
        return False

def createGraph():
    g = Graph()
    g.add(1)
    g.add(2)
    g.add(3)
    g.add(4)
    g.add(5)
    g.add(6)
    g.add(7)
    g.add(8)
    g.connect(1, 2)
    g.connect(1, 5)
    g.connect(2, 6)
    g.connect(6, 3)
    g.connect(6, 7)
    g.connect(3, 7)
    g.connect(3, 4)
    g.connect(7, 4)
    g.connect(7, 8)
    g.connect(4, 8)
    return g

g = createGraph()

print(f'Adj Matrix:{g.adjMatrix}')

bfs = g.BFSearch(2)

bfsvp = g.BFSverifyPath(2, 8)

bfssp = g.BFSshowPath(2, 8)

print(f'BFSearch result:\n {bfs}')
print(f'BFSverifyPath result:\n {bfsvp}')
print(f'BFSshowPath result:\n {bfssp}')