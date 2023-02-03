from BinaryTree import BinaryTree

def replace_0_or_1(tree):
    if tree.get_data() < 0:
        tree.set_data(0)
    else:
        tree.set_data(1)

    if tree.get_left() is not None:
        replace_0_or_1(tree.get_left())
    if tree.get_right() is not None:
        replace_0_or_1(tree.get_right())

def print_tree(tree, level):
    print(' ' * (level*4) + str(tree.get_data())) 
    if tree.get_left() != None:
        print('(L)', end = '')
        print_tree(tree.get_left(), level + 1) 
    if tree.get_right() != None: 
        print('(R)', end = '')
        print_tree(tree.get_right(), level + 1)


binary_tree = BinaryTree(1)
binary_tree.insert_left(-10)
binary_tree.insert_right(4)
replace_0_or_1(binary_tree)
print_tree(binary_tree, 0)