import networkx as nx
import algorithms

G = nx.read_edgelist("data/Wiki-Vote.txt", create_using=nx.DiGraph(), nodetype=int)

# Alcuni nodi non ci sono, ci sono nodi isolati, quindi li inserisco manualmente subito
G.add_nodes_from(range(G.number_of_nodes()))

labels = algorithms.APM(G, gamma=0.1, iterations=1)

print(labels)
