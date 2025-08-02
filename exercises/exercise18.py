
# Output of this Python program?
a = [[1], [2]]
b = a
b[0].append(11)
b = b + [[3]]
b[1].append(22)
b[2].append(33)

print(a)
# --- possible answers ---
# A) [[1], [2]]
# B) [[1, 11], [2]]
# C) [[1, 11], [2, 22]]
# D) [[1, 11], [2, 22], [3, 33]]
