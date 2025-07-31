
# What is the output of this Python Program?
import copy

class Coord:

    def __init__(self, x, y, z):
        self.x = x; self.y = y; self.z = z

    def __str__(self):
        return f'{self.x}, {self.y}, {self.z}'

coord = Coord(0, 0, 0)
c1 = coord
c2 = copy.copy(coord)
c3 = copy.deepcopy(coord)
c1.x = 1
c2.y = 2
c3.z = 3

print(coord)
# --- possible answers ---
# A) 0, 0, 0
# B) 1, 0, 0
# C) 1, 2, 0
# D) 1, 2, 3

