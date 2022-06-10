class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
    def addNeighbors(self, neighbors):
        for neighbor in neighbors:
            self.neighbors.append(neighbor)
    def removeNeighbors(self ,neighbors):
        index = []
        for neighbor in neighbors:
            temp = self.neighbors.index(neighbor)
            index.append(temp)
        for i in range(0, len(index)):
            self.neighbors.pop(index[i])
    def setNeighbors(self, neighbors):
        self.neighbors = neighbors
    
def DFS(inputState, goalState):
    frontier = [inputState]
    explorer = []
    while frontier:
        state = frontier.pop((len(frontier)-1))
        explorer.append(state)
        if goalState == state:
            return explorer
        for neighbor in state.neighbors:
            if neighbor not in (explorer and frontier):
                frontier.append(neighbor)
    return False        

def BFS(inputState, goalState):
    frontier = [inputState]
    explorer = [] 
    while frontier:
        state = frontier.pop(0)
        explorer.append(state)
        if goalState == state:
            return explorer
        for neighbor in state.neighbors:
            if neighbor not in (explorer and frontier):
                frontier.append(neighbor)
    return False

nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")
nodeH = Node("H")
nodeI = Node("I")  
nodeJ = Node("J")
nodeK = Node("K")
nodeL = Node("L")
nodeM = Node("M")
nodeN = Node("N")
nodeO = Node("O")
nodeA.addNeighbors([nodeB, nodeC])
nodeB.addNeighbors([nodeD, nodeE])
nodeC.addNeighbors([nodeF, nodeG])
nodeD.addNeighbors([nodeH, nodeI])
nodeE.addNeighbors([nodeJ, nodeK])
nodeF.addNeighbors([nodeL, nodeM])
nodeG.addNeighbors([nodeN, nodeO])

result = DFS(nodeA , nodeH)
if result:
    s = 'explored '
    for i in result:
        s  += i.name + ' '
        print(s)
else: 
    print('Error')
  
    