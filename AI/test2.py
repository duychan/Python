from copy import copy

class State:
    def __init__(self,data = None, N = 9):
        self.data = data
        self.N = N
    def clone(self):
        sn = copy.deepcopy(self)
        return sn
    def Print(self):
        sz = self.N
        for i in range(sz):
            for j in range(sz):
                tmp = self.data[i][j]
                if tmp == 0:
                    print('_|',end='')
                elif tmp == 1:
                    print('o|',end='')
                else:
                    print('x|',end='')
            print()
        print("=============")
class Operator:
    def __init__(self,x = 0, y = 0):
        self.x = x
        self.y = y
    def MOVE(self, s):
        sz = s.N
        x = self.x
        y = self.y
        if x < 0 or x >= sz:
            return None
        if y < 0 or y >= sz:
            return None
        if s.data[x][y] != 0:
            return None
        res = 0
        for i in range(9):
            for j in range(9):
                if s.data[i][j] != 0:
                    res += 1
        sn = s.clone()
        if res % 2 == 0:
            sn.data[x][y] = 2
        else:
            sn.data[x][y] = 1
        return sn
def isEndNode(s):
    sz = s.N
    data = s.data
    for i in range(sz):
        for j in range(sz):
            if(data[i][j]) == 0:
                return False
    return True

def CheckFrameWin(s):
    data = s.data
    for i in range(2,7):
        for j in range(2,7):
            if data[i-2][j-2] == 1 and data[i-2][j-1] == 1 and data[i-2][j] == 1 and data[i-2][j+1] == 1 and data[i-2][j+2] == 1:
                return 1
            if data[i+2][j-2] == 1 and data[i+2][j-1] == 1 and data[i+2][j] == 1 and data[i+2][j+1] == 1 and data[i+2][j+2] == 1:
                return 1
            if data[i-2][j-2] == 1 and data[i-1][j-2] == 1 and data[i][j-2] == 1 and data[i+1][j-2] == 1 and data[i+2][j-2] == 1:
                return 1
            if data[i-2][j+2] == 1 and data[i-1][j+2] == 1 and data[i][j+2] == 1 and data[i+1][j+2] == 1 and data[i+2][j+2] == 1:
                return 1
            if data[i-2][j-2] == 1 and data[i-1][j-1] == 1 and data[i][j] == 1 and data[i+1][j+1] == 1 and data[i+2][j+2] == 1:
                return 1
            if data[i-2][j+2] == 1 and data[i-1][j+1] == 1 and data[i][j] == 1 and data[i+1][j-1] == 1 and data[i+2][j-2] == 1:
                return 1
            if data[i-2][j-2] == 2 and data[i-2][j-1] == 2 and data[i-2][j] == 2 and data[i-2][j+1] == 2 and data[i-2][j+2] == 2:
                return 2
            if data[i+2][j-2] == 2 and data[i+2][j-1] == 2 and data[i+2][j] == 2 and data[i+2][j+1] == 2 and data[i+2][j+2] == 2:
                return 2
            if data[i-2][j-2] == 2 and data[i-1][j-2] == 2 and data[i][j-2] == 2 and data[i+1][j-2] == 2 and data[i+2][j-2] == 2:
                return 2
            if data[i-2][j+2] == 2 and data[i-1][j+2] == 2 and data[i][j+2] == 2 and data[i+1][j+2] == 2 and data[i+2][j+2] == 2:
                return 2
            if data[i-2][j-2] == 2 and data[i-1][j-1] == 2 and data[i][j] == 2 and data[i+1][j+1] == 2 and data[i+2][j+2] == 2:
                return 2
            if data[i-2][j+2] == 2 and data[i-1][j+1] == 2 and data[i][j] == 2 and data[i+1][j-1] == 2 and data[i+2][j-2] == 2:
                return 2
    return 0

def checkMyTurn(s):
    sum = 0
    for i in range(s.N):
        for j in range(s.N):
            if s.data[i][j] == 1:
                sum -= 1
            if s.data[i][j] == 2:
                sum += 1
    if sum != 0:
        return True
    else:
        return False
def Value(s):
    if CheckFrameWin(s) == 1:
            return -1
    if CheckFrameWin(s) == 2:
            return 1  
    return 0
def AlphaBeta(s, d, a, b, mp):
    if isEndNode(s) or d == 0 :
        return Value(s)
    sz = 9
    if  mp == True: 
        for i in range(sz):
            for j in range(sz):
                child = Operator(i ,j).MOVE(s)
                if child == None:
                    continue
                tmp = AlphaBeta(child, d - 1, a, b, False)
                a = max(a, tmp)
                if a >= b:
                    break
        return a
    else:
        for i in range(sz):
            for j in range(sz):
                child = Operator(i, j).MOVE(s)
                if child == None:
                    continue
                tmp = AlphaBeta(child, d - 1, a, b, True)
                b = min(b, tmp)
                if a >= b:
                    break
        return b
def MiniMax(s, d, mp):
    return AlphaBeta(s, d, -2, 2, mp) 

def RUN():
    player = 1
    turn = 0
    s=State( data=[[0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],])
    s.Print()
    while True:
        if turn % 2 + 1 == player:
            child = None
            while child == None:
                print("Di le dum cai: ")
                x = (int)(input())
                y = (int)(input())
                child = Operator(x,y).MOVE(s)
            s = child
            if CheckFrameWin(s) == 2:
                s.Print()
                print('Player Win')
                break
        else:
            mn = 2
            minChild = None
            sz = s.N
            for i in range(sz):
                for j in range(sz):
                    child = Operator(i,j).MOVE(s)
                    if child == None:
                        continue
                    tmp = MiniMax(child, 1, True)
                    print(i,j,tmp)
                    if mn > tmp:
                        mn = tmp
                        minChild = child
            s = minChild
            s.Print()
            if CheckFrameWin(s) == 1:
                s.Print()
                print("AI win")
                break
        s.Print()
        if isEndNode(s):
            print("Draw")
            break
        turn += 1
RUN()