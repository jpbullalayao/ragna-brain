from node import Node

from interfaces.findable import Findable
from interfaces.printable import Printable

class LinkedList(Findable, Printable):
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
            return
        
        self.tail.next = node
        self.tail = self.tail.next

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
