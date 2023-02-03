from Node import Node

def get_sum_odd(a_node):
    if not a_node:
        return 0
    if a_node.is_odd():
        return a_node.data + get_sum_odd(a_node.next)
    return get_sum_odd(a_node.next)

node1 = Node(1)
node1.add_after(2)
node1.get_next().add_after(3)
node1.get_next().add_after(4)
print(get_sum_odd(node1))

node1 = Node(2)
node1.multi_add([4, 6, 8, 10, 12])
print(get_sum_odd(node1))