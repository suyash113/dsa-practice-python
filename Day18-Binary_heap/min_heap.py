class MinHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i-1)//2
    
    def left_child(self, i):
        return 2*i + 1
    def right_child(self, i):
        return 2*i + 2
    
    def insert(self, data):
        self.heap.append(data)

        self.bubble_up(len(self.heap)-1)
    
    def bubble_up(self, index):
        while index > 0 and self.heap[index] < self.heap[self.parent(index)]:
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.bubble_down(0)
        return root
    
    def bubble_down(self, index):
        while True:
            smallest = index
            left = self.left_child(index)
            right = self.right_child(index)

            if left < len(self.heap)  and self.heap[smallest] > self.heap[left]:
                smallest = left 
            if right < len(self.heap) and self.heap[smallest] > self.heap[right]:
                smallest = right
            
            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                self.bubble_down(smallest)
                index = smallest
            else:
                break
         
    
    def heapify(self):
        arr = self.heap 
        for i in range(len(arr)//2 -1, -1, -1):
            self.bubble_down(i)
        
h = MinHeap()
h.insert(5)    
h.insert(8)    
h.insert(3)    
h.insert(1)

print("Heap array:", h.heap)
print("Extract min:", h.extract_min())
print("Heap after extract:", h.heap)