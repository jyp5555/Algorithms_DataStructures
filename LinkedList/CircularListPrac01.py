class Node(object):
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class CircularList(object):
    def __init__(self):
        self.head = self
        self.length = 0

    def isEmpty(self):
        return not bool(self.head)
    
    def getList(self, nodes):
        current = self.head
        for n in nodes:
            node = Node(n)
            current.next = node
            node.next = None
            current = current.next
        current.next = self
    
    def getPos(self, value):
        current = self.head
        while(current.next == self.head or current.next.value != value):
            current = current.next
        return current.next

    def getLength(self, pos):
        current = pos
        length = 0
        while(current and current.next != pos):
            length += 1
            current = current.next
        return length
    def printList(self):
        current = self.head
        while(current.next != self.head):
            print(current.next.value, end=" ")
            current = current.next
        print()
        
import sys, random
words = list(sys.stdin.readline().rstrip())
circularLst = CircularList()
circularLst.getList(words)
circularLst.printList()

randomNum = random.randint(0,len(words))
print(str(randomNum)+" "+words[randomNum])
searchPos = circularLst.getPos(words[randomNum])
print(searchPos)
print(circularLst.getLength(searchPos))
