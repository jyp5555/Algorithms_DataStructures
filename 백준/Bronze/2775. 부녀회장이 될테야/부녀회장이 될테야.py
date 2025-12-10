floorDict = {}
ks = []
ns = []

for _ in range(int(input().rstrip())):
    ks.append(int(input().rstrip()))
    ns.append(int(input().rstrip()))
kmax = max(ks)
nmax = max(ns)
floorDict[0] = [x for x in range(nmax+2)]
for i in range(1,kmax+1):
    tmpDict = [0 for _ in range(nmax+2)]
    for j in range(1, nmax+1):
        tmpDict[j] = floorDict[i-1][j] + tmpDict[j-1]
    floorDict[i] = tmpDict
for i in range(len(ks)):
    print(floorDict[ks[i]][ns[i]])