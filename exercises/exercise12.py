
# Output of this Python program?
import copy

a = [[0]]
c1 = a
c2 = a[:]
c3 = list(a)
c4 = a.copy()
c5 = copy.copy(a)
c6 = copy.deepcopy(a)

c1[0].append(1)
c2[0].append(2)
c3[0].append(3)
c4[0].append(4)
c5[0].append(5)
c6[0].append(6)

print(a)
# --- possible answers ---
# A) [[0]]
# B) [[0, 1]]
# C) [[0, 1, 2, 3]]
# D) [[0, 1, 2, 3, 4, 5]]
# E) [[0, 1, 2, 3, 4, 5, 6]]


