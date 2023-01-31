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
    
    

a_node = Node('hello')
a_node.add_after('world')
print(a_node.get_data())
result = a_node.get_next()
print(result.get_data())
if not isinstance(result, Node):
    print("result must be an object of the Node class")
a_node.set_data('happy')
print(a_node.get_data())

node1 = Node('hello')
node2 = Node('world')
node1.set_next(node2)
node1.add_after(123)
print(node1.get_data())
print(node1.get_next().get_data())
print(node1.get_next().get_next().get_data())