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

    def check_for_sort(self):
        if self.head is None or self.head == self.tail:
            return False
        
        seen = set()
        current = self.head
        prev = self.tail
        while current:
            if current.data > current.next.data:
                return False
            current = current.next
            if current == self.head:
                break
        return True
    
    def insert_into_sorted(self, data):
        if self.head is None or self.head == self.tail:
            return False
        new_node = Node(data)
        current = self.head
        prev = self.tail
        while current:
            if prev.data < data and data < current.data :
                prev.next = new_node
                new_node.next = current
                self.length += 1
                return True
            prev = current
            current = current.next
            if current == self.head:
                break
        if self.head.data > data:
            self.tail.next = new_node
            new_node.next = self.head
            self.head = new_node
        elif self.tail.data < data:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
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
l1.insert_into_sorted(15)
print(l1)
# l1.insert(1,15)
# l1.insert(0,5)
# l1.insert(6, 100)
# print("after insert:", l1)