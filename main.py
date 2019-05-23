import networkx as nx
import numpy as np
import _thread

import algorithms
import utils

G = nx.read_edgelist("data/Wiki-Vote.txt", create_using=nx.DiGraph(), nodetype=int)

# Alcuni nodi non ci sono, ci sono nodi isolati, quindi li inserisco manualmente subito
max_node = np.max(G.nodes())
print(max_node)
G.add_nodes_from(range(max_node))

print(G.number_of_nodes())


labels, v = algorithms.APM(G, gamma=0.1, iterations=1)

print(labels)
print(list(v))