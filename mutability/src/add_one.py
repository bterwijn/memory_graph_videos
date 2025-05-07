import memory_graph as mg

def add_one(a, b, c):
    a += [1]
    b += (1,)
    c += [1]

a = [4, 3, 2]  # list:    mutable
b = (4, 3, 2)  # tuple: immutable
c = [4, 3, 2]  # list:    mutable
add_one(a, b, c.copy())

print(f'{a=}\n{b=}\n{c=}')