
# Output of this Python program?
import copy

def fun(cs):
    for i, c in enumerate(cs):
        c[0].append(i)

mylist = [[]]
c1 = mylist
c2 = mylist.copy()
c3 = copy.copy(mylist)
c4 = copy.deepcopy(mylist)
fun( (c1, c2, c3, c4) )

print(mylist)
# --- possible answers ---
# A) [[]]
# B) [[0]]
# C) [[0, 1]]
# D) [[0, 1, 2]]
# E) [[0, 1, 2, 3]]

