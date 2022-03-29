# Tic-Tac-Toe
import numpy as np 
import random 
from time import sleep 
  
# Tạo bàn cờ rỗng
def create_board(): 
    return(np.array([[0, 0, 0], 
                     [0, 0, 0], 
                     [0, 0, 0]])) 
  
# Kiểm tra danh sách còn rỗng
def possibilities(board): 
    l = [] 
      
    for i in range(len(board)): 
        for j in range(len(board)): 
              
            if board[i][j] == 0: 
                l.append((i, j)) 
    return(l) 
  
# chọn ngẫu nhiên
def random_place(board, player): 
    selection = possibilities(board) 
    current_loc = random.choice(selection) 
    board[current_loc] = player 
    return(board) 
  
# kiểm tra thắng theo cột
def row_win(board, player): 
    for x in range(len(board)): 
        win = True
          
        for y in range(len(board)): 
            if board[x, y] != player: 
                win = False
                continue
                  
        if win == True: 
            return(win) 
    return(win) 
  
# kiểm tra thắng theo dòng
def col_win(board, player): 
    for x in range(len(board)): 
        win = True
          
        for y in range(len(board)): 
            if board[y][x] != player: 
                win = False
                continue
                  
        if win == True: 
            return(win) 
    return(win) 
  
# kiểm tra thắng theo đường chéo
def diag_win(board, player): 
    win = True
    y = 0
    for x in range(len(board)): 
        if board[x, x] != player: 
            win = False
    if win: 
        return win 
    win = True
    if win: 
        for x in range(len(board)): 
            y = len(board) - 1 - x 
            if board[x, y] != player: 
                win = False
    return win 
  
# Đánh giá thắng thua  
def evaluate(board): 
    winner = 0
      
    for player in [1, 2]: 
        if (row_win(board, player) or
            col_win(board,player) or 
            diag_win(board,player)): 
                 
            winner = player 
              
    if np.all(board != 0) and winner == 0: 
        winner = -1
    return winner 

pc = 2

# Đánh giá cục diện trận đấu
def value(board):
  v = evaluate(board);
  if v == pc:
    return 1
  elif v == 3 - pc:
    return -1
  else:
    return 0

# thuật toán minimax
def minimax(board, d, player):
  if d==0 or evaluate(board)!=0:
    return board, value(board)
  if player == pc:
    max,bmax = -10,1;
    for l in possibilities(board):
      child = np.copy(board)
      child[l] = player
      b,v = minimax(child,d-1,3-player)
      if max<=v:
        max,bmax = v,child
    return bmax,max
  else:
    min,bmin = 10,1;
    for l in possibilities(board):
      child = np.copy(board)
      child[l] = player
      b,v = minimax(child,d-1,3-player)
      if min>=v:
        min,bmin = v,child
    return bmin,min

# lựa chọn nước đi sử dụng minimax
def minimax_place(board):
  b, v = minimax(board,1,pc)
  return b;

# chọn thủ công
def hand_place(board, player): 
    selection = possibilities(board) 
    i,j = map(int,input().split())
    if (i,j) in selection:
      board[i,j] = player 
    return(board) 

# Main function to start the game 
def play_game(): 
    board, winner, counter = create_board(), 0, 1
    print(board) 
      
    while winner == 0: 
        for player in [1, 2]: 
            if player == pc:
              print("PC move") 
              board = minimax_place(board)
            else:
              print("you move") 
              board = hand_place(board, player) 
            
           
            print(board) 
            counter += 1
            winner = evaluate(board) 
            if winner != 0: 
                break
    return(winner) 
  
# Driver Code 
print("Winner is: " + str(play_game())) 