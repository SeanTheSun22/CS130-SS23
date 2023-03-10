class BinarySearchTree:
    def __init__(self, data, left = None, right = None):
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
    def find_in_order_successor(self):
        if self.right is None:
            return self
        current = self.right
        while current.left is not None:
            current = current.left
        return current