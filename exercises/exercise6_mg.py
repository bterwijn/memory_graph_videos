import memory_graph as mg
# show separate nodes for str
mg.config.embedded_types -= {str}

# Output of this Python program?
def fun(a, b, c, d):
    a += "1"
    b += [2]
    c += (3,)
    d |= {4}

a = ""
b = []
c = tuple()
d = set()
fun(a, b, c, d)

print(a, b, c, d)
# --- possible answers ---
# A) 1 [] (3,) {} 
# B) 1 [] () {4}
# C)  [2] (3,) {}
# D)  [2] () {4}
