
# Output of this Python Program?
a = [1, 2]
b = a
b += [3, 4]
b.extend([5, 6])
b = b + [7, 8]
b.insert(9, 10)

print(a)
# --- possible answers ---
# A) [1, 2]
# B) [1, 2, 3, 4]
# C) [1, 2, 3, 4, 5, 6]
# D) [1, 2, 3, 4, 5, 6, 7, 8]
# E) [1, 2, 3, 4, 5, 6, 7, 8, 10]
