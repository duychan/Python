n = int(input())
myList = list(map(int, input().split()))[:n]
B = []
sum = 0
dicB = {0:-1}
length = 0
for i in range(len(myList)):
    sum += myList[i]
    B.append(sum)
for i in range(len(B)):
    if B[i] in dicB:
        length = max(length,i - dicB[B[i]]) # change value of dict by length which range from new index to first index
    else:
        dicB[B[i]] = i # set value of dict = index of array and key = value of array
if length > 0:
  print(length)
else:
  print(-1)