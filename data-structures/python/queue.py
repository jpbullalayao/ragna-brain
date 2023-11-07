from node import Node

from interfaces.findable import Findable
from interfaces.printable import Printable
from interfaces.sizable import Sizable

class Queue(Findable, Printable, Sizable):
    def __init__(self, val = None):
        self.head = None
        self.tail = None

        if val:
            self.enqueue(val)


    def enqueue(self, val):
        node = Node(val)

        if not self.head:
            self.head = node
            self.tail = node
            return

        node.next = self.head
        self.head = node


    def dequeue(self):
        temp_node = self.head

        if temp_node == self.tail:
            node_dequeued = temp_node
            self.head = None
            self.tail = None

            return node_dequeued

        while temp_node != None:
            if temp_node.next == self.tail:
                node_dequeued = self.tail
                temp_node.next = None
                self.tail = temp_node

                return node_dequeued
            
            temp_node = temp_node.next


    def find(self, val):
        temp_node = self.head

        while (temp_node != None):
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
