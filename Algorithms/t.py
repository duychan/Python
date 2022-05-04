import re
n = int(input())
ar = []
arr = []
pattern = "^([+-]{0,1})[0-9]*\.[0-9]*$"
for i in range(n):
    x = input()
    ar.append(x)
for i in ar:
    arr.append(re.fullmatch(pattern,i) != None)
for i in arr:
    print(i)