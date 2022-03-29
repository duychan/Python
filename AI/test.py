from collections import defaultdict

from numpy import greater


class Node:
    def __init__(self, name, par=None):
        self.name = name
        self.par = par

    def display(self):
        print(self.name)


def equal(O, G):
    return O.name == G.name


def checkInArray(t, Open):
    for x in Open:
        if equal(t, x):
            return True
    return False


def path(O, res):
    res.append(O.name)
    if(O.par != None):
        path(O.par, res)
    return res

def build_graph():
    V = ["A", "B", "C", "D", "E", "F"]
    E = [
    ["A","F"],["A","D"],
    ["B","C"],
    ["C","D"],["C","E"],["C","C"],
    ["F","D"],
    ]
    graph = defaultdict(list)
    for edge in E:
        a, b = edge[0], edge[1]
        graph[a].append(b)
        graph[b].append(a)
    return dict(graph)


def printExplored(Closed):
    for i in Closed:
        print(i.name, end=" ")
    print()


def DFS(S=Node("A"), G=Node("M")):
    Open = []
    Closed = []
    Open.append(S)
    while True:
        if len(Open) == 0:
            print("ko tim thay")
            return
        O = Open.pop(0)
        Closed.append(O)
        # print explored
        printExplored(Closed)
        if equal(O, G):
            res = []
            print("Path: ", path(O, res)[::-1])
            return
        pos = 0
        for x in graph[O.name]:
            t = Node(x)
            t.par = O

            ok1 = checkInArray(t, Open)
            ok2 = checkInArray(t, Closed)
            if not ok1 and not ok2:
                Open.insert(pos, t)
                pos += 1

graph = build_graph()
# print(graph)
DFS(Node("S"), Node("G"))