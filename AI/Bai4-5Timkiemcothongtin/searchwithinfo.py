from Tree import Tree
import heapq

def updateFrontier(frontier, newNode):
    for index, n in enumerate(array_of_node):
        if n == newNode:
            if frontier[index].cost > newNode.cost:
                frontier[index] = newNode

def GBPSearch(initialState, goalTest):
    frontier = []
    explored = []
    heapq.heapify(frontier)
    heapq.heappush(frontier, initialState)
    while len(frontier) > 0:
        state = heapq.heappop(frontier)
        explored.append(state)
        if state == goalTest:
            return explored
        for neighbor in state.get_children():
            if neighbor not in (frontier and explored):
                heapq.heappush(frontier, neighbor)
            elif neighbor in frontier:
                updateFrontier(frontier=frontier, newNode=neighbor)
    return False

if __name__ == '__main__':
    nodeA = Tree("A", 6)
    nodeB = Tree("B", 3)
    nodeC = Tree("C", 4)
    nodeD = Tree("D", 5)
    nodeE = Tree("E", 3)
    nodeF = Tree("F", 1)
    nodeG = Tree("G", 6)
    nodeH = Tree("H", 2)
    nodeI = Tree("I", 5)  
    nodeJ = Tree("J", 4)
    nodeK = Tree("K", 2)
    nodeL = Tree("L", 0)
    nodeM = Tree("M", 4)
    nodeN = Tree("N", 0)
    nodeO = Tree("O", 4)
    nodeA.add_child(nodeB)
    nodeA.add_child(nodeC)
    nodeA.add_child(nodeD)
    nodeB.add_child(nodeE)
    nodeB.add_child(nodeF)
    nodeC.add_child(nodeG)
    nodeC.add_child(nodeH)
    nodeD.add_child(nodeI)
    nodeD.add_child(nodeJ)
    nodeF.add_child(nodeK)
    nodeF.add_child(nodeL)
    nodeF.add_child(nodeM)
    nodeH.add_child(nodeN)
    nodeH.add_child(nodeO)
    result = GBPSearch(nodeA, nodeN)
    if result:
        s = 'explored: '
        for i in result:
            s += i.data + " "
            print(s)
    else:
        print('404')