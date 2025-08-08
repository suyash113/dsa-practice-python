class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i-1)//2
    def left_child(self, i):
        return 2*i + 1
    def right_child(self, i):
        return 2*i + 2
    
    def insert(self, value, priority):
        temp_tuple = (value, priority)
        self.heap.append(temp_tuple)
        self.bubble_up(len(self.heap)-1)
    
    def bubble_up(self, index):
        while index > 0 and self.heap[index][1] > self.heap[self.parent(index)][1]:
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)
    
    def extract_max(self):
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.bubble_down(0)
        return root

    def bubble_down(self, index):
        biggest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[biggest][1] < self.heap[left][1]:
            biggest = left
        if right < len(self.heap) and self.heap[biggest][1] < self.heap[right][1]:
            biggest = right
        
        if biggest != index:
            self.heap[biggest], self.heap[index] = self.heap[index], self.heap[biggest]
            index = biggest
            self.bubble_down(index)
        else:
            return None
    def peek(self):
        return self.heap[0] if self.heap else None

    def hepify(self):
        arr = self.heap
        for i in range(len(arr)//2-1,-1,-1):
            self.bubble_down(i)

h = PriorityQueue()
h.insert("Wash DIshes",2)    
h.insert("Do DSA", 10)    
h.insert("REply to text", 6)    
h.insert("Watch Shorts", 1)

print(h.extract_max())
print(h.extract_max())
print(h.extract_max())