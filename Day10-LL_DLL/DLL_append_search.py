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
        
    # def append(self, data):
        # new_node = Node(data)
        # if self.head == None:
        #     self.head = new_node
        #     self.tail = new_node
        # else:
        #     self.tail.next = new_node
        #     new_node.prev = self.tail
        #     self.tail = new_node
        # self.length += 1
 
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
           
    # def prepend(self, data):
    #     new_node = Node(data)
    #     if self.head == None:
    #         self.head = new_node
    #         self.tail = new_node
    #     else:
    #         self.head.prev = new_node
    #         new_node.next = self.head
    #         self.head = new_node
    #     self.length += 1
    
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
    
    # def pop(self):
    #     if not self.head:
    #         return False
        
    #     temp = self.tail
    #     if self.head == self.tail:
    #         self.head = self.tail = None
    #     else:
    #         self.tail = self.tail.prev
    #         self.tail.next = None
    #         temp.prev = None
    #     self.length -= 1
    #     return temp
    
    def pop(self):
        if not self.head:
            return False
        
        current = self.tail

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            current.prev = None
        self.length -= 1
            
    
    
    # def pop_first(self):
    #     if not self.head:
    #         return False
        
    #     temp = self.head
    #     if self.head == self.tail:
    #         self.head = self.tail = None
    #     else:
    #         self.head = self.head.next
    #         self.head.prev = None
    #         temp.next = None
    #     self.length -= 1
    #     return temp
    
    def pop_first(self):
        if not self.head:
            return False
        
        current = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            current.next = None
        self.length -= 1
        return current
    
    def __str__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        return "<->".join(nodes) + "<-> None"
    
l1 = DoublyLinkedList()
l1.append(10)
l1.append(20)
l1.append(30)
print(l1)
l1.prepend(40)
print(l1)
l1.pop_first()
print(l1)