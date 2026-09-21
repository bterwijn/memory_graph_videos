
# Output of this Python program?
import copy

def custom_copy(a):
    c = a.copy()
    c[1] = a[1].copy()
    c[2] = a[2].copy()
    return c

a = [ [0], [1], [2] ]
b = custom_copy(a)
b[0].append(10)
b[1].append(11)
b[2].append(12)

print(a)
# --- possible answers ---
# A) [[0], [1], [2]]
# B) [[0, 10], [1], [2]]
# C) [[0, 10], [1, 11], [2]]
# D) [[0, 10], [1, 11], [2, 12]]
