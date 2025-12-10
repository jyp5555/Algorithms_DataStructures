from collections import deque
n = int(input().rstrip())
board = [[0 for _ in range(n)] for _ in range(n)]
board.insert(0,[-1 for _ in range(n)])
board.append([-1 for _ in range(n)])
for i in range(n+2):
    board[i].insert(0,-1)
    board[i].append(-1)

k = int(input().rstrip())
for j in range(k):
    x, y = map(int, input().split())
    board[x][y] = 1

l  = int(input().rstrip())
ls = deque()
for m in range(l):
    ls.append(tuple(map(str, input().split())))

dx = [0, 1, 0, -1] #우, 하, 좌, 상
dy = [1, 0, -1, 0]
#head = 3, tail = 2
t = 0
x = 1
y = 1
d = 0
tot = deque()
while True:
    
    tot.append((x,y))
    if t == 0:
        board[x][y] = 2
    if board[x][y] == 1:
        board[x][y] = 2
    elif board[x][y] == 0 :
        board[x][y] = 2
        tlo = tot.popleft()
        board[tlo[0]][tlo[1]] = 0

    if ls[0][0] == str(t-1) and ls[0][1] == 'L':
        nx = x + dx[(d + 3) % 4]
        ny = y + dy[(d + 3) % 4]
        d += 3
    elif ls[0][0] == str(t-1) and ls[0][1] == 'D':
        nx = x + dx[(d + 1) % 4]
        ny = y + dy[(d + 1) % 4]
        d += 1
    else:
        nx = x + dx[d]
        ny = y + dy[d]

    t += 1

    if board[nx][ny] == -1 or board[nx][ny] > 1:
        t += 1
        break
    else:
        x = nx
        y = ny
    

print(t)