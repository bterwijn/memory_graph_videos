

# Output of this Python Program?
a = {1: [11]}
b = a
b[2] = [22]
b[1].append(111)
b = b.copy()
b[3] = [33]
b[2].append(222)
b[3].append(333)

print(a)
# --- possible answers --- 
# A) {1: [11]}
# B) {1: [11], 2: [22]}
# C) {1: [11, 111], 2: [22]}
# D) {1: [11, 111], 2: [22, 222]}
# E) {1: [11, 111], 2: [22, 222], 3: [33, 333]}

