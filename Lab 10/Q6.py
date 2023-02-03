class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("ERROR: The stack is empty!")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("ERROR: The stack is empty!")
        return self.items[-1]
        
    def size(self):
        return len(self.items)

    def __str__(self):
        return "[" + ", ".join(repr(item) for item in self.items) + " <-"

    def pop_all(self):
        if self.is_empty():
            raise IndexError("ERROR: The stack is empty!")
        list = []
        while len(self.items) != 0:
            list.append(self.pop())
        return list

    def search(self, item):
        for i in range(1, self.size() + 1):
            if self.items[self.size() - i] == item:
                return i
        raise ValueError("ERROR: The item is not in the stack.")

    def move_to_top(self, item):
        index = self.search(item)
        self.push(self.items.pop(self.size() - index))

my_stack = Stack()
my_stack.push(100)
my_stack.push(101)
my_stack.push(102)
my_stack.push(103)
print(my_stack)
my_stack.move_to_top(100)
print(my_stack)

my_stack = Stack()
my_stack.push(101)
my_stack.push(102)
my_stack.push(103)
print(my_stack)
try:
    print(my_stack.search(100))
except ValueError as err:
    print(err)
print(my_stack)