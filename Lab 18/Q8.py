from BinarySearchTree import print_tree
from BinarySearchTree import create_tree_from_nested_list
from BinarySearchTree import BinarySearchTree

def is_binary_search_tree(my_tree, min_value, max_value):
    if my_tree is None:
        return True
    if my_tree.get_data() > min_value and my_tree.get_data() < max_value:
        left = is_binary_search_tree(my_tree.get_left(), min_value, my_tree.get_data())
        right = is_binary_search_tree(my_tree.get_right(), my_tree.get_data(), max_value)
        return left and right
    return False


tree3 = create_tree_from_nested_list([8, [3, [1, None, None], [6, [4, None, None],
                [7, None, None]]], [10, None, [14, [13, None, None], None]]])
print(is_binary_search_tree(tree3, 0, 100))