class CircularQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0
        self.capacity = capacity
    
    def enqueue(self, data):
        if self.size == self.capacity:
            return "Queue is full" 
        
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = data
        self.size += 1
        return True
    
    def dequeue(self):
        if self.size == 0:
            return "Queue is empty"
        
        data = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return data
    
    def peek(self):
        if self.size == 0:
            return None
        return self.queue[self.front]

    def __str__(self):
        return str(self.queue)

cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.dequeue()
cq.enqueue(40)
cq.enqueue(50)
cq.enqueue(60)  # This wraps around to the front
print(cq)       # Output shows circular behavior