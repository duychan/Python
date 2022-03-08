n = int(input())
dic = {}
for i in range(n):
    name, val = list(input().split())
    if [name, val] in dic:
        dic[name,val] = val
    else
    