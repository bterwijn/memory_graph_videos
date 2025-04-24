import memory_graph as mg
import copy

a = [ [1, 2], ['x', 'y'] ]
c1 = a
c2 = copy.copy(a)  # equivalent to:  a.copy() a[:] list(a)
c3 = copy.deepcopy(a)

print(f'{c1=}\n{c2=}\n{c3=}')
