from collections import deque

stack = deque()
stack.append(10)
stack.append(20)
stack.append(30)
print(stack.pop())

queue = deque()
queue.append(10)
queue.append(20)
queue.append(30)
print(queue.popleft())