
# Output of this Python program?
tuple1  = (100, 200)
tuple2  = tuple1
tuple2 += (300,)

list1   = [100, 200]
list2   = list1
list2  += [300]

print(tuple1[-1], list1[-1])
# --- possible answers ---
# A) 200 200
# B) 200 300
# C) 300 200
# D) 300 300