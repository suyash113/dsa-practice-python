class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, data):
        self.items.append(data)
        
    def pop(self):
        if not self.is_empty():
            return  self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return "Top ->" + "->".join(map(str, reversed(self.items)))
    

s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s)         # Top -> 30 -> 20 -> 10
print(s.pop())   # 30
print(s.peek())  # 20
