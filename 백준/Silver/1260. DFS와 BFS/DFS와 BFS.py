from collections import deque
import sys
sys.setrecursionlimit(10**7)

v, g, start = map(int, input().split(" "))
visitedDFS = [False for _ in range(v+1)]
visitedBFS = [False for _ in range(v+1)]
visitedDFS[0] = True
visitedBFS[0] = True
bfsQueue = deque([start])

adjMatrix = [[0 for _ in range(v+1)] for _ in range(v+1)]
for _ in range(g):
    x, y = map(int, input().split(" "))
    adjMatrix[x][y] = 1
    adjMatrix[y][x] = 1

def dfs(start, matrix, visited):
    print(start, end=" ")
    if visited[start] == True:
        return
    visited[start] = True
    for i, j in enumerate(matrix[start]) :
        if j == 1 and visited[i] == False: dfs(i, matrix, visited)

def bfs(matrix, visited, queue):
    if not queue: return

    v = queue.popleft()
    print(v, end=" ")

    visited[v] = True

    for i, j in enumerate(matrix[v]):
        if j == 1 and visited[i] == False:
            visited[i] = True
            queue.append(i)
    
    bfs(matrix, visited, queue)

dfs(start, adjMatrix, visitedDFS)
print()
bfs(adjMatrix, visitedBFS, bfsQueue)