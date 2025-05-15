import memory_graph as mg
import copy

def custom_copy(a):
    c = a.copy()
    c[1] = a[1].copy()
    return c

a  = [[1,2], ['x', 'y']]
c1 = a
c2 = a.copy()
c3 = custom_copy(a)
c4 = copy.deepcopy(a)
print(f'{c1=} {c2=} {c3=} {c4=}')
