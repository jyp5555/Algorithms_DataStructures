class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return not bool(self.head)

    def addLast(self, item):
        node = Node(item)
        if self.isEmpty():
            self.head = node
        else:
            current = self.head
            while current.pointer:
                current = current.pointer
            current.pointer = node
    
        self.length += 1

    def addHere(self, pos, item):
        node = Node(item)

        if self.isEmpty():
            print("list is empty")
        else:
            if(pos > 0 and pos <= self.length):
                current = self.head
                for i in range(pos):
                    current = current.pointer
                node.pointer = current.pointer
                current.pointer = node
                
            elif(pos == 0):
                node.pointer = self.head
                self.head = node
            
            self.length += 1

    def deleteNode(self, item):
        if self.isEmpty():
            print("list is empty")
        else:
            current = self.head
            if (current.value == item):
                self.head = current.pointer
                self.length -= 1
                current = None
                return True
            else:
                while(current):
                    delNode = current.pointer
                    print(str(delNode.value))
                    if(delNode.value == item):
                        current.pointer = delNode.pointer
                        delNode = None
                        self.length -=1
                        return True

                    current = current.pointer
                
                return False
    
    def searchItem(self,item):
        if self.isEmpty():
            print("list is empty")
            return False
        else:
            pos = 0
            current = self.head
            while current:
                if (current.value == item):
                    print(str(pos) +"<-위치 || 값->"+ str(current.value))
                    return pos
                current = current.pointer
                pos += 1
            return False
    
    def printList(self):
        if self.isEmpty():
            print("list is empty")
        else:
            current = self.head
            while current:
                print(current.value, end=" ")
                current = current.pointer
            print()

if __name__ == '__main__':
    list1 = LinkedList()
    print(list1.isEmpty())
    list1.addLast(1); list1.printList()
    list1.addLast(2); list1.printList()
    list1.addLast(4); list1.printList()
    list1.addLast(5); list1.printList()
    list1.addHere(1,3); list1.printList()
    list1.deleteNode(4); list1.printList()
    list1.searchItem(5)
    list1.printList()





