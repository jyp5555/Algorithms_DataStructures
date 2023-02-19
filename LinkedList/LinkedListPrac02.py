import sys

#스택활용

stack1 = list(sys.stdin.readline().rstrip())
stack2 = []
counts = int(sys.stdin.readline().rstrip())

for i in range(0,counts):
    commands = list(sys.stdin.readline().rstrip().split(" "))
    if commands[0] == "P":
        stack1.append(commands[1])
        print(stack1)
        print(stack2)
    elif commands[0] == "L":
        if(len(stack1) > 0):
            num = stack1.pop()
            print(num)
            stack2.append(num)
            print(stack1)
            print(stack2)
    elif commands[0] == "D":
        if(len(stack2) > 0):
            num = stack2.pop()
            stack1.append(num)
    else:
        if(len(stack1) > 0):
            del(stack1[-1])
if(len(stack2) == 1): 
    stack1.extend(stack2)
elif(len(stack2) > 1):
    stack2.reverse()
    stack1.extend(stack2)

print("".join(stack1))                  
