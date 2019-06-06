import numpy as np
import time
import datetime
import copy
import random

def APM_with_analytics(G, gamma=0.1, iterations=10, graph='email-Eu-core'):

    max_iter = True
    # Inizializzazione vettori labels, pi e v
    n = G.number_of_nodes()
    numEdges = G.number_of_edges()

    labels = {x: 1 for x in G.nodes()}    # We set lambda as the identity function and also initialize v as a value
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
            iter_changes = 0
            for i in labels.keys():
                lCandidates = []
                for l in labels.keys():
                    k[l] = len({l}.intersection({x for x in G.neighbors(pi[i])}))
                    #lCandidates.append(k[l])
                    lCandidates.append(k[l] - gamma * (labels[l] - k[l]))

                max_index = np.argmax(lCandidates)
                max_value = lCandidates[int(max_index)]
                candidates = {key for key, v in k.items() if v == max_value}
                if len(candidates) is not 0:
                    l_ = random.choice(tuple(candidates))
                else:
                    l_ = random.choice([x for x in labels.keys()])
                labels[pi[i]] -= 1
                if pi[i] != l_:
                    iter_changes += 1
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
            if np.array_equal(v, v_previous) or iter_changes < 4:
                print('Maximum found, stopping the algorithm.')
                f.write('Maximum found, stopping the algorithm.\n')
                max_iter = False
                break
            v_previous = copy.deepcopy(v)
        if max_iter:
            print('Maximum number of iteration reached, stopping the algorithm.')
            f.write('Maximum number of iteration reached, stopping the algorithm.\n')
        print('num clusters: ' + str(len([x for x in list(v) if x != 0])))
        f.write('# nodes | # clusters: ' + str({x: sum(1 for y in list(v) if x == y) for x in list(v) if x != 0}) + "\n")
        f.write('num clusters: ' + str(len([x for x in list(v) if x != 0])) + "\n")
        print('Total running time: {x} minutes and {y} seconds.'.format(x=int(sum(running_time) / 60),
                                                                        y=(int(sum(running_time) % 60))))
        f.write('Total running time: {x} minutes and {y} seconds.\n'.format(x=int(sum(running_time) / 60),
                                                                            y=(int(sum(running_time) % 60))))

    return labels, v


def APM(G, gamma=0.1, iterations=10):
    # Inizializzazione vettori labels, pi e v

    labels = {x: 1 for x in G.nodes()}  # We set lambda as the identity function and also initialize v as a value
    print(labels)
    perm = [x for x in labels.keys()]
    random.shuffle(perm)
    pi = {perm[i]: list(labels.keys())[i] for i in range(len(labels.keys()))}
    print(pi)

    k = {x: 0 for x in labels.keys()}
    v_previous = []

    l_ = 0

    running_time = []

    for iter in range(iterations):
        print('Starting iteration {x}.'.format(x=iter + 1))
        start = time.clock()
        iter_changes = 0
        for i in labels.keys():
            lCandidates = []
            for l in labels.keys():
                k[l] = len({l}.intersection({x for x in G.neighbors(pi[i])}))
                lCandidates.append(k[l] - gamma * (labels[l] - k[l]))

            max_index = np.argmax(lCandidates)
            max_value = lCandidates[int(max_index)]
            candidates = {key for key, v in k.items() if v == max_value}
            if len(candidates) is not 0:
                l_ = random.choice(tuple(candidates))
            else:
                l_ = random.choice([x for x in labels.keys()])
            labels[pi[i]] -= 1
            if pi[i] != l_:
                iter_changes += 1
            pi[i] = l_
            labels[pi[i]] += 1
        end = time.clock()
        running_time.append(end - start)
        v = [labels[i] for i in labels.keys()]
        print('Number of nodes per label:')
        print(v)
        print('Iteration {x} ended. Elapsed time: {time} seconds.'.format(x=iter + 1, time=round(end - start, 2)))
        if np.array_equal(v, v_previous) or iter_changes < 4:
            print('Maximum found, stopping the algorithm.')
            break
        v_previous = copy.deepcopy(v)


    return labels, v
