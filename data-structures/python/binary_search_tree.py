from bst_node import BSTNode

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


    def print_in_order_iterative(self):        
        if not self.root:
            return None

        stack = []
        values = []

        node = self.root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                values.append(node.val)
                node = node.right

        for value in values:
            print(value)


    def print_preorder(self, node):
        if not node:
            return None
        
        print(node.val)
        self.print_preorder(node.left)
        self.print_preorder(node.right)
    

    def print_preorder_iterative(self):
        if not self.root:
            return None
        
        stack = [self.root]

        while stack:
            node = stack.pop()
            print(node.val)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

 
    def print_postorder(self, node):
        if not node:
            return None
        
        self.print_postorder(node.left)
        self.print_postorder(node.right)
        print(node.val)


    def print_postorder_iterative(self):
        if not self.root:
            return None
        
        stack = [self.root]
        values = []

        while stack:
            node = stack.pop()

            values = [node.val] + values
            
            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        for value in values:
            print(value)


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
