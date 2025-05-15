import memory_graph as mg
import random

class BinTree:

    def __init__(self, value=None, smaller=None, larger=None):
        self.smaller = smaller
        self.value = value
        self.larger = larger

    def add(self, value):
        if self.value is None:
            self.value = value
        elif value < self.value:
            if self.smaller is None:
                self.smaller = BinTree(value)
            else:
                self.smaller.add(value)
        else:
            if self.larger is None:
                self.larger = BinTree(value)
            else:
                self.larger.add(value)

tree = BinTree()
while True
    value = random.randrange(100)
    tree.add(value)
