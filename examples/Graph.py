import memory_graph as mg
mg.config.max_graph_depth = 1000
import string
import random

class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def add_edge(self, node):
        self.edges.append(node)

def get_name(i):
    name = ''
    nr_letter = len(string.ascii_lowercase)
    while i > nr_letter - 1:
        i, remainder = divmod(i, nr_letter)
        name = string.ascii_lowercase[remainder] + name
    return string.ascii_lowercase[i] + name

nr_nodes = 20
nodes = [Node(get_name(i)) for i in range(nr_nodes)]

max_nr_edges = 3
for node in nodes:
    for _ in range(random.randint(1, max_nr_edges)):
        node.add_edge(random.choice(nodes))

mg.sl()
