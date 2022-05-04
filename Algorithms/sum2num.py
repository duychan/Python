ar = list(map(int, input().split()))
k = int(input())
ar2 = ar[:]
dic = {}
str = "NO"
for i in range(len(ar)):
    ar2[i] = k - ar[i]
    dic[ar[i]] = ar2[i]
for i in ar2:
    if i in dic and i != dic[i]:
        str = "YES"
        break
print(str)