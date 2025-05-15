import memory_graph as mg
import itertools as it

class Linked_List:

    def __init__(self, value=None, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def add_front(self, value):
        if self.value == None:
            self.value = value 
        elif self.next is None:
            new_node = Linked_List(value)
            self.prev = new_node
            self.next = new_node
        else:
            new_node = Linked_List(value, self.next)
            self.next.next = new_node
            self.next = new_node

linked_list = Linked_List()
for value in range(100):
    linked_list.add_front(value)
