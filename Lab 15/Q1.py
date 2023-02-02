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


num_list = [10, 20, 30]
linked_list = LinkedList()
for num in num_list:
	linked_list.add(num)
print(linked_list.size())
linked_list.remove(15)
linked_list.remove(20)
print(linked_list.size())