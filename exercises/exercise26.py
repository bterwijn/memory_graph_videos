
# Output of this Python Program?
a = {1: []}
b = a
b |= {2: []}
b[1].append(100)
b = b | {3: []}
b[2].append(200)
b[3].append(300)

print(a)
# --- possible answers --- 
# A) {1: []}
# B) {1: [100], 2: []}
# C) {1: [100], 2: [200]}
# D) {1: [100], 2: [200], 3: []}
# E) {1: [100], 2: [200], 3: [300]}
