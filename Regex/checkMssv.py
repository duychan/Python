import re
n = int(input())
l = []
pattern = "^102(1[7-9]|2[0-1])0\d{3}"
for _ in range(n):
    mssv = input()
    rs = re.fullmatch(pattern, mssv)
    l.append(rs != None)
for _ in l:
    print(_)