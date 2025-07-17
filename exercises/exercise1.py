import memory_graph as mg
import copy

mydict = {'a': [100], 'b': [200], 'c': [300]}
c1 = mydict
c2 = mydict.copy()
c3 = copy.deepcopy(mydict)
c1['a'].append(111)
c2['b'].append(222)
c3['c'].append(333)

print(mydict)






















