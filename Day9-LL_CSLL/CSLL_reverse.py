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
        return True
    
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
    
    def reverse(self):
        if not self.head or self.head == self.tail:
            return False
        
        current = self.head
        prev = self.tail

        while current:
            next_node = current.next 
            current.next = prev
            prev = current
            current = next_node
            if current == self.head:
                break
        self.head, self.tail = self.tail, self.head
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
print(l1.reverse())
print(l1)
