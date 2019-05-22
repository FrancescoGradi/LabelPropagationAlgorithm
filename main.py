import networkx as nx
import numpy as np

G = nx.read_edgelist("data/Wiki-Vote.txt", create_using=nx.DiGraph(), nodetype=int)

print(nx.info(G))

pi = range(1, G.number_of_nodes() + 1)
pi = np.random.permutation(pi)

l = range(1, G.number_of_nodes() + 1)
v = np.ones(G.number_of_nodes() + 1)

print(pi)