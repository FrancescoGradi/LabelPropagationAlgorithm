import numpy as np
import time
import datetime
import copy
import random

def APM_with_analytics(G, gamma=0.1, iterations=1, graph='email-Eu-core'):

    max_iter = True
    # Inizializzazione vettori labels, pi e v
    n = G.number_of_nodes()
    numEdges = G.number_of_edges()

    labels = {x: 1 for x in G.nodes()}
    print(labels)
    perm = [x for x in labels.keys()]
    random.shuffle(perm)
    pi = {perm[i]: list(labels.keys())[i] for i in range(len(labels.keys()))}
    print(pi)

    k = {x: 0 for x in labels.keys()}
    v_previous = []

    l_ = 0

    running_time = []
    now = datetime.datetime.now()
    if now.time().minute < 10:
        log_file_path = 'logs/log-{date}_{hour}:0{min}.txt'.format(date=now.date(),
                                                                   hour=now.time().hour,
                                                                   min=now.time().minute)
    else:
        log_file_path = 'logs/log-{date}_{hour}:{min}.txt'.format(date=now.date(),
                                                                  hour=now.time().hour,
                                                                  min=now.time().minute)
    with open(log_file_path, 'w+') as f:
        f.write('Run started at {time}    Date: {date}    Num. Iterations: {numIter}\n'.format(time=now.time(),
                                                                                               date=now.date(),
                                                                                               numIter=iterations))
        f.write('Graph: {graph}    (nodes: {nodes}, edges: {edges})\n'.format(graph=graph,
                                                                              nodes=n,
                                                                              edges=numEdges))
        f.write('\n')
        for iter in range(iterations):

            print('Starting iteration {x}.'.format(x=iter + 1))
            start = time.clock()
            for i in labels.keys():

                lCandidates = {x: 0 for x in labels.keys()}
                for l in labels.keys():
                    k[l] = len(list(x for x in list(G.neighbors(pi[i])) if x == l))
                    lCandidates[l] = k[l]
                    #lCandidates[l] = k[l] - gamma * (labels[l] - k[l])

                reverse_lCand = {v: k for k, v in lCandidates.items()}
                candidates_list = [lCandidates[i] for i in lCandidates.keys()]
                l_ = reverse_lCand[candidates_list[int(np.argmax(candidates_list))]]

                labels[pi[i]] -= 1
                pi[i] = l_
                labels[pi[i]] += 1
            end = time.clock()
            running_time.append(end - start)
            v = [labels[i] for i in labels.keys()]
            print('Number of nodes per label:')
            print(v)
            print('Iteration {x} ended. Elapsed time: {time} seconds.'.format(x=iter + 1, time=round(end - start, 2)))

            f.write('Iteration {iter} (gamma: {gamma}):\n'.format(iter=iter + 1, gamma=gamma))
            f.write('Number of nodes per label:\n')
            f.write(str(v) + "\n")
            f.write('Iteration {x} ended. Elapsed time: {time} seconds.\n'.format(x=iter + 1, time=round(end - start, 2)))
            if np.array_equal(v, v_previous):
                print('Maximum found, stopping the algorithm.')
                f.write('Maximum found, stopping the algorithm.\n')
                max_iter = False
                break
            v_previous = copy.deepcopy(v)
        if max_iter:
            print('Maximum number of iteration reached, stopping the algorithm.')
            f.write('Maximum number of iteration reached, stopping the algorithm.')
        print('Total running time: {x} minutes and {y} seconds.'.format(x=int(sum(running_time) / 60),
                                                                        y=(int(sum(running_time) % 60))))
        f.write('Total running time: {x} minutes and {y} seconds.'.format(x=int(sum(running_time) / 60),
                                                                          y=(int(sum(running_time) % 60))))

    return labels, v


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
        if iter % 5 == 0 and iter != 0:
            gamma = gamma / 2

        for i in range(n):

            lCandidates = np.full(n, -1)
            for l in range(len(labels)):
                k[l] = len(list(x for x in list(G.neighbors(pi[i])) if labels[x] == labels[l]))
                lCandidates[l] = k[l]
                # lCandidates[l] = k[l] - gamma * (v[l] - k[l])

            l_ = np.argmax(lCandidates)

            v[labels[pi[i]]] -= 1
            labels[pi[i]] = l_
            v[labels[pi[i]]] += 1

    return labels, v
