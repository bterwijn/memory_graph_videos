# show separate node for float and str
mg.config.embedded_types -= {float, str} 

# Output of this Python program?
float1 = 0.0  ; float2 = float1
str1   = "0"  ; str2   = str1
list1  = [0]  ; list2  = list1
tuple1 = (0,) ; tuple2 = tuple1
set1   = {0}  ; set2   = set1

float2 += 0.1
str2   += "1"
list2  += [1]
tuple2 += (1,)
set2   |= {1}

print(float1, str1, list1, tuple1, set1)
# --- possible answers ---
# A) 0.0 0 [0] (0,) {0}
# B) 0.0 0 [0, 1] (0,) {0, 1}
# C) 0.0 0 [0, 1] (0, 1) {0, 1}
# D) 0.0 01 [0, 1] (0, 1) {0, 1}
# E) 0.1 01 [0, 1] (0, 1) {0, 1}

