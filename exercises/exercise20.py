
# Output of this Python program?
a = [1]
try:
    b = a
    b += [2]
    b += (3,)
    b.append(4)
    b.extend([5])
    b.extend((6,))
    b[len(b):] = [7]
    b = b + [8]
except Exception:
    pass

print(a)
# --- possible answers ---
# A) [1]
# B) [1, 2]
# C) [1, 2, 3, 4, 5, 6, 7]
# D) [1, 2, 3, 4, 5, 6, 7, 8]
# E) None of the above
