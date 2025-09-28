
# What is the output of this program?
import copy

mydict = {1: [], 2: [], 3: []}
c1 = mydict
c2 = mydict.copy()
c3 = copy.deepcopy(mydict)
c1[1].append(100)
c2[2].append(200)
c3[3].append(300)

print(mydict)
# --- possible answers ---
# A) {1: [], 2: [], 3: []}
# B) {1: [100], 2: [], 3: []}
# C) {1: [100], 2: [200], 3: []}
# D) {1: [100], 2: [200], 3: [300]}
# see "Solution" for correct answer





