class ThreeStackFixed:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.array = [0]*(stack_size*3)
        self.stack_sizes = [0]*3
    
    def push(self, stack_num, data):
        if self.isfull(stack_num):
            return f"Stack {stack_num} is full"
        
        top_index = self.top_index(stack_num)
        self.array[top_index + 1] = data
        self.stack_sizes[stack_num] += 1
    
    def pop(self, stack_num):
        if self.isempty(stack_num):
            return f"Stack {stack_num} is empty"
        
        top_index = self.top_index(stack_num)
        data = self.array[top_index]
        self.array[top_index] = 0
        self.stack_sizes[stack_num] -= 1
        return data
    
    def peek(self, stack_num):
        if self.isempty(stack_num):
            return f"Stack {stack_num} is empty"
        
        return self.array[self.top_index(stack_num)]

    def isfull(self, stack_num):
        if self.stack_sizes[stack_num] == self.stack_size:
            return True
    
    def isempty(self, stack_num):
        if self.stack_sizes[stack_num] == 0:
            return True
    
    def top_index(self, stack_num):
        offset = stack_num*self.stack_size
        return offset + self.stack_sizes[stack_num] -1
    
    def __str__(self):
        return "->".join(map(str, self.array))

s = ThreeStackFixed(5)
s.push(0,100)
s.push(1,200)
s.push(2,300)
print(s.peek(0))
print(s.peek(1))
print(s.peek(2))
print(s.pop(1))
print(s.pop(1))
print(s)
