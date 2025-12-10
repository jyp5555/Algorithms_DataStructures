#백준 1260
from collections import deque

m, n, start = map(int, input().rstrip().split(" "))
print(f"{m}, {n}, {start}")

adjList = {x : [] for x in range(1, m+1)}
visited = {}
for _ in range(n):
    a, b = map(int, input().rstrip().split(" "))
    adjList[a].append(b)
    adjList[b].append(a)
    visited[a] = False
    visited[b] = False

print(adjList)
#dfs 시작
dfsStack = deque()

def dfs(start):
    dfsStack.append(start)
    visited[start] = True
    while(len(dfsStack) > 0):
        curr = dfsStack.pop()
        print(adjList[curr])    
        for i in adjList[curr]:
            if(visited[i] == False):
                visited[i] = True
                print(visited)
                dfsStack.append(i)
        print(f"dfsStack : {dfsStack}")  
        print(curr)

dfs(start)