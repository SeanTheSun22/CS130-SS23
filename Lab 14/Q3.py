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

node1 = Node('hello')
node2 = Node('world')
node1.set_next(node2)
node1.remove_after()
print(node1.get_data())
print(node1.get_next())

node1 = Node('hello')
node2 = Node('world')
node3 = Node('happy')
node4 = Node('coding')
node1.set_next(node2)
node2.set_next(node3)
node3.set_next(node4)
try:
    node4.remove_after()
except IndexError as err:
    print(err)
print(node1.get_data())
print(node1.get_next().get_data())
print(node1.get_next().get_next().get_data())
print(node1.get_next().get_next().get_next().get_data())