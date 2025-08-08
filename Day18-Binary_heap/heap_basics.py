# class MinHeap:
#     def __init__(self):
#         self.heap = []
    
#     def parent(self, i):
#         return (i-1)//2

#     def left_child(self, i):
#         return 2*i + 1
#     def right_child(self, i):
#         return 2*i + 2

#     def insert(self, data):
#         self.heap.append(data)

#         self._bubble_up(len(self.heap)-1)

#     def _bubble_up(self, index):
#         while index > 0 and self.heap[index] < self.heap[self.parent(index)]:
#             self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
#             index = self.parent(index)

#     def extract_min(self):
#         if not self.heap:
#             return None
#         if len(self.heap) == 1:
#             return self.heap.pop()
        
#         root =self.heap[0]
#         self.heap[0] = self.heap.pop()
#         self._bubble_down(0)
#         return root
    
#     def _bubble_down(self, index):
#         smallest = index
#         left = self.left_child(index)
#         right = self.right_child(index)

#         if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
#             smallest = left
#         if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
#             smallest = right
        
#         if smallest != index:
#             self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
#         elif smallest == index:
#             return None
#         self._bubble_down(smallest)
    
#     def heapify(self, arr):
#         self.heap = arr
#         for i in range(len(arr)//2 - 1, -1, -1):
#             self._bubble_down(i)
        
# h = MinHeap()
# h.insert(5)    
# h.insert(8)    
# h.insert(3)    
# h.insert(1)

# print("Heap array:", h.heap)
# print("Extract min:", h.extract_min())
# print("Heap after extract:", h.heap)










class MinHeap:
    def __init__(self):
        self.heap = []

    # Index helpers
    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    # Insert value
    def insert(self, value):
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    def _bubble_up(self, index):
        while index > 0 and self.heap[index] < self.heap[self.parent(index)]:
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    # Extract minimum value (root)
    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move last element to root
        self._bubble_down(0)
        return min_val

    def _bubble_down(self, index):
        length = len(self.heap)
        while True:
            smallest = index
            left = self.left_child(index)
            right = self.right_child(index)

            if left < length and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < length and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                self._bubble_down(smallest)
                index = smallest
            else:
                break

    # Build heap from an unsorted list
    def heapify(self, arr):
        self.heap = arr[:]
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._bubble_down(i)

    # View heap
    def display(self):
        print("Heap array:", self.heap)
    
# h = MinHeap()
# for val in [5,3,8,1,6,2]:
#     h.insert(val)

# h.display()

# print("Extract min:", h.extract_min())
# h.display()

# print("Extract min:", h.extract_min())
# h.display()

# h.heapify([9,4,7,1,-2,6,5])
# h.display()

h = MinHeap()
h.insert(5)    
h.insert(8)    
h.insert(3)    
h.insert(1)

print("Heap array:", h.heap)
print("Extract min:", h.extract_min())
print("Heap after extract:", h.heap)