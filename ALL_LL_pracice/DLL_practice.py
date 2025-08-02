class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
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
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def prepend(self, data):    
        new_node = Node(data)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def delete(self, data):
        if not self.head:
            return False
        
        current = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    if self.head == self.tail:
                        self.head = self.tail = None
                    else:
                        self.head = self.head.next
                        self.head.prev = None
                    self.length -= 1
                    return True
                elif current == self.tail:
                    self.tail = self.tail.prev
                    d1 = self.tail.data
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                self.length -= 1
                return True
            current = current.next
    
    def delete_by_index(self, index):
        if not self.head or index < 0 or index >= self.length:
            return False
        
        if index == 0:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.length -= 1
            return True
        if index == self.length-1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return True
        current = self.head
        for _ in range(index):
            current = current.next
        
        current.prev.next = current.next
        current.next.prev = current.prev
        self.length -= 1
    
    def insert(self, index, data):
        if index < 0 or index > self.length:
            return False
        
        new_node = Node(data)
        if index == 0:
            if self.head == None:
                self.head = self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            self.length += 1
            return True
        
        if index == self.length:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1
            return True
        
        current = self.head
        for _ in range(index-1):
            prev = current
            current = current.next
        
       
        new_node.next = current.next
        current.next = new_node
        new_node.prev = current
        self.length += 1
        
    def reverse(self):
        if not self.head:
            return False
        
        current = self.head
        while current:
            current.next, current.prev = current.prev, current.next
            current = current.prev   
        self.head, self.tail = self.tail, self.head
        
    def __str__(self):
        temp = self.head
        nodes = []
        while temp:
            nodes.append(str(temp.data))
            temp = temp.next
        return "<->".join(nodes) + "<-> None"

l1 = DoublyLinkedList()
l1.append(10)
l1.append(20)
l1.append(30)
l1.prepend(40)
print(l1)
# l1.insert(3, 5)
# print(l1)
l1.reverse()
print(l1)