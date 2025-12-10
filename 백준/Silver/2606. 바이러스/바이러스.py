v = int(input().rstrip())
g = int(input().rstrip())
matrix = [[0 for _ in range(v+1)] for _ in range(v+1)]
visited = [False for _ in range(v+1)]

for _ in range(g):
    x, y = map(int, input().split(" "))
    matrix[x][y] = 1
    matrix[y][x] = 1

count = []

def dfs(start, matrix, visited, count):
    
    if visited[start] == True: return
    count.append(start)
    visited[start] = True

    for i, j in enumerate(matrix[start]):
        if j == 1 and visited[i] == False:
            dfs(i, matrix, visited, count)

dfs(1, matrix, visited, count)
print(len(count)-1)