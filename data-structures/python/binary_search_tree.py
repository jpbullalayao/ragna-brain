from bst_node import BSTNode

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Duplicate values get inserted to right of node
    def insert(self, node, val):
        if not node:
            self.root = BSTNode(val)
            return

        if node.val <= val:
            if not node.right:
                node.right = BSTNode(val)

            else:
                self.insert(node.right, val)

        else:
            if not node.left:
                node.left = BSTNode(val)

            else:
                self.insert(node.left, val)


    def print_in_order(self, node):
        if not node:
            return

        self.print_in_order(node.left)
        print(node.val)
        self.print_in_order(node.right)


    def print_preorder(self, node):
        if not node:
            return
        
        print(node.val)
        self.print_in_order(node.left)
        self.print_in_order(node.right)
    
 
    def print_postorder(self, node):
        if not node:
            return
        
        self.print_in_order(node.left)
        self.print_in_order(node.right)
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
