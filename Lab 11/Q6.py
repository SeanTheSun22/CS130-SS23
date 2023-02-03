class CircularQueue:
    def __init__(self, capacity = 8):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.back = capacity - 1
        self.count = 0

q1 = CircularQueue()
print(q1.capacity)
print(q1.items)
print(q1.front)
print(q1.back)
print(q1.count)
print(type(q1))

q1 = CircularQueue(5)
print(q1.capacity)
print(q1.items)
print(q1.front)
print(q1.back)
print(q1.count)