from queue import Queue

q = Queue()

q.put(10)
q.put(20)
q.put(30)
q.put(40)

print(q.get())
print(q.get())

print(q.qsize())
print(q.empty())