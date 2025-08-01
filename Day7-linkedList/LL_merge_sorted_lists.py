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
                return f"Index of {data} is {temp_index}"
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
    
    # def merge(self, l1, l2):
    #     temp_l1 = l1.head
    #     temp_l2 = l2.head
    #     merged_nodes =[]
    #     for _ in range(l1.length + l2.length):
    #         if temp_l1 is not None and temp_l1.data <= temp_l2.data:
    #             merged_nodes.append(str(temp_l1.data))
    #             temp_l1 = temp_l1.next
    #         else:
    #             merged_nodes.append(str(temp_l2.data))
    #             temp_l2 = temp_l2.next
            
    #     return "->".join(merged_nodes) + "-> None"
            
    def merge(self, l1, l2):
        dummy = Node(0)
        tail = dummy
        
        current1 = l1.head
        current2 = l2.head
        
        while current1 and current2:
            if current1.data < current2.data:
                tail.next = current1
                current1 = current1.next
            else:
                tail.next = current2
                current2 = current2.next 
            tail = tail.next 
        
        if current1:
            tail.next =current1 
        elif current2:
            tail.next =current2
            
        merged_list = LinkedList()
        merged_list.head = dummy.next
        
        temp = dummy.next
        while temp:
            merged_list.length += 1 
            if temp.next is None:
                merged_list.tail = temp
            temp = temp.next 
        return merged_list
        
    def rm_duplicates(self):
        seen =set()
        prev = None
        current =self.head
        while current:
            if current.data in seen:
                prev.next = current.next
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
l1.append(1)
l1.append(2)
l1.append(4)
print(l1)

l2 = LinkedList()
l2.append(1)
l2.append(3)
l2.append(4)
print(l2)

merged = LinkedList().merge(l1, l2)
print(merged)
