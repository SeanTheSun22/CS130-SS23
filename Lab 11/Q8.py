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

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("ERROR: The queue is full.")
        self.back = (self.back + 1) % self.capacity
        self.count += 1
        self.items[self.back] = item

    def dequeue(self):
        if self.is_empty():
            raise IndexError("ERROR: The queue is empty.")
        self.front = (self.front + 1) % self.capacity
        self.count += -1
        return self.items[self.front - 1]

q1 = CircularQueue(3)
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
print(q1)
try:
    q1.enqueue(5)
except IndexError as err:
    print(err)
print(q1.dequeue())
print(q1)
q1.enqueue(5)
print(q1)

q1 = CircularQueue(5)
for index in range(1, 6):
    q1.enqueue(index)
for index in range(1, 7):
    try:
        print(q1.dequeue())
    except IndexError as err:
        print(err)
print(q1)
for index in range(10, 14):
    q1.enqueue(index)
for index in range(10, 12):
    q1.dequeue()
print(q1)
