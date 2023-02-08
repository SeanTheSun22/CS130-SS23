class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self, new_data):
        self.data = new_data
    def set_next(self, new_next):
        self.next = new_next
    def add_after(self, value):
        new_node = Node(value,self.next )
        self.next = new_node
    def remove_after(self):
        self.next = self.next.get_next()
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def __iter__(self):
        return LinkedListIterator(self.head)
    def add(self, item): #add to the beginning of the list
        new_node = Node(item, self.head)
        self.head = new_node
        self.size += 1
    def __len__(self):
        return self.size
    def is_empty(self):
        return self.head == None 
    def __str__(self):
        if self.head != None:
            result = "Head: "
            current = self.head
            while current != None:
                result = result + str(current) + " -> "
                current = current.next
            return result + "None"
        else:
            return "Head: "
            
class LinkedListIterator:
    def __init__(self, head):
        self.current = head
    def __next__(self):
        if self.current == None:
            raise StopIteration
        else:
            item = self.current.get_data()
            self.current = self.current.get_next()
            return item
