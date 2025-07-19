
# What is the output of this Python program?
a = ([10, 11], [20, 21])
b = a
b[0].append(12)
b += ([30, 31],)
b[1].append(22)
b[2].append(32)

print(a)
# --- possible answers ---
# A) ([10, 11], [20, 21])
# B) ([10, 11, 12], [20, 21])
# C) ([10, 11, 12], [20, 21, 22])
# D) ([10, 11, 12], [20, 21, 22], [30, 31, 32])
