n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
map.insert(0,[0 for _ in range(n)])
map.append([0 for _ in range(n)])
for i in range(n+2):
    map[i].insert(0, 0)
    map[i].append(0)

home = []
originalChickRC = []
candidateChickRC = []

for a in range(n+1):
    for b in range(n+1):
        if map[a][b] == 1 : home.append((a,b))
        elif map[a][b] == 2 : originalChickRC.append((a,b))


def calMin(r, c, chickRC):
    minLen = (n-1)*2

    for chick in chickRC:
        if(minLen > abs(chick[0]-r) + abs(chick[1]-c)):
            minLen = abs(chick[0]-r) + abs(chick[1]-c)
        
    return minLen

def combi(arr,r):
    arr = sorted(arr)
    visited = [False for _ in range(len(arr))]
    candidateChick = []
    candidateChicks = []

    def back(cnt):    
        if cnt == r:
            a = [x for x in candidateChick]
            candidateChicks.append(a)
            return
        start = arr.index(candidateChick[-1]) + 1 if candidateChick else 0
        for i in range(start, len(arr)):
            if not visited[i]:
                visited[i] = True
                candidateChick.append(arr[i])
                back(cnt + 1)
                visited[i] = False
                candidateChick.pop()
    back(0)
    return candidateChicks

candidateChickRC.extend(combi(originalChickRC,m))

def sumMin(arr1, arr2):
    an = []
    for a1 in arr1:
        ll = [abs(a1[0] - a2[0]) + abs(a1[1]-a2[1]) for a2 in arr2]
        an.append(min(ll))
    return sum(an)

ans = []
for ca in candidateChickRC:
    ans.append(sumMin(home, ca))

print(min(ans))