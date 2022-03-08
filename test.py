import random
# Trò chơi 8 số

def ToadoZero(S):
  n = len(S)
  for i in range(n):
    for j in range(n):
      if S[i][j] == 0:
        return i,j

# o = 0 : Up
# o = 1 : Down
# o = 2 : Left
# o = 3 : Right
def move(S,o):
  n = len(S)
  L = [list(x) for x in S]
  i,j = ToadoZero(S)
  if o == 0:
    if i<n-1:
      L[i][j] = L[i+1][j]
      L[i+1][j] = 0
      return tuple([tuple(x) for x in L])
  elif o == 1:
    if i>0:
      L[i][j] = L[i-1][j]
      L[i-1][j] = 0
      return tuple([tuple(x) for x in L])
  elif o == 2:
    if j<n-1:
      L[i][j] = L[i][j+1]
      L[i][j+1] = 0
      return tuple([tuple(x) for x in L])
  elif o == 3:
    if j>0:
      L[i][j] = L[i][j-1]
      L[i][j-1] = 0
      return tuple([tuple(x) for x in L])
  return None


Goal = ((1,2,3),(4,5,6),(7,8,0))
#Goal = ((1,2,3,4),(5,6,7,8),(9,10,11,12),(13,14,15,0))
Start = Goal
for _ in range(5000):
  O = move(Start,random.randint(0,3))
  if O!=None:
    Start = O

for _ in Start: print(_)

OK = False
count = 0
# 1.Cho đỉnh xuất phát vào open. 
Open = [(Start,None,None)]
Closed = {Start}
# 2. Nếu open rỗng thì tìm kiếm thất bại, kết thúc việc tìm kiếm.
# 6. Trở lại bước 2.
<<<<<<< HEAD
def priority(arr):
    max = 0
    for i in range(len(arr)):
        if arr[i] > arr[max]:
            max = i
    item = arr[max]
    del arr[max]
    return item

=======
>>>>>>> 6aa056ac23397ebf8897093d7cf91f5387b3baf2
while len(Open) > 0:
  count += 1
  # 3. Lấy đỉnh đầu trong open ra và gọi đó là ʘ. Cho ʘ vào closed
  O_TT = Open.pop(0)
  O = O_TT[0]
  # 4. Nếu ʘ là đỉnh đích thì tìm kiếm thành công, kết thúc việc tìm kiếm.
  if O == Goal:
    OK = True
    break
  # 5. Tìm tất cả các đỉnh con của ʘ không thuộc open và closed cho vào cuối của open
  for i in range(4):
    child = move(O,i)
    if child!=None and child not in Closed:
      Open.append((child,i,O_TT))
      Closed.add(child)

print(OK,count)

def MyPrint(O_TT):
  if O_TT[2]!=None:
    MyPrint(O_TT[2])
    print(O_TT[1])
  for _ in O_TT[0]: print(_)

MyPrint(O_TT)