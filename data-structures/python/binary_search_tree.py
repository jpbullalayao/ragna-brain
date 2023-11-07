from bst_node import BSTNode

from queue import Queue
from stack import Stack

class BinarySearchTree:
    def __init__(self):
        self.root = None

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

        stack = Stack()
        values = []

        node = self.root
        while stack.size() > 0 or node:
            if node:
                stack.push(node)
                node = node.left
            else:
                node = stack.pop().val
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

        stack = Stack(self.root)

        while stack.size() > 0:
            node = stack.pop().val
            print(node.val)

            if node.right:
                stack.push(node.right)

            if node.left:
                stack.push(node.left)

 
    def print_postorder(self, node):
        if not node:
            return None
        
        self.print_postorder(node.left)
        self.print_postorder(node.right)
        print(node.val)


    def print_postorder_iterative(self):
        if not self.root:
            return None

        stack = Stack(self.root)
        values = []

        while stack.size() > 0:
            node = stack.pop().val

            values = [node.val] + values
            
            if node.left:
                stack.push(node.left)

            if node.right:
                stack.push(node.right)

        for value in values:
            print(value)


    def print_breadth_first(self):
        if not self.root:
            return None

        queue = Queue(self.root)

        while queue.size() > 0:
            node = queue.dequeue().val

            print(node.val)

            if node.left:
                queue.enqueue(node.left)
            
            if node.right:
                queue.enqueue(node.right)


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
