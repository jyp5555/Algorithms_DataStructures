# 이중 연결 리스트로 구현
class Node(object):
    def __init__(self, value, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next

class DLL(object):
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)

        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def getList(self, nodes):
        current = self.head
        for n in nodes:
            node = Node(n,current,current.next)
            current.next.prev = node
            current.next = node
            current = current.next
    
    def printList(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()
    

def searchValue(list1, list2):
    current1 = list1.tail.prev
    current2 = list2.tail.prev
    while(current1.value != None and current2.value != None):

        if(current1.value == current2.value):
            current1 = current1.prev
            current2 = current2.prev
        else:
            return current1.value
        
    return False


import sys
dll1 = DLL(); dll2 = DLL()
dll1.getList(list(sys.stdin.readline().rstrip()))
dll2.getList(list(sys.stdin.readline().rstrip()))
dll1.printList()
dll2.printList()
print(searchValue(dll1, dll2))