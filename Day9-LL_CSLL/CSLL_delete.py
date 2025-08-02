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
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        self.length += 1
        
    
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
        self.length += 1
        return True

    def search(self, data):
        if self.head is None:
            return False
        
        current = self.head
        index = 0 
        while current:
            if current.data == data:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def delete(self, data):
        if not self.head:
            return False
        
        current = self.head
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
                self.length -= 1
                return True
            prev = current
            current = current.next
            if current == self.head:
                break
        return False

    def delete_by_index(self, index):
        if not self.head or index < 0 or index >= self.length:
            return "index out of bound"
        
        if index == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
            self.length -= 1
            return True

        current = self.head
        prev = self.tail
        for _ in range(index):
            prev = current
            current = current.next
        prev.next = current.next
        

        if current == self.tail:
            self.tail = prev
        
        self.length -= 1
        return True
    
    def __str__(self):
        if self.head is None:
            return "List is empty"
        
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
print(l1.delete_by_index(3))
print(l1)