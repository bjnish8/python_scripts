class Node:
    def __init__(self, val, nextnode = None):
        self.val = val
        self.nextnode = nextnode

class LinkedList:
    
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
    
    def append(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            self.head.nextnode = None
        else:
            curr = self.tail
            curr.nextnode = node
            self.tail = node
    
    def display(self):
        curr = self.head
        while curr is not None:
            print(curr.val, end = "-->")
            curr = curr.nextnode
        print(None)
        
    def getfirst(self):
        return (self.head)
    
    def getlast(self):
        return(self.tail)
        
    def search(self,val):
        curr = self.head
        isvalid = False
        while curr:
            if curr.val == val:
                isvalid = True
                break
            curr = curr.nextnode
        return isvalid
    
    def insert(self, node, value):
        if not self.search(value):
            print ("Could not be added")
            return None
        curr = self.head
        while curr:
            if curr.val == value:
                temp = curr.nextnode
                curr.nextnode = node
                node.nextnode = temp
            curr = curr.nextnode
    def delete(self, value):
        if self.head.val == value:
            self.head = self.head.nextnode
            return None
        curr = self.head
        while curr.nextnode:
            if curr.nextnode.val == value:
                break
            curr = curr.nextnode
        curr.nextnode = curr.nextnode.nextnode
                
linked = LinkedList()
a = Node(10)
b = Node(20)
c = Node(1)
linked.append(a)
linked.append(b)
linked.append(c)
linked.display()
print(linked.search(2))
d = Node(31)
e = Node(2)
f = Node(91)
linked.insert(d, 20)
linked.display()
linked.delete(31)
linked.display()
linked.insert(d, 20)
linked.display()
linked.insert(e, 1)
linked.display()
linked.insert(f, 10)
linked.display()
print(linked.search(2))
