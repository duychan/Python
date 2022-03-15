Start = [3,3,0,0,0]
Goal = [0,0,1,3,3]
Open = [Start]
Close = []
OK = False
while(len(Open) > 0):
    O = Open.pop(0)
    Close.append(O)
    if 0 == Goal:
        OK = True
        break
     