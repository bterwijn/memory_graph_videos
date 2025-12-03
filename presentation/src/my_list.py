import memory_graph as mg

my_list = []
for i in range(10):
    my_list.append(i)
    print(my_list)     # debug print statement
    mg.l()             # debug graph statement (graphs all local variables)
