import networkx
import numpy as np

def APM(G, gamma=0.1, iterations=1):

    # Inizializzazione vettori labels, pi e v
    n = G.number_of_nodes()

    labels = list(range(n))

    pi = list(range(n))
    pi = np.random.permutation(pi)

    v = np.ones(n)
    k = np.zeros(n)

    # implementazione senza array di permutazione pi, ma direttamente con i
    l_ = 0

    for iter in range(iterations):
        for i in range(n):

            lCandidates = np.full(n, -1)
            for l in range(len(labels)):
                k[l] = len(list(x for x in list(G.neighbors(i)) if labels[x] == labels[l]))
                lCandidates[l] = k[l] - gamma * (v[l] - k[l])

            l_ = np.argmax(lCandidates)

            v[labels[i]] -= 1
            labels[i] = l_
            v[labels[i]] += 1

    return labels, v