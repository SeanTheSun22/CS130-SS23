from Queue import Queue
from BinarySearchTree import print_tree
from BinarySearchTree import create_tree_from_nested_list
from BinarySearchTree import BinarySearchTree

def get_list_by_level(bst):
    list = []
    q = Queue()
    q.enqueue(bst)
    while not q.is_empty():
        current = q.dequeue()
        list.append(current.get_data())
        if current.get_left() is not None:
            q.enqueue(current.get_left())
        if current.get_right() is not None:
            q.enqueue(current.get_right())
    return list








tree3 = create_tree_from_nested_list([8, [3, [1, None, None], [6, [4, None, None],
                [7, None, None]]], [10, None, [14, [13, None, None], None]]])
print_tree(tree3, 0)

print(get_list_by_level(tree3))