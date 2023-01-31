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

a_node = Node('hello')
a_node.add_after('world')
a_node.multi_add(['a', 'b'])
current = a_node.get_next()
if not isinstance(current, Node):
    print("current must be an object of the Node class")
print(a_node)
print(current)  
current = current.get_next()
print(current)
current = current.get_next()
print(current)
current = current.get_next()
print(current)

node1 = Node('hello')
node1.multi_add(['a', 'b'])
print(node1)
current = node1.get_next()
print(current)
current = current.get_next()
print(current)
current = current.get_next()
print(current)