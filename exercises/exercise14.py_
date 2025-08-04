
# What is the output of this Python program?
def fun(a, b, c, d):
    a += [1, 2]
    b += (1, 2)
    c |= {1, 2}
    d |= {1, 2}

a = [1]
b = (1,)
c = {1}
d = frozenset({1})
fun(a, b, c, d)

print(a, b, c, d)
# --- possible answers ---
# A) [1, 1, 2] (1,) {1, 2} frozenset({1})
# B) [1, 1, 2] (1,) {1, 1, 2} frozenset({1})
# C) [1, 1, 2] (1, 1, 2) {1, 2} frozenset({1, 2})
# D) [1, 1, 2] (1, 1, 2) {1, 1, 2} frozenset({1, 1, 2})

