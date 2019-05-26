import networkx as nx
import numpy as np
import random

import algorithms

# graph_name = 'email-Eu-core'    # Download from: https://snap.stanford.edu/data/
graph_name = 'CA-GrQc'
# graph_name = 'Wiki-Vote'
G = nx.read_edgelist("data/{name}.txt".format(name=graph_name), create_using=nx.DiGraph(), nodetype=int)

labels, v = algorithms.APM_with_analytics(G, gamma=0.1, iterations=1000, graph=graph_name)

print('labels: ' + str(labels))
print('nodes per label: ' + str(list(v)))
print('distribution of the nodes: ' + str({x for x in list(v) if x != 0}))
print('num clusters: ' + str(len([x for x in list(v) if x != 0])))

"""asd = {k: 0 for k in range(80, 88)}
lol = []
for l in asd.keys():
    asd[l] = random.randint(0, 7)
    lol.append(asd[l])

max_index = np.argmax(lol)
max_arg = lol[int(max_index)]
candidates = [k for k, v in asd.items() if v == max_arg]

print(lol)
print(asd)
print(max_arg)
print(candidates)"""
