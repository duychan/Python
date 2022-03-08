n = int(input())
listCostOfTickets = list(set(map(int,input().split())))
numberSV = int(input())
arr = []
dicBa = {}
for i in range(1,numberSV+1):
    balance = int(input())
    if balance in dicBa:
        arr.append(dicBa[balance])
    else:
        defaultVal = -1
        if balance in listCostOfTickets:
            defaultVal = balance
        else:
            for j in listCostOfTickets:
                if balance >= j:
                    defaultVal = j
        arr.append(defaultVal)
        dicBa[balance] = defaultVal
for i in arr:
    print(i)