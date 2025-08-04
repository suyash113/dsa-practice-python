class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, data):
        self.items.append(data)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

    def __str__(self):
        return "Front -> " + " -> ".join(map(str, self.items)) + " <- Rear"
    
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q)             # Front -> 10 -> 20 -> 30 <- Rear
print(q.dequeue())   # 10
print(q.peek())      # 20
print(q)             # Front -> 20 -> 30 <- Rear
