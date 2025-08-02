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
    
    def reverse(self):
        if not self.head:
            return False
        
        current = self.head
        while current:
            current.next, current.prev = current.prev, current.next
            current = current.prev
        self.head, self.tail = self.tail, self.head
        return True
    
    def palindrome(self):
        if not self.head:
            return False
        
        left = self.head
        right = self.tail
        for _ in range(self.length//2):
            if left.data != right.data:
                return False
            else:
                right = right.prev
                left = left.next
        return True
    
    def remove_duplicates(self):
        if not self.head:
            return False
        
        seen = set()
        current = self.head
        deleted = False
        while current:
            cu_data = current.data
            if current.data in seen:
                if current == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None
                    current.prev = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                self.length -= 1
                deleted = True
            else:
                seen.add(current.data)
            current = current.next
        return deleted 
    
    # def merge_sort(self):
    #     if not self.head:
    #         return False
        
    #     slow = self.head
    #     fast = self.head
    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next
    #     return 
    
    def rotate_by_k(self, k):
        if not self.head:
            return False
        
        current = self.head
        for _ in range(k):
            current = current.next
        
        self.head.prev  = self.tail.next
        self.tail.next = self.head
        self.tail = current
        return True

    def two_sum(self, target):
        if not self.head:
            return False
        
        left = self.head
        right = self.tail
        required = 0
        while left:
            if target > left.data:
                required = target - left.data
                if right.data == required:
                    return left.data, right.data
                else:
                    right = right.prev
            else:
                left = left.next
        return False
                
    
    def __str__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return "<->".join(nodes) + "<-> None"
    
l1 = DoublyLinkedList()
l1.append(2)
l1.append(7)
l1.append(11)
# print(l1)
# l1.prepend(30)
l1.append(15)
l1.append(20)
print(l1)
print(l1.reverse())
# print(l1.palindrome())
# print(l1.remove_duplicates())
print(l1)
# print(l1.two_sum(9))
# print(l1.rotate_by_k(2))
print(l1)