import heapq

class Node:
    def __init__(self, label, goalCost):
        self.label = label
        self.goalCost = goalCost
        self.cost = 10000
        self.parent = []
        self.child = []
    def __repr__(self):
        return str(dict({
            "label": self.label,
            "cost" : self.cost,
            "goal cost": self.goalCost
        }))
    def __lt__(self, other):
        return self.goalCost + self.cost < other.goalCost + other.cost
    def getLabel(self):
        return self.label

class Tree:
    def __init__(self):
        self.nodes = []
        self.edges = []
    def add_nodes(self, data):
        for node in data:
            self.nodes.append(node)
    def add_node(self, node):
        self.nodes.append(node)
    def getIndex(self, node):
        for i, n in enumerate(self.nodes):
            if n.getLabel() == node.getLabel():
                return i
        return -1
    def addEdges(self, tupleEdges):
        for t in tupleEdges:
            start_label = t[0]
            end_label = t[1]
            w = t[2]
            #Tim ra vi tri 2 node trong tree
            indexStartNode = self.getIndex(Node(start_label, None))
            indexEndNode = self.getIndex(Node(end_label, None))
            #them node child vao parent
            self.nodes[indexStartNode].child.append(self.nodes[indexEndNode])
            #them node parent vao child
            self.nodes[indexEndNode].parent.append(self.nodes[indexStartNode])
            self.edges.append((self.nodes[indexStartNode], self.nodes[indexEndNode],t[2]))
    def getEdge(self, startNode, endNode):
        try:
            #Tim ra khoang cach giua startNode va endNode
            for edge in self.edges:
                if edge[0] == startNode and edge[1] == endNode:
                    return edge
        except:
            return None

def updateCost(tree, currentNode, prevNode):
    #Tim ra cost giua currentNode va prevNode
    edge = tree.getEdge(prevNode, currentNode)
    if edge is not None:
        currentNode.cost = prevNode.cost + edge[2]

def aStarSearch(tree, start, end):
    frontier = [start]
    heapq.heapify(frontier)
    explored = []
    while len(frontier) > 0:
        state = heapq.heappop(frontier)
        explored.append(state)
        print(state)
        if state == end:
            return explored
        for child in state.child:
            #Truoc khi add vao heap thi phai update lai cost cua Node
            updateCost(tree, child, state)
            if child.getLabel() not in list(set(node.getLabel() for node in frontier + explored)):
                heapq.heappush(frontier, child)
    return False

if __name__ == "__main__":
    tree = Tree()
    tree.add_nodes([
        Node("A", 6),
        Node("B", 3),
        Node("C", 4),
        Node("D", 5),
        Node("E", 3),
        Node("F", 1),
        Node("G", 6),
        Node("H", 2),
        Node("I", 5),
        Node("J", 4),
        Node("K", 2),
        Node("L", 0),
        Node("M", 4),
        Node("N", 0),
        Node("O", 4)
    ])
    tree.addEdges([
        ("A", "B", 2),
        ("A", "C", 1),
        ("A", "D", 3),
        ("B", "E", 5),
        ("B", "F", 4),
        ("C", "G", 6),
        ("C", "H", 3),
        ("D", "I", 2),
        ("D", "J", 4),
        ("F", "K", 2),
        ("F", "L", 1),
        ("F", "M", 4),
        ("H", "N", 2),
        ("H", "O", 4),
    ])
    tree.nodes[0].cost = 0
    result = aStarSearch(tree, tree.nodes[0], tree.nodes[11])
    if result:
        s = 'explored: '
        for i in result:
            s += i.label + "(" + str(i.cost) + "," + str(i.goalCost) + ") "
            print(s)
    else:
        print('404 Not Found!')