import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt
import math

import algorithms

graph_name = 'email-Eu-core'    # Download from: https://snap.stanford.edu/data/
# graph_name = 'CA-GrQc'
# graph_name = 'Wiki-Vote'
G = nx.read_edgelist("data/{name}.txt".format(name=graph_name), create_using=nx.DiGraph(), nodetype=int)

labels, v = algorithms.APM_with_analytics(G, gamma=1.6e-18 * (x/5), iterations=1000, graph=graph_name)

print('labels: ' + str(labels))
print('nodes per label: ' + str(list(v)))
print('distribution of the nodes: ' + str({x: sum(1 for y in list(v) if x == y) for x in list(v) if x != 0}))
print('num clusters: ' + str(len([x for x in list(v) if x != 0])))