import sys

#연결리스트
class Letter(object):
    def __init__(self, value, prev = None, next = None):
        self.value = value
        self.next = next
        self.prev = prev

class DoubleLinkedList(object):
    def __init__(self):
        self.head = Letter(None)
        self.tail = Letter(None, self.head)
        self.head.next = self.tail
        self.length = 0
    
    def listLength(self):
        return self.length
    
    def isEmpty(self):
        if self.length != 0:
            return False
        else:
            return True
    
    def getList(self, list):
        current = self.head
        current2 = self.tail
        for i in list:
            newLetter = Letter(i)
            current.next = newLetter
            newLetter.prev = current
            current2.prev = newLetter
            newLetter.next = current2
            current = current.next
            self.length += 1

    def printList(self):
        current = self.head.next
        while(current.next != None):
            print(current.value, end="")
            current = current.next
        print()
    
    def moveLeft(self, pos):
        #맨앞에서 무시
        if(pos == self.head):
            pos = self.head
            return pos
        elif(pos.prev == self.head):
            pos = self.head
            return pos
        else:
            pos = pos.prev
            return pos
    
    def moveRight(self, pos):
        #맨끝에서 무시
        if(pos == self.tail):
            pos = self.tail
            return pos
        elif(pos.next == self.tail):
            pos = self.tail
            return pos
        else:
            pos = pos.next
            return pos

    def delLetter(self, pos):
        if(pos == self.head or pos.prev == self.head or pos == None):
            pos = self.head
            return pos

        elif(pos.prev.prev == self.head):
            delNode = pos.prev
            self.head.next = pos
            pos.prev = self.head
            delNode = None
            self.length -=1
            return pos

        else: 
            delNode = pos.prev
            pos.prev = delNode.prev
            delNode.prev.next = pos
            delNode = None
            self.length -= 1
        
            return pos
    
    def insertLetter(self, pos, item):
        newLetter = Letter(item)
        #맨앞
        if(pos == self.head):
            pos = self.head
            newLetter.next = pos.next
            newLetter.prev = pos
            pos.next.prev = newLetter
            pos.next = newLetter
            
            pos = pos.next.next
            
        elif(pos.prev == self.head):
            newLetter.next = pos
            newLetter.prev = pos.prev
            pos.prev.next = newLetter
            pos.prev = newLetter

        #맨끝
        elif(pos == self.tail):
            newLetter.next = pos
            newLetter.prev = pos.prev
            pos.prev.next = newLetter
            pos.prev = newLetter

            pos = self.tail

        #중간
        else:
            newLetter.next = pos
            newLetter.prev = pos.prev
            pos.prev.next = newLetter
            pos.prev = newLetter

            pos = newLetter.next
        
        return pos
    
words = []
counts = 0
words = list(sys.stdin.readline().rstrip().lower())
counts = int(sys.stdin.readline())

lnklst = DoubleLinkedList()
lnklst.getList(words)
if(lnklst.listLength() > 0 and counts != None and counts > 0):
    cursor = lnklst.tail
    i = 0
    for i in range(counts):
        commands = list(sys.stdin.readline().rstrip().split(" "))
        if(commands[0] == "L"):
            cursor = lnklst.moveLeft(cursor)
        elif(commands[0] == "D"):
            cursor = lnklst.moveRight(cursor)
        elif(commands[0] == "B"):
            cursor = lnklst.delLetter(cursor)
        elif(commands[0] == "P"):
            cursor = lnklst.insertLetter(cursor,commands[1])
    lnklst.printList()  