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

    

my_stack = Stack()
my_stack.push('a')
my_stack.push('b')
my_stack.push('c')
print(my_stack)
print(my_stack.size())
all_items = my_stack.pop_all()
print(all_items)
print(type(all_items))
print(my_stack.size())

try:
    my_stack = Stack()
    print(my_stack.size())
    print(my_stack)
except IndexError as err:
    print (err)

import random
random.seed(30)
numbers = [random.randint(1, 50) for index in range(10)]
s = Stack()
for num in numbers:
   s.push(num)
print(s)

try:
    my_stack = Stack()
    print(my_stack.size())
    print(my_stack)
    print(my_stack.pop_all())
except IndexError as err:
    print (err)