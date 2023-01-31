class CircularQueue:
    def __init__(self, capacity = 8):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.back = capacity - 1
        self.count = 0

    def __str__(self):
        list = [self.items[i % self.capacity] for i in range(self.front + self.count - 1, self.front - 1, -1)]
        for i in range(self.count):
            if type(list[i]) == str:
                list[i] = f"'{list[i]}'"
            else:
                list[i] = str(list[i])
        
        return "-> |" + ", ".join(list) + "| ->"

    def is_full(self):
        return self.count == self.capacity
    def is_empty(self):
        return self.count == 0

q = CircularQueue(3)
print(q)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
q.enqueue(4)
print(q)
print(q.is_full())
q.clear()
print(q.is_empty())

q = CircularQueue(3)
q.enqueue(1)
q.dequeue()
q.enqueue(2)
q.dequeue()
q.enqueue(3)
q.enqueue(4)
print(q)
print(q.is_empty())
print(q.is_full())