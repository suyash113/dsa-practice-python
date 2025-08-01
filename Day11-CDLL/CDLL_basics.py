class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
            new_node.prev = self.tail
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.head.prev = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
            new_node.prev = self.tail
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def get(self, index):
        if not self.head or index < 0 or index >= self.length:
            return False
        
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data
    
    def set(self, index, data):
        if not self.head or index < 0 or index >= self.length:
            return False
        
        new_node = Node(data)
        current = self.head
        for _ in range(index):
            current = current.next
        
        current.next = new_node.next 
        current.prev = new_node.prev
        current = new_node
        return True
    
    def delete(self, data):
        if not self.head:
            return False
        
        current = self.data
        deleted = False
        while True:
            if current.data == data:
                if current == self.head:
                    if self.head == self.tail:
                        self.head = None
                        self.tail = None
                    else:
                        self.tail.next = current.next
                        current.next.prev = self.tail
                    self.length -= 1
                elif current == self.tail:
                    current.prev.next = self.head
                    current.next.prev = current.prev
                self.length -= 1
                deleted = True
            current = current.next
            if current == self.head:
                break
        return deleted
    
    def delete_by_index(self, index):
        if not self.head or index < 0 or index >= self.length:
            return False
        
        current = self.head
        if index == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.head.next
                self.tail.next= self.head
            self.length -= 1
            return True

        if index == self.length-1:
            current.prev.next = self.head
            current.next.prev = current.prev
            self.length -= 1
            return True
        