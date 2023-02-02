from BinaryTree import BinaryTree

def is_full(my_tree):
    if (my_tree.get_left() is None) ^ (my_tree.get_right() is None):
        return False
    if my_tree.get_left() is not None:
        is_left_full = is_full(my_tree.get_left())
    else:
        is_left_full = True
    if my_tree.get_right() is not None:
        is_right_full = is_full(my_tree.get_right())
    else:
        is_right_full = True
    return is_left_full and is_right_full

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
tree1 = tree.get_left()
tree1.insert_right(69)

tree2 = tree.get_right()
tree2.insert_left(420)
'''
tree2 = tree.get_right().get_right().get_right()
tree2.insert_left(12)
'''

print_tree(tree, 0)

print(is_full(tree))
