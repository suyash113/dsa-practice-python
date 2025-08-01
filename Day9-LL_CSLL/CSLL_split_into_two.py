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

    def delete(self, data):
        if self.head.next is None:
            self.head = None
        
        prev = None
        current = self.head
        while current:
            if current.data == data:
                prev.next = current.next
                return True
            prev = current
            current = current.next
        return False
    
    def split_ll(self):
        if not self.head or not self.head.next:
            return False

        first = CircularSinglyLinkedList()
        second = CircularSinglyLinkedList()

        current = self.head
        mid = (self.length + 1)//2
        for _ in range(mid):
            first.append(current.data)
            current = current.next
        
        for _ in range(self.length - mid):
            second.append(current.data)
            current = current.next 
            if current == self.head:
                break
        first.tail.next = first.head
        second.tail.next = second.head
        return first.__str__(), second.__str__()
    
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
l1.append(40)
l1.append(50)
print(l1)
# print(l1.search(20))
print(l1.split_ll())

    #  slow = self.head
    #     fast = self.head
    #     first = CircularSinglyLinkedList()
    #     second = CircularSinglyLinkedList()
    #     while fast and fast.next:
    #         first.append(slow.data)
    #         slow = slow.next
    #         fast = fast.next.next
    #         fast_data = fast.data
    #         if fast == self.head:      #fast == self.head.next or
    #             break
        
    #     while slow:
    #         slow_data = slow.data
    #         second.append(slow.data)
    #         slow = slow.next
    #         if slow == self.head:
    #             break
    #     return first.__str__(), second.__str__()