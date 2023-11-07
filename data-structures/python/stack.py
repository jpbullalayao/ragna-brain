from node import Node

from interfaces.findable import Findable
from interfaces.printable import Printable
from interfaces.sizable import Sizable

class Stack(Findable, Printable, Sizable):
    def __init__(self, val = None):
        self.head = None

        if val:
            self.push(val)
    

    def push(self, val):
        node = Node(val)

        if not self.head:
            self.head = node
            return

        node.next = self.head
        self.head = node


    def pop(self):
        if not self.head:
            return None

        node_to_pop = self.head
        self.head = self.head.next

        return node_to_pop


    def find(self, val):
        temp_node = self.head

        while temp_node != None:
            if temp_node.val == val:
                return True
            
            temp_node = temp_node.next
        
        return False


    def print(self):
        temp_node = self.head

        while temp_node != None:
            print(temp_node.val)
            temp_node = temp_node.next


    def size(self):
        length = 0

        temp_node = self.head

        while temp_node != None:
            length += 1
            temp_node = temp_node.next
        
        return length