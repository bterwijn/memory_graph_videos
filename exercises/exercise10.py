
# What is the output of this Python Program?
import copy

class Coord:

    def __init__(self, x, y, z):
        self.c = [x, y, z]

    def __str__(self):
        return str(self.c)[1:-1]

coord = Coord(0, 0, 0)
c1 = coord
c2 = copy.copy(coord)
c3 = copy.deepcopy(coord)
c1.c[0] = 1
c2.c[1] = 2
c3.c[2] = 3

print(coord)
# --- possible answers ---
# A) 0, 0, 0
# B) 1, 0, 0
# C) 1, 2, 0
# D) 1, 2, 3

