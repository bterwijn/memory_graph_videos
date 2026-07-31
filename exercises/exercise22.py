
# Output of this Python Program?
a = {1, 2}
b = a
b.update({3})
b |= {4}
b = b | {5}
b.add(6)

print(a)
# --- possible answers ---
# A) {1, 2}
# B) {1, 2, 3}
# C) {1, 2, 3, 4}
# D) {1, 2, 3, 4, 5}
# E) {1, 2, 3, 4, 5, 6}
