class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert_left(self, new_data):
        if self.left == None:
            self.left = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data, left=self.left)
            self.left = t

    def insert_right(self, new_data):
        if self.right == None:
            self.right = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data, right=self.right)
            self.right = t

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def is_full_node(self):
        if (self.left is None) ^ (self.right is None):
            return False
        return True

b_tree = BinaryTree(0)
print(b_tree.is_full_node())

b_tree1 = BinaryTree('python')
print(b_tree1.is_full_node())
b_tree1.set_left(BinaryTree('anaconda'))
print(b_tree1.is_full_node())
b_tree1.set_right(BinaryTree('weka'))
print(b_tree1.is_full_node())