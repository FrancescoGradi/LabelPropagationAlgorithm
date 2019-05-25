import networkx as nx
import numpy as np

import algorithms

graph_name = 'email-Eu-core'    # Download from: https://snap.stanford.edu/data/
# graph_name = 'CA-GrQc'
# graph_name = 'Wiki-Vote'
G = nx.read_edgelist("data/{name}.txt".format(name=graph_name), create_using=nx.DiGraph(), nodetype=int)

labels, v = algorithms.APM_with_analytics(G, gamma=- 1/2, iterations=10, graph=graph_name)

"""print(labels)
print(list(v))"""
