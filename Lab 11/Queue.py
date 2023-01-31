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