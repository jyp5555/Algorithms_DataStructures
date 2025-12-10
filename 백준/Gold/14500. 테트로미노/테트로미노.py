n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

for b in board:
    b.extend([0,0,0])
for i in range(3):
    board.append([0 for _ in range(len(board[0]))])

maxS = 0
for i in range(n):
    for j in range(m):
        s1 = board[i][j] + board[i][j+1] + board[i][j+2] + board[i][j+3]        
        s2 = board[i][j] + board[i+1][j] + board[i+2][j] + board[i+3][j]

        s3 = board[i][j] + board[i+1][j] + board[i][j+1] + board[i+1][j+1]

        s4 = board[i][j] + board[i+1][j] + board[i+2][j] + board[i+2][j+1]
        s5 = board[i][j+1] + board[i+1][j+1] + board[i+2][j+1] + board[i+2][j]
        s6 = board[i][j] + board[i][j+1] + board[i+1][j] + board[i+2][j]
        s7 = board[i][j] + board[i][j+1] + board[i+1][j+1] + board[i+2][j+1]
        s8 = board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+1][j+2]
        s9 = board[i][j+2] + board[i+1][j] + board[i+1][j+1] + board[i+1][j+2]
        s10 = board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j]
        s11 = board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j+2]

        s12 = board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+2][j+1]
        s13 = board[i][j+1] + board[i+1][j] + board[i+1][j+1] + board[i+2][j]

        s14 = board[i][j] + board[i][j+1] + board[i+1][j+1] + board[i+1][j+2]
        s15 = board[i][j+2] + board[i][j+1] + board[i+1][j+1] + board[i+1][j]
        
        s16 = board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j+1]
        s17 = board[i+1][j] + board[i+1][j+1] + board[i+1][j+2] + board[i][j+1]
        s18 = board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+2][j]
        s19 = board[i][j+1] + board[i+1][j] + board[i+1][j+1] + board[i+2][j+1]
        ms = max([s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19]) 
        if ms > maxS : maxS = ms
print(maxS)