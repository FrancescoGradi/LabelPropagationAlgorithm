import networkx as nx
import numpy as np

import algorithms

graph_name = 'email-Eu-core'    # Download from: https://snap.stanford.edu/data/
G = nx.read_edgelist("data/{name}.txt".format(name=graph_name), create_using=nx.DiGraph(), nodetype=int)

# Alcuni nodi non ci sono, ci sono nodi isolati, quindi li inserisco manualmente subito
max_node = np.max(G.nodes())
G.add_nodes_from(range(max_node))

labels, v = algorithms.APM_with_analytics(G, gamma=0.1, iterations=5, graph=graph_name)

print(labels)
print(list(v))
