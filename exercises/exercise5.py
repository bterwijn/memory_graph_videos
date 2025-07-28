import memory_graph as mg

a = ([1], [2])
b = a
b[0].append(11)
b += ([3],)
b[1].append(22)
b[2].append(33)

print(a)
