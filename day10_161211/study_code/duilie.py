import queue

q = queue.PriorityQueue()

q.put([2, "lili2"])
q.put([3, "lili3"])
q.put([1, "zewei1"])
q.put([4, "lili4"])
q.put([5, "lili5"])

print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
