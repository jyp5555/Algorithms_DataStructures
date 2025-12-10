from collections import deque

c, r = map(int,input().split())
tomatoes = [list(map(int, input().split())) for _ in range(r)]
dr = [0,0,1,-1]
dc = [1,-1,0,0]
res = []

def bfs():
    queue = deque()
    zeroCount = 0
    for i in range(r):
        for j in range(c):
            if tomatoes[i][j] == 0:
                zeroCount += 1
            if tomatoes[i][j] == 1:
                queue.append((i,j))

    if zeroCount == 0 : return 0
    
    while(queue):
        rr, cc = queue.popleft()
        
        for k in range(4):
            nr = rr + dr[k]
            nc = cc + dc[k]
            if nr < 0 or nc < 0 or nr >= r or nc >= c:
                continue
            if tomatoes[nr][nc] == 0:
                res.append(tomatoes[rr][cc] + 1)
                tomatoes[nr][nc] = tomatoes[rr][cc] + 1
                queue.append((nr,nc))
    
    for i in range(r):
        for j in range(c):
            if tomatoes[i][j] == 0:
                return -1
    return res[-1]-1

print(bfs())