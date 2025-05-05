import memory_graph as mg

a = [4, 3, 2]
b = a
b += [1]  # equivalent to:  b.append(1)

print(f'{a=}\n{b=}')
