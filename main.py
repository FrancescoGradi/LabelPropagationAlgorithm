import snap
import numpy as np

G = snap.LoadEdgeList(snap.PNGraph, "Wiki-Vote.txt", 0, 1)
print "G5: Nodes %d, Edges %d" % (G.GetNodes(), G.GetEdges())

pi = range(1, G.GetNodes() + 1)
pi = np.random.permutation(pi)

l = range(1, G.GetNodes() + 1)
v = np.ones(G.GetNodes() + 1)

print l
