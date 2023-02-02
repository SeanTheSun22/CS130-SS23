from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        if self.count == 0:
            return True
        return False

    def size(self):
        return self.count

    def add(self, item):
        new_node = Node(item, self.head)
        self.count += 1
        self.head = new_node

    def search(self, item):
        current = self.head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False

    def remove(self, item): 
        found = False
        current = self.head
        previous = None
        while current is not None and not found:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next
        if found:
            self.count += -1
            if previous == None:
                self.head = current.next
            else:
                previous.set_next(current.next)
    
    def __str__(self):
        current = self.head
        if not current:
            return ""
        string = "Head: "
        while current:
            string += f"{current.get_data()} -> "
            current = current.get_next()
        return string + "None"

    def pop(self):
        if self.is_empty():
            raise IndexError("Error: the list is empty!")
        current = self.head
        if current.get_next():
            while current.get_next():
                previous = current
                current = current.get_next()
            previous.next = None
        else:   
            self.head = None
        self.count += -1
        return current.get_data()

    def reverse(self):
        if self.count <= 1:
            return
        next = self.head
        current = next
        previous = None
        while next.get_next():
            next = next.get_next()
            current.next = previous
            previous = current
            current = next
        current.next = previous
        self.head = current

    def add_all(self, a_tuple):
        if len(a_tuple) == 0:
            return
        self.add(a_tuple[0])
        self.add_all(a_tuple[1:])

my_list = LinkedList()
my_list.add_all((1, 2, 3))
print(my_list)
print(type(my_list))

my_list = LinkedList()
my_list.add_all(('apple', 'banana'))
my_list.add(1)
print(my_list)

import random
random.seed(30)
my_list = LinkedList()
numbers = (random.randint(1, 50) for index in range(10))
for num in numbers:
    my_list.add(num)
my_list.add(99)
print(my_list)