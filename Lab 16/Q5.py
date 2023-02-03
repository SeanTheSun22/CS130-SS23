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

    def get_multiple_of_number(self, number):
        if self.data % number == 0:
            return self.data
        return 0

b_tree1 = BinaryTree(1)
b_tree2 = BinaryTree(3)
b_tree3 = BinaryTree(99)
print(b_tree1.get_multiple_of_number(2))
print(b_tree2.get_multiple_of_number(3))
print(b_tree3.get_multiple_of_number(11))

b_tree1 = BinaryTree(17)
b_tree2 = BinaryTree(15)
b_tree3 = BinaryTree(919)
print(b_tree1.get_multiple_of_number(10))
print(b_tree2.get_multiple_of_number(5))
print(b_tree3.get_multiple_of_number(100))