import copy

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

    def create_new_circular_queue(self, number):
        temp_queue = copy.deepcopy(self)
        new_queue = CircularQueue(self.capacity + number)
        for i in range(self.count):
            new_queue.enqueue(temp_queue.dequeue())
        return new_queue


my_queue1 = CircularQueue(5)
my_queue1.enqueue(1)
my_queue2 = my_queue1.create_new_circular_queue(5)
print(my_queue2)
print(my_queue2.dequeue())
print(my_queue2)

my_queue1 = CircularQueue(3)
my_queue1.enqueue(1)
my_queue1.enqueue(2)
my_queue1.enqueue(3)
my_queue2 = my_queue1.create_new_circular_queue(0)
print(my_queue2)
print(my_queue2.dequeue())
print(my_queue2)
my_queue2.enqueue(4)
try:
    my_queue2.enqueue(5)
except IndexError as err:
    print(err)
print(my_queue2)

my_queue1 = CircularQueue(2)
my_queue1.enqueue(1)
my_queue1.enqueue(2)
my_queue2 = my_queue1.create_new_circular_queue(3)
print(my_queue2)
my_queue2.enqueue(3)
my_queue2.enqueue(4)
my_queue2.enqueue(5)
print(my_queue2)