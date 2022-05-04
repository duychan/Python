ar = {}
t = int(input())
for i in range(t):
    n = int(input())
    dic = {}
    for j in range(n):
        s1, s2 = input().split()
        if s1 in dic:
            dic[s1].append(s2)
        else:
            dic[s1] = [int(s2)]
    print(dic)