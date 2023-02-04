<<<<<<< HEAD
import random
random.seed(30)
for i in range(10):
    print(random.randrange(-5, 5), end = " ")
=======
class BinarySearchTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def get_left(self):
        return self.left
    def get_right(self):
        return self.right
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
    def set_left(self, left):
        self.left = left
    def set_right(self, right):
        self.right = right
    def double_up(self):
        self.data *= 2

def get_bst_inorder(tree):
    if tree is None:
        return []
    left = get_bst_inorder(tree.get_left())
    right = get_bst_inorder(tree.get_right())
    return left + [tree.get_data()] + right
>>>>>>> 327c572 (no message)
