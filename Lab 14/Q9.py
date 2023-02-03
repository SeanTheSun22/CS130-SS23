from Node import Node

def print_node_chain(a_node):
    if not a_node:
        print()
        return
    print(f"{a_node.data} -> ", end = "")
    print_node_chain(a_node.next)
    return

def set_to_capitalised_vowel_list(a_node):
    if a_node == None:
        return ""
    if a_node.data[0] in "aeiou":
        return f"{a_node.data[0].upper()}{a_node.data[1:]} " + set_to_capitalised_vowel_list(a_node.next)
    return f"{a_node.data} " + set_to_capitalised_vowel_list(a_node.next)


node1 = Node("my")
node1.multi_add(["name", "is", "oliver"])
print_node_chain(node1)
print(set_to_capitalised_vowel_list(node1))

node1 = Node("anaconda")
print_node_chain(node1)
print(set_to_capitalised_vowel_list(node1))