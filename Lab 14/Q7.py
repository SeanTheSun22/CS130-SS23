from Node import Node

def print_node_chain(a_node):
    if not a_node:
        print()
        return
    print(f"{a_node.data} -> ", end = "")
    print_node_chain(a_node.next)
    return


node1 = Node('hello')
node2 = Node('world')
node3 = Node('goodbye')
node1.set_next(node2)
node2.set_next(node3)
print_node_chain(node1)
print("END")

node1 = Node("You")
node1.multi_add(["shall", "not", "pass"])
print_node_chain(node1)
print("END")