
# Output of this Python program?
import copy

def fun(c1, c2, c3):
    c1.append(1)
    c2.append(2)
    c3.append(3)

a = [[0]]
c1 = a
c2 = a.copy()
c3 = copy.deepcopy(a)

fun(c1[0], c2[0], c3[0])
fun(c1   , c2   , c3   )

print(a)
# --- possible answers ---
# A) [[0, 1], 1]
# B) [[0, 1, 2], 1]
# C) [[0, 1, 2], 1, 2]
# D) [[0, 1, 2, 3], 1, 2]
