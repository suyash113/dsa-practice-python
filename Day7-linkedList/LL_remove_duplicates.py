class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
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
        self.length += 1
    
    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        
    def insert(self, index ,data):
        
        if index < 0 or index > self.length:
            print("Index out of bound")
            return False
        
        if index == 0:
            self.prepend(data)
            return True
        
        if index == self.length:
            self.append(data)
            return True
            
        new_node = Node(data)
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
            
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def search(self, data):
        temp = self.head
        temp_index = 0
        while temp:
            if temp.data != data:
                temp = temp.next
                temp_index += 1
            else:
                return temp_index
        return False
    
    def delete(self, index):
        if index < 0 or index > self.length:
            print("Index out of bound")
            return False
        
        if index == 0:
            removed = self.head
            self.head = removed.next
            removed.next = None
            self.length -= 1
            
            if self.length == 0:
                self.tail = None
            return True
        
        prev = self.head
        for _ in range(index-1):
            prev = prev.next
        
        to_delete = prev.next
        prev.next = to_delete.next
        to_delete.next = None
        self.length -= 1
        
        if self.length == index-1:
            self.tail = prev
            self.length -= 1
        return True
    
    def set(self, index, data):
        if index < 0 or index > self.length:
            print("Index out of bound")
            return False
        
        if index == 0:
            self.head.data = data
            return True
        
        if index == self.length - 1:
            self.tail.data = data
            return True
        
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        temp.next.data = data
        return True
    
    def get(self, index):
        if index < 0 or index > self.length:
            print("Index out of bound")
            return False
        
        if index == 0:
            return self.head
        
        if index == self.length - 1:
            return self.tail
        
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        return temp.next
    
    def remove_duplicates(self):
        seen = set()
        prev = None
        current = self.head
        
        while current:
            if current.data in seen:
                prev.next = current.next
                self.length -= 1
            else:
                seen.add(current.data)
                prev = current
            current = current.next
        self.tail = prev
                    
    def __str__(self):
        temp = self.head
        nodes = []
        while temp:
            nodes.append(str(temp.data))
            temp = temp.next
        return "->".join(nodes) + "-> None"
    
    
l1 = LinkedList()
l1.append(10)
l1.append(20)
l1.append(30)
l1.append(10)

# print("Before insert:", l1)

l1.insert(1, 15)
l1.insert(0, 5)
l1.insert(5, 40)
l1.insert(6, 30)

# print("After insert:", l1)
print(l1)
# print(l1.search(40))
# l1.delete(4)
l1.set(3,88)
print(l1.get(4).data)
print(l1)
l1.remove_duplicates()
print(l1)


    # def remove_duplicates(self):
    #     seen = set()
                
    #     prev = None
    #     current = self.head
    #     while current:
    #         if current.data in seen:
    #             prev.next = current.next        # self.delete(self.search(current.data))
    #             self.length -= 1
    #         else:
    #             seen.add(current.data)
    #             prev = current
    #         current = current.next
            
    #     self.tail = prev