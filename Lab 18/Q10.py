from BinarySearchTree import BinarySearchTree
from BinarySearchTree import create_tree_from_nested_list

def get_concatenated_words(bst):
    if bst is None:
        return ""
    left = get_concatenated_words(bst.get_left())
    current = bst.get_data()
    right = get_concatenated_words(bst.get_right())
    return left + current + right

tree4 = create_tree_from_nested_list(["h", ["d", ["b", ["a", None, None], ["c", None, None]], None, None], None])
print(get_concatenated_words(tree4))