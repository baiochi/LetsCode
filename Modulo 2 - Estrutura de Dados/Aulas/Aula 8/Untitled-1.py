import math

class Graph():
    def __init__(self) -> None:
        self.adjMatrix = {}

    def addVertex(self, number):
        self.adjMatrix[number] = {}

    def connectVertex(self, origin, destiny, weight=1):
        self.adjMatrix[origin][destiny] = weight
        self.adjMatrix[destiny][origin] = weight
    
    def deepSearch(self, origin, know=[]):
        know.append(origin)
        for adj in self.adjMatrix[origin].keys():
            if adj in know:
                pass
            else:
                self.deepSearch(adj,know)
        return know
    
    def broadSearch(self, origin):
        queue = [origin]
        know = []

        while len(queue) > 0:
            firstElement = queue[0]
            queue = queue[1:]
            know.append(firstElement)
            for adj in self.adjMatrix[firstElement].keys():
                if adj not in know and adj not in queue:
                    queue.append(adj)
        return know
    
    def DS_VerifyPath(self, origin, destiny, know=[]):



        if origin == destiny:
            return True
        
        know.append(origin)
        for adj in self.adjMatrix[origin].keys():
            if adj not in know:
                if self.DS_VerifyPath(adj, destiny, know):
                    return True

    def BS_VerifyPath(self, origin, destiny):
        
        queue = [origin]
        know = []
        previous = {origin: None}
        
        while len(queue) > 0:
            print(f'begin: {queue}')
            firstElement = queue[0]
            queue = queue[1:]
            know.append(firstElement)

            if firstElement == destiny:
                prev = firstElement
                path = [destiny]
                while prev is not None:
                    path.append(str(prev))
                    prev = previous[prev]

                print('->'.join(path[::-1]))
                return True
            
            
            for adj in self.adjMatrix[firstElement].keys():
                if adj not in know and adj not in queue:
                    previous[adj] = firstElement
                    queue.append(adj)
        return False

    def djikstra(self, origin):
        # create vertex dictionary with infinite values
        distance = {vertex: math.inf for vertex in self.adjMatrix.keys()}
        distance[origin] = 0

        # create dicitionary with None
        previous = {vertex: math.inf for vertex in self.adjMatrix.keys()}

        # create aux dict for not know vertex
        know = []
        not_know = distance.copy() # to remove already visited nodes

        while len(not_know) > 0:
            # order dictionary
            k = sorted(not_know.items(), key=lambda x: x[1])[0][0]
            # remove the visited node
            del not_know[k]
            # mark node a visited
            know.append(k)

            for adj in self.adjMatrix[k]:
                # if node was not visited
                if adj not in know:
                    newDist = distance[k] + self.adjMatrix[k][adj]
                    if newDist < distance[adj]:
                        distance[adj] = newDist
                        not_know[adj] = newDist
                        previous[adj] = k
        return distance, previous

def createGraph():
    g = Graph()
    g.addVertex(1)
    g.addVertex(2)
    g.addVertex(3)
    g.addVertex(4)
    g.addVertex(5)
    g.addVertex(6)
    g.addVertex(7)
    g.addVertex(8)
    g.connectVertex(1, 2)
    g.connectVertex(1, 5)
    g.connectVertex(2, 6)
    g.connectVertex(6, 3)
    g.connectVertex(6, 7)
    g.connectVertex(3, 7)
    g.connectVertex(3, 4)
    g.connectVertex(7, 4)
    g.connectVertex(7, 8)
    g.connectVertex(4, 8)
    return g


g = createGraph()

distance, previous = g.djikstra(2)


print(distance)
print(previous)

"""path_inverted = [str(destiny)]
prev = previous[destiny]
while prev is not None:
    path_inverted.append(str(prev))
    prev = """
#g.DS_VerifyPath(2, 8)