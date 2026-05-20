# What is the output of this program?
a = {1:[], 2:[]}
b = a
b[1].append(11)
b = b.copy()
b[2].append(22)
b[3] = [33]

print(a)
# --- possible answers ---
# A) [[0], [1], [2]]
# B) [[0], [1, 11], [2]]
# C) [[0], [1, 11], [2, 22]]
# D) [[0], [1, 11], [2, 22], [3]]
# E) [[0], [1, 11], [2, 22], [3, 33]]
# see "Solution" for correct answer
