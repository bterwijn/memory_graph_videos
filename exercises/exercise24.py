
# Output of this Python Program?
class Value:
    def __init__(self, value):
        self.set(value)
    def set(self, value):
        self.value = value
        
v1 = Value(1)
v2 = Value(2)
a = {v1, }
print(v1 in a, end=' ')
v2.set(1)
print(v2 in a, end=' ')
v1.set(2)
print(v1 in a, end=' ')

# --- possible answers ---
# A) TypeError: unhashable type: 'Value'
# B) True False False
# C) True True False
# D) True False True
