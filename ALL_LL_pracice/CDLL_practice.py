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
    
    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = self.tail = new_node
            new_node.next = self.tail
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        self.length += 1
        return True
    
    def prepend(self, data):    
        new_node = Node(data)
        if self.head == None:
            self.head = self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
            self.head.prev = self.tail
        self.length += 1
        return True
    
    def delete(self, data):
        if not self.head:
            return False
        
        current = self.head
        prev = None
        while True:
            if current.data == data:
                if current == self.head:
                    if self.head == self.tail:
                        self.head = self.tail = None
                    else:
                        self.head = self.head.next
                        self.head.prev = self.tail
                        self.tail.next = self.head
                    self.length -= 1
                    return True
                elif current == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
                else:
                    prev.next = current.next
                self.length -= 1
                return True
            current = current.next
            if current == self.head:
                break
            
    def __str__(self): 
        temp = self.head
        nodes = []
        while temp:
            nodes.append(str(temp.data))
            temp = temp.next
            if temp == self.head:
                break
        return "->".join(nodes) + "-> back to head"  
      
l1 = CircularDoublyLinkedList()
l1.append(10)
l1.append(20)
l1.append(30)
l1.prepend(40)
print(l1)
l1.delete(10)
print(l1)