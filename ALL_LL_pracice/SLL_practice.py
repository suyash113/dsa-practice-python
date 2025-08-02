class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def prepend(self, data):    
        new_node = Node(data)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def delete(self, data):
        if not self.head:
            return False
        
        current = self.head 
        prev = None
        while current:
            if current.data == data:
                if current == self.head:
                    if self.head == self.tail:
                        self.head = self.tail = None
                    else:
                        self.head = current.next
                    self.length -= 1
                else:
                    prev.next = current.next
                    self.length -= 1
            prev = current
            current = current.next
            
    def delete_by_index(self, index):
        if not self.head or index < 0 or index >= self.length:
            return False
        
        if index == 0:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
            self.length -= 1
            return True
        current = self.head
        prev = None
        for _ in range(index):
            prev = current
            current = current.next
        prev.next = current.next
        
    def insert(self, index, data):
        if index < 0 or index > self.length:
            return False
        
        new_node = Node(data)
        if index == 0:
            if self.head == None:
                self.head = self.tail = new_node
            else:
                new_node.next = self.head
                self.head = new_node
            self.length += 1
            return True
        
        current = self.head
        prev = None
        for _ in range(index):
            prev = current
            current = current.next
        prev.next = new_node
        new_node.next = current
        current = new_node
    
    def reverse(self):
        if not self.head:
            return False
        
        current = self.head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
        self.head, self.tail = self.tail, self.head
            
    def __str__(self):
        temp = self.head
        nodes = []
        while temp:
            nodes.append(str(temp.data))
            temp = temp.next
        return "->".join(nodes) + "-> None"
    
    
l1 = LinkedList()
l1.append(10)
l1.append(20)
l1.append(30)
l1.prepend(40)
print(l1)
l1.insert(4, 5)
print(l1)
# l1.reverse()
# print(l1)              
                    