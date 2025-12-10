from collections import deque
t = int(input())

def Dfunc(arr):
    if len(arr) > 0:
        del arr[0]
    return arr

def solution1(f, c, li):
    if c > 0:
        li = deque(map(int,li[1:-1].split(',')))
    else:
        li = deque()
    rev = 0
    for ff in f:
        if ff == 'R':
            rev+=1
        elif ff == 'D':
            if len(li) <= 0 : 
                return 'error'
            elif rev%2==0:
                li.popleft()
            elif rev%2==1 :
                li.pop()
    if rev%2==1:
       li.reverse()
    return '[' + ','.join(map(str, li))+']'
            
for i in range(t):
    print(solution1(list(input()), int(input()), input().rstrip()))