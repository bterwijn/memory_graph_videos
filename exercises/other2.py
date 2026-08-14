# Output of this Python Program?
def main():
    o1, o2 = MyClass(1), MyClass(1)
    myset = {o1}
    print(o2 in myset, end=' ')
    o1.set_value(1000)
    print(o1 in myset, end=' ')

class MyClass:
    def __init__(self, v):
        self.v = v
    def set_value(self, v):
        self.v = v

main()

class MyClass:
    def __init__(self, v):
        self.v = v
    def set_value(self, v):
        self.v = v
    def __eq__(self, other):
        return self.v == other.v
    def __hash__(self):
        return hash(self.v)

main()

# --- possible answers ---
# A) TypeError: unhashable type: 'MyClass'
# B) True False False False
# C) True False False True
# E) False True True True
# D) False True True False
