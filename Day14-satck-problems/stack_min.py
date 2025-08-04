class Node:
    def __init__(self, data=None, next= None):
        self.data = data
        self.next = next
    
    def __str__(self):
        str1 = str(self.data)
        if self.next:
            str1 += "," + str(self.next)
        return str1

class StackMin:
    def __init__(self):
        self.top = None
        self.minNode = None
    
    def min(self):
        if not self.minNode:
            return False
        return self.minNode.data
    
    def push(self, data):
        if self.minNode and (self.minNode.data < data):
            self.minNode = Node(data = self.minNode.data, next =self.minNode)
        else:
            self.minNode = Node(data = data, next = self.minNode)
        self.top = Node(data = data, next=self.top)
    
    def pop(self):
        if not self.top:
            return False
        
        self.minNode = self.minNode.next
        data = self.top.data
        self.top = self.top.next
        return data
    
m = StackMin()
m.push(10)
m.push(20)
m.push(30)
print(m.min())
m.push(5)
print(m.min())
print(m.pop())
print(m.pop())