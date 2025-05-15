import memory_graph as mg
import random

class Bin_Tree:

    def __init__(self, value=None, smaller=None, larger=None):
        self.smaller = smaller
        self.value = value
        self.larger = larger

    def add(self, value):
        if self.value is None:
            self.value = value
        elif value < self.value:
            if self.smaller is None:
                self.smaller = Bin_Tree(value)
            else:
                self.smaller.add(value)
        else:
            if self.larger is None:
                self.larger = Bin_Tree(value)
            else:
                self.larger.add(value)

bin_tree = Bin_Tree()
for i in range(100):
    value = random.randrange(100)
    bin_tree.add(value)
