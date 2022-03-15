n = int(input())
dic = {}
count = 0
for _ in range(n):
    name, val = input().split()
    if name in dic:
        dic[name].append(val)
    else:
        dic[name] = [val]
for i in dic.values():
    if len(set(i)) >= 2:
        count += 1
print(count)