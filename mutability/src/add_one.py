import memory_graph as mg

def add_one(a, b, c):
    mg.block(mg.show, mg.stack())
    a += [1]
    b += (1,)
    c += [1]
    mg.block(mg.show, mg.stack())

a = [4, 3, 2]
b = (4, 3, 2)
c = [4, 3, 2]
add_one(a, b, c.copy())

print(f'{a=}\n{b=}\n{c=}')