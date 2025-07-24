
# Output of this Python program?
import copy

def fun(c1, c2, c3, c4):
    c1[0].append(1)
    c2[0].append(2)
    c3[0].append(3)
    c4[0].append(4)

mylist = [[]]
c1 = mylist
c2 = mylist.copy()
c3 = copy.copy(mylist)
c4 = copy.deepcopy(mylist)
fun(c1, c2, c3, c4)

print(mylist)
# --- possible answers ---
# A) [[1]]
# B) [[1, 2]]
# C) [[1, 2, 3]]
# D) [[1, 2, 3, 4]]

