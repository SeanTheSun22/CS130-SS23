from BinaryTree import BinaryTree

def get_sum_multiples_of_number(tree, number):
    sum = 0
    if tree.get_left() is not None:
        sum += get_sum_multiples_of_number(tree.get_left(), number)
    if tree.get_right() is not None:
        sum += get_sum_multiples_of_number(tree.get_right(), number)
    if tree.get_data() % number == 0:
        sum += tree.get_data()
    return sum

def print_tree(tree, level):
    print(' ' * (level*4) + str(tree.get_data())) 
    if tree.get_left() != None:
        print('(L)', end = '')
        print_tree(tree.get_left(), level + 1) 
    if tree.get_right() != None: 
        print('(R)', end = '')
        print_tree(tree.get_right(), level + 1)

tree1 = BinaryTree(3)
tree1.insert_left(2)
tree1.insert_right(6)
print_tree(tree1, 0)
print("The sum is", get_sum_multiples_of_number(tree1, 2))

tree2 = BinaryTree(4)
tree2.insert_left(2)
tree2.insert_right(5)
print_tree(tree2, 0)
print("The sum is", get_sum_multiples_of_number(tree2, 3))