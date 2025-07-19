
a = [100, 200, 300]
b = []
b.append(a)
a.append(b)
b.append(b)

print(a[-1][-1][0][1])
