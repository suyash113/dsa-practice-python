class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear =None
        self.length = 0
        
    def enqueue(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.length += 1
    
    def dequeue(self):
        temp = self.front
        if self.length == 0:
            return "Queue is empty"
        elif self.length == 1:
            self.rear = None
        else:
            self.front = self.front.next
        self.length -= 1
        return temp.data
    
    def peek(self):
        return self.front.data if not self.length == 0 else None

    def __str__(self):
        temp = self.front
        items = []
        while temp:
            items.append(str(temp.data))
            temp = temp.next
        return "Front -> " + " -> ".join(items) + " <- Rear"

q = LinkedListQueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q)              # Front -> 10 -> 20 -> 30 <- Rear
print(q.dequeue())    # 10
print(q.peek())       # 20
print(q)              # Front -> 20 -> 30 <- Rear
