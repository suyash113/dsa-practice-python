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

    def insert(self, index, data):
        if not self.head or index < 0 or index > self.length:
            return "index out of bound"
        
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
            self.length += 1
            return True

        current = self.head
        prev = self.tail
        for _ in range(index):
            prev = current
            current = current.next

        prev.next = new_node
        new_node.next = current

        if index == self.length:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            return True
    
    def jospheus(self, n, k):
        jos_list = CircularSinglyLinkedList()
        for i in range(1, n+1):
            jos_list.append(i)
        # print(jos_list.__str__())
        
        current = jos_list.head
        prev = jos_list.tail
        while jos_list.length > 1:
            for _ in range(k-1):
                prev = current
                current = current.next 
            prev.next = current.next

            if current == jos_list.head:
                jos_list.head = current.next
            if current == jos_list.tail:
                jos_list.tail = prev

            current = current.next 
            jos_list.length -= 1
        
        return jos_list.tail.data

        

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
print(l1.jospheus(5,2))
print(l1)
