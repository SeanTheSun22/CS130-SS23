class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.size() == 0:
            raise IndexError("ERROR: The queue is empty!")
        return self.items.pop()

    def peek(self):
        if self.size() == 0:
            raise IndexError("ERROR: The queue is empty!")
        return self.items[len(self.items)-1]

    def __str__(self):
        return "-> |" + ", ".join(str(item) for item in self.items) + "| ->"
    
    def search(self, item):
        for i in range(self.size() - 1, -1, -1):
            if self.items[i] == item:
                return self.size() - i
        raise ValueError("ERROR: The item is not in the queue.")

my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
print(my_queue)
print(my_queue.search(1))

my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
print(my_queue)
try:
    print(my_queue.search(4))
except ValueError as err:
    print(err)

import random
random.seed(30)
numbers = [random.randint(1, 50) for index in range(10)]
my_queue = Queue()
for num in numbers:
   my_queue.enqueue(num)
print(my_queue)
try:
    print(my_queue.search(50))
except ValueError as err:
    print(err)
try:
    print(my_queue.search(2))
except ValueError as err:
    print(err)