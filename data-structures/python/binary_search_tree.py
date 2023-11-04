from bst_node import BSTNode

from stack import Stack

#      5
#   2        7
# 1   3    6   8
#
#

# stack: []
# values: 

class BinarySearchTree:
    def __init__(self):
        self.root = None

        self.insert(5)
        self.insert(2, self.root)
        self.insert(7, self.root)
        self.insert(1, self.root)
        self.insert(3, self.root)
        self.insert(6, self.root)
        self.insert(8, self.root)

    # Duplicate values get inserted to right of node
    def insert(self, val, node = None):
        if not node:
            self.root = BSTNode(val)
            return

        if node.val <= val:
            if not node.right:
                node.right = BSTNode(val)

            else:
                self.insert(val, node.right)

        else:
            if not node.left:
                node.left = BSTNode(val)

            else:
                self.insert(val, node.left)


    def print_in_order(self, node):
        if not node:
            return None

        self.print_in_order(node.left)
        print(node.val)
        self.print_in_order(node.right)


    def print_preorder(self, node):
        if not node:
            return None
        
        print(node.val)
        self.print_preorder(node.left)
        self.print_preorder(node.right)
    

    def print_preorder_iterative(self):
        if not self.root:
            return None
        
        values = []
        stack = []

        node = self.root

        stack.insert(0, node)

        while stack:
            node = stack.pop(0)
            values.append(node.val)

            if node.right:
                stack.insert(0, node.right)

            if node.left:
                stack.insert(0, node.left)

        for value in values:
            print(value)

 
    def print_postorder(self, node):
        if not node:
            return None
        
        self.print_postorder(node.left)
        self.print_postorder(node.right)
        print(node.val)


    def find(self, node, val):
        if not node:
            return None
        
        if node.val == val:
            return node

        if node.val < val:
            if not node.right:
                return None

            return self.find(node.right, val)
        else:
            if not node.left:
                return None
