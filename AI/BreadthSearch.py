Start = [3, 3, 0, 0, 0]
Goal = [0, 0, 1, 3, 3]
OK = False
# Tìm tất cả đỉnh con của O
def Children(O):
    result = []
    # 1. 2 người qua sông
    if O[2] == 0:
        if O[0] >= 2:
            child = [O[0]-2, O[1], 1, O[3]+2, O[4]]
            if Check(child):
                result.append(child)
    else:
        if O[3] >= 2:
            child = [O[0]+2, O[1], 0, O[3]-2, O[4]]
            if Check(child):
                result.append(child)
    # 2. 1 người qua sông
    if O[2] == 0:
        if O[0] >= 1:
            child = [O[0]-1, O[1], 1, O[3]+1, O[4]]
            if Check(child):
                result.append(child)
    else:
        if O[3] >= 1:
            child = [O[0]+1, O[1], 0, O[3]-1, O[4]]
            if Check(child):
                result.append(child)
    # 3. 1 quỷ qua sông
    if O[2] == 0:
        if O[1] >= 1:
            child = [O[0], O[1]-1, 1, O[3], O[4]+1]
            if Check(child):
                result.append(child)
    else:
        if O[3] >= 1:
            child = [O[0], O[1]+1, 0, O[3], O[4]-1]
            if Check(child):
                result.append(child)
    # 4. 2 quỷ qua sông
    if O[2] == 0:
        if O[1] >= 2:
            child = [O[0], O[1]-2, 1, O[3], O[4]-2]
            if Check(child):
                result.append(child)
    else:
        if O[4] >= 2:
            child = [O[0], O[1]+2, 0, O[3], O[4]-2]
            if Check(child):
                result.append(child)
    return result
    
# Kiểm tra điều kiện bài toán (người >= quỷ)
def Check(child):
    if child[0] >= child[1]:
        return True
    if child[3] >= child[4]:
        return True
    return False
# 1. Cho đỉnh xuất phát vào Open
Open = [(Start,None)]
Closed = []
# 2. Nếu Open rỗng thì kết thúc việc tìm kiếm
# 6. Trở lại bước 2
while len(Open) > 0:
    # 3. Lấy đỉnh đầu trong Open ra và gọi đó là O, cho O vào Close
    O_TT = Open.pop(0)
    O = O_TT[0]
    Closed.append(O)
    # 4. Nếu O là đỉnh đích thì tìm kiếm thành công, kết thúc việc tìm kiếm
    if O == Goal:
        OK = True
        break
    # 5. Tìm tất cả các đỉnh con của O không phụ thuộc Open và Closed cho vào cuối của Open
    for child in Children(O):
        if child not in Open and child not in Closed:
            Open.append((child,O_TT))
print(OK)
print(O_TT)
