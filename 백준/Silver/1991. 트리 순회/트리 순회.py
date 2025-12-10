import string
adj = {str(a) : ['.','.'] for a in string.ascii_uppercase}
for _ in range(int(input().rstrip())):
    root, left, right = map(str, input().split(" "))
    adj[root][0] = left
    adj[root][1] = right

def preorder(start):    
    if(start == '.') : return
    print(start, end="")
    preorder(adj[start][0])
    preorder(adj[start][1])

def midorder(start):
    if(start == '.') : return    
    midorder(adj[start][0])
    print(start, end="")
    midorder(adj[start][1])

def postorder(start):
    if(start == '.') : return    
    postorder(adj[start][0])    
    postorder(adj[start][1])
    print(start, end="")

preorder('A')
print()
midorder('A')
print()
postorder('A')