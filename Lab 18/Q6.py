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
    def delete(self, delete_value):
        if self == None:
            return self
        if self.data > delete_value:
            self.left = self.left.delete(delete_value)
        elif self.data < delete_value:
            self.right = self.right.delete(delete_value)
        else:
            if self.right == None:
                return self.left
            if self.left == None:
                return self.right
            self.data = self.find_in_order_successor().data
            self.right = self.right.delete(self.data)
        return self

def create_tree_from_nested_list(node_list):
    if node_list:
        result = BinarySearchTree(node_list[0])
        left = create_tree_from_nested_list(node_list[1])
        right = create_tree_from_nested_list(node_list[2])
        if left != None:
            result.set_left(left)
        if right != None:
            result.set_right(right)
        return result

def print_tree(tree, level):
    print(' ' * (level*4) + str(tree.get_data())) 
    if tree.get_left() != None:
        print('(L)', end = '')
        print_tree(tree.get_left(), level + 1) 
    if tree.get_right() != None: 
        print('(R)', end = '')
        print_tree(tree.get_right(), level + 1)

tree3 = create_tree_from_nested_list([8, [3, [1, None, None], [6, [4, None, None],
                       [7, None, None]]], [10, None, [14, [13, None, None], None]]])

print_tree(tree3, 0)
tree3.delete(3)
print_tree(tree3, 0)