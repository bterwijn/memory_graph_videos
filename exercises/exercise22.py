
# Output of this Python Program?
a = {1, 2}
b = a
b.update({3})
b |= {4}
b.union({5})
b = b | {6}
b.add(7)

print(a)
# --- possible answers ---
# A) {1, 2}
# B) {1, 2, 3}
# C) {1, 2, 3, 4}
# D) {1, 2, 3, 4, 5}
# E) {1, 2, 3, 4, 5, 6}
# F) {1, 2, 3, 4, 5, 6, 7}
