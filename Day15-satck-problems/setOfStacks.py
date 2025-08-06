class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []
    
    def push(self, data):
        if not self.stacks or len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])
        self.stacks[-1].append(data)
    
    def pop(self):
        if  not self.stacks:
            return None
        data = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        return data
    
    def pop_at(self, index):
        if not self.stacks or index < 0 or index >= len(self.stacks):
            return None
        data = self.stacks[index].pop()
        if len(self.stacks[index]) == 0:
            self.stacks.pop(index)
        return data
    
    def __str__(self):
        return str(self.stacks)
    
s = SetOfStacks(capacity=3)
for i in range(10):
    s.push(i)

print(s)        # [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
print(s.pop())  # 9
print(s.pop_at(1))  # 5
print(s)        # [[0, 1, 2], [3, 4], [6, 7, 8]]
