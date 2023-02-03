class Node:
    def __init__(self, data, next = None):
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

    def __str__(self):
        return str(self.data)

    def add_after(self, data):
        temp = self.next
        self.next = Node(data)
        self.next.next = temp

    def remove_after(self):
        if self.next == None:
            raise IndexError("ERROR: The node is the last of the chain!")
        self.next = self.next.next

    def multi_add(self, a_list):
        current = self
        for i in a_list:
            current.add_after(i)
            current = current.next

    def set_to_capitalised(self):
        self.data = self.data[0].upper() + self.data[1:]

node1 = Node("hello")
print(node1)
node1.set_to_capitalised()
print(node1)