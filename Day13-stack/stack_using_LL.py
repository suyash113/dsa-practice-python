class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class StackLinkedList:
    def __init__(self):
        self.top = None
        self.length = 0
    
    def push(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1
    
    def pop(self):
        temp = self.top
        if self.length == 0:
            return "Stack is empty"
        elif self.length == 1:
            self.top = None
        else:
            self.top = self.top.next
        return temp.data

    def peek(self):
        return self.top.data if self.length != 0 else print("Stack is empty")
    
    def __str__(self):
        temp = self.top
        items = []
        while temp:
            items.append(str(temp.data))
            temp = temp.next
        return "Top -> " + " -> ".join(items) + " -> None"
        
s = StackLinkedList()
s.push(10)
s.push(20)
s.push(30)
print(s)            # Top -> 30 -> 20 -> 10 -> None
print(s.pop())      # 30
print(s.peek())     # 20
print(s)            # Top -> 20 -> 10 -> None
