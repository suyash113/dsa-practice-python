class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
        self.length += 1
        return True
    
    def search(self, data):
        if not self.head:
            return False
        
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
            if current == self.head:
                break
        return False
    
    # def delete(self, data):
    #     if not self.head:
    #         return False
        
    #     current = self.head
    #     prev= self.tail
    #     while current:
    #         if current.data == data:
                
    #             if self.head == self.tail:
    #                 self.head = None
    #                 self.tail = None
                
    #             elif current == self.head:
    #                 self.head = self.head.next
    #                 self.tail.next = self.head
                
    #             else:
    #                 prev.next = current.next
    #                 if current == self.tail:
    #                     self.tail = prev
    #             return True
            
    #         prev = current
    #         current = current.next
    #         if current == self.head:
    #             break
    #     return False
    
    def delete(self, data):
        if not self.head:
            return False
        
        current =self.head
        prev = self.tail
        while True:
            
            if current.data == data:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                elif current == self.head:
                    self.head = self.head.next
                    self.tail.next = self.head
                else:
                    prev.next = current.next
                    if current == self.tail:
                        self.tail = prev
            
            prev = current
            current = current.next
            if current == self.head:
                break
        return False
        

    def prepend(self, data):
        
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        return True
        
    def __str__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        return "->".join(nodes) + "-> (back to head)"
    
l1 = CircularSinglyLinkedList()
l1.append(10)
l1.append(20)
l1.append(30)

print(l1)
print(l1.delete(10))
# l1.prepend(40)
print(l1)