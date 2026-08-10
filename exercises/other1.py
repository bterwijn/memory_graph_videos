
# Output of this Python Program?
class Value:
    def __init__(self, value):
        self.value = value
    def set(self, value):
        self.value = value
        
v1 = Value(1)
v2 = Value(2)
myset = {v1}
print(v1 in myset, end=' ')
v2.set(1)
print(v2 in myset, end=' ')
v1.set(2)
print(v1 in myset, end=' ')

# --- possible answers ---
# A) TypeError: unhashable type: 'Value'
# B) True False False
# C) True True False
# D) True False True
