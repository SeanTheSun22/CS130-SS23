from BinaryTree import BinaryTree

def get_node_depth(tree, target_value):
    if tree is None:
        return -1
    if tree.get_data() == target_value:
        return 0
    left_node_depth = get_node_depth(tree.get_left(), target_value)
    right_node_depth = get_node_depth(tree.get_right(), target_value)
    node_depth = max(left_node_depth, right_node_depth)
    if node_depth == -1:
        return -1
    return node_depth + 1

def print_tree(tree, level):
    print(' ' * (level*4) + str(tree.get_data())) 
    if tree.get_left() != None:
        print('(L)', end = '')
        print_tree(tree.get_left(), level + 1) 
    if tree.get_right() != None: 
        print('(R)', end = '')
        print_tree(tree.get_right(), level + 1)

tree = BinaryTree(10)
tree.insert_left(40)
tree.insert_left(21)
tree.insert_right(13)
tree.insert_right(11)
tree.insert_right(42)
tree.insert_right(31)
tree1 = tree.get_left()
tree1.insert_right(69)
tree2 = tree.get_right().get_right().get_right()
tree2.insert_left(12)
print_tree(tree, 0)
print(get_node_depth(tree, 12))