
# Output of this Python program?
import copy

def fun(c1, c2, c3):
    c1 += (1,)
    c2 += (2,)
    c3 += (3,)

a = (0,)
c1 = a
c2 = copy.copy(a)
c3 = copy.deepcopy(a)
fun(c1, c2, c3)

print(a)
# --- possible answers ---
# A) (0,)
# B) (0, 1)
# C) (0, 1, 2)
# D) (0, 1, 2, 3)

