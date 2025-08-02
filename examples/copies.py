import memory_graph as mg
import copy

def custom_copy(a):
    c = a.copy()
    c[1] = a[1].copy()
    return c

a = [ [1, 2], [3, 4] ]
c1 = a
c2 = copy.copy(a)
c3 = custom_copy(a)
c4 = copy.deepcopy(a)

a[1][0] = 9999
print(f'{c1=}\n{c2=}\n{c3=}\n{c4=}')

