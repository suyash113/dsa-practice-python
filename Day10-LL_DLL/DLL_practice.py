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
        
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def get(self, index):
        if not self.head or index < 0 or index >= self.length:
            return "Index out of bound"
        
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data
    
    def set(self, index, data):
        if not self.head or index < 0 or index >= self.length:
            return "Index out of bound"
        
        new_node = Node(data)
        if index == 0:
            self.head.next = new_node.next
            self.head = new_node
            self.head.next = None
        
        if index == self.length-1:
            self.tail.prev = new_node
            self.tail = new_node
            self.tail.prev = None
            
        current = self.head
        for _ in range(index):
            current = current.next

        current.next = new_node.next
        current.prev = new_node.prev
        current = new_node
        current.next = None
        current.prev = None
        return True
    
    def delete(self, data):
        if not self.head:
            return False
        
        current = self.head
        while current:
            cu_data = current.data
            if current.data == data:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                elif current == self.head:
                    self.head = self.head.next
                    self.head.prev = None
                    current.next = None
                    self.length -= 1
                elif current == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None
                    current.prev = None
                    self.length -= 1
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    self.length -= 1
                return True
            current = current.next

        return False
    
    def delete_by_index(self, index):
        if not self.head or index < 0 or index >= self.length:
            return "Index out of bound"
        
        if index == 0:
            current = self.head
            self.head = self.head.next
            self.head.prev = None
            current.next = None
            self.length -= 1
            return True
        
        if index == self.length-1:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.next = None
            self.length -= 1
            return True

        else:
            temp1 = self.head
            for _ in range(index):
                temp1 = temp1.next
            
            temp1.prev.next = temp1.next
            temp1.next.prev = temp1.prev
            temp1.next = None
            temp1.prev = None
            self.length -= 1
            return True
    
    def insert(self, index, data):
        if not self.head or index < 0 or index > self.length:
            return "Index out of bound"       

        new_node = Node(data)
        if index == 0:
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
        
        else:
            current = self.head
            for _ in range(index-1):
                current = current.next
                
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node
            self.length += 1
            return True
        
            
    def __str__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return "<->".join(nodes) + "<-> None"
    
l1 = DoublyLinkedList()
l1.append(10)
l1.append(20)
l1.append(30)
print(l1)
l1.prepend(40)
print(l1)
# print(l1.get(4))
# print(l1.set(0,100))
# print(l1.delete(50))
# print(l1.delete_by_index(4))
print(l1.insert(5,50))

print(l1)     