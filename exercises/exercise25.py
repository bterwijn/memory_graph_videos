
# Output of this Python Program?
import copy

a = {0: [{0}]}
c1 = a
c2 = a.copy()
c3 = copy.copy(a)
c4 = {k:v.copy() for k,v in a.items()}
c5 = copy.deepcopy(a)

c1[0][0].add(1)
c2[0][0].add(2)
c3[0][0].add(3)
c4[0][0].add(4)
c5[0][0].add(5)

print(a)
# --- possible answers --- 
# A) {0: [{0}]}
# B) {0: [{0, 1}]}
# C) {0: [{0, 1, 2}]}
# D) {0: [{0, 1, 2, 3}]}
# E) {0: [{0, 1, 2, 3, 4}]}
# F) {0: [{0, 1, 2, 3, 4, 5}]}

