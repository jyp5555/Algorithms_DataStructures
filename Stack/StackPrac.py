#BOJ 10828
import sys

n = int(sys.stdin.readline().rstrip())

arr = list()

for i in range(n):
    commands= list(map(str,sys.stdin.readline().split()))
    if(commands[0] == "push"): 
        arr.append(int(commands[1]))
    elif(commands[0] == "pop"): 
        print(arr.pop() if len(arr) > 0 else -1)
    elif(commands[0] == "size"):
        print(len(arr))
    elif(commands[0] == "empty"):
        print(1 if len(arr) == 0 else 0)
    else:
        print(arr[-1] if len(arr) > 0 else -1)