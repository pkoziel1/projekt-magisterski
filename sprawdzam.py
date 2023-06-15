import math
import time
import networkx.algorithms.community as nx_comm
from fast_unfolding import FastUnfolding
from graph import KozikGraph
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx


def get_bitcoin_graph():
    data = pd.read_csv("soc-sign-bitcoinalpha.csv")
    source_list = list(data['source']-1)
    target_list = list(data['target']-1)
    rating_list = list(data['rating'])
    G = nx.Graph()
    myList = []
    for number in source_list:
        if number not in myList:
            myList.append(number)
    for number in target_list:
        if number not in myList:
            myList.append(number)
    G.add_nodes_from(list(range(0, max(data['source']))))
    G.add_weighted_edges_from(list(zip(source_list, target_list, rating_list)))
    nx.draw_networkx_labels(G, pos=nx.circular_layout(G))
    nx.draw(G, pos=nx.circular_layout(G), node_color='r', edge_color='b')
    print('stop')
    return G


def fast_graph():
    G = nx.Graph()
    G.add_nodes_from(range(0, 16))
    G.add_weighted_edges_from([(0, 2, 1), (0, 3, 1), (0, 4, 1), (0, 5, 1), (1, 2, 1), (1, 4, 1), (1, 7, 1),
                               (2, 4, 1), (2, 5, 1), (2, 6, 1), (3, 7, 1), (4, 10, 1), (5, 7, 1), (5, 11, 1),
                               (6, 7, 1), (6, 11, 1), (8, 9, 1), (8, 10, 1), (8, 11, 1), (8, 14, 1),
                               (8, 15, 1), (9, 12, 1), (9, 14, 1), (10, 11, 1), (10, 12, 1), (10, 13, 1),
                               (10, 14, 1), (11, 13, 1)])
    nx.draw_networkx_labels(G, pos=nx.circular_layout(G))
    nx.draw(G, pos=nx.circular_layout(G), node_color='r', edge_color='b')
    mod = nx_comm.modularity(G, nx_comm.greedy_modularity_communities(G))
    c = nx_comm.greedy_modularity_communities(G)
    print(f'NetX mod: {mod}')
    return G


def ring_graph():
    G = nx.Graph()
    G.add_nodes_from(range(0, 150))
    list_of_edges = []
    for z in range(0, 30):
        for x in range(z*5, z*5+4):
            for y in range(1, 5):
                if x + y > z*5+4:
                    continue
                list_of_edges.append((x, x + y, 1))
        if z*5+5 < 150:
            list_of_edges.append((z*5+4, z*5+5, 1))
    list_of_edges.append((0, 149, 1))
    G.add_weighted_edges_from(list_of_edges)
    nx.draw_networkx_labels(G, pos=nx.circular_layout(G))
    nx.draw(G, pos=nx.circular_layout(G), node_color='r', edge_color='b')

    print(math.ceil((time.perf_counter_ns() - startpoint) / 1000000))
    print("^ before greedy algorithm")

    mod = nx_comm.modularity(G, nx_comm.greedy_modularity_communities(G))

    print(math.ceil((time.perf_counter_ns() - startpoint) / 1000000))
    print("^ after greedy algorithm")

    print(f'NetX mod: {mod}')

    print(math.ceil((time.perf_counter_ns() - startpoint) / 1000000))
    print("^ before louvain algorithm")

    mod2 = nx_comm.modularity(G, nx_comm.louvain_communities(G))

    print(math.ceil((time.perf_counter_ns() - startpoint) / 1000000))
    print("^ after louvain algorithm")

    print(f'NetX mod: {mod2}')
    return G


def ring_graph_after_1_step():
    G = nx.Graph()
    G.add_nodes_from(range(0, 30))
    list_of_edges = []
    list_of_edges.append((0,29,1))
    for node in range(0, 30):
        list_of_edges.append((node,node,10))
        if node+1 > 29:
            break
        list_of_edges.append((node, node+1, 1))
    G.add_weighted_edges_from(list_of_edges)
    nx.draw_networkx_labels(G, pos=nx.circular_layout(G))
    nx.draw(G, pos=nx.circular_layout(G), node_color='r', edge_color='b')
    mod = nx_comm.modularity(G, nx_comm.greedy_modularity_communities(G))
    c = nx_comm.greedy_modularity_communities(G)
    print(f'NetX mod: {mod}')
    return G


def ring_graph_after_2_step():
    G = nx.Graph()
    G.add_nodes_from(range(0, 15))
    list_of_edges = []
    list_of_edges.append((0,14,1))
    for node in range(0, 15):
        list_of_edges.append((node, node, 21))
        if node+1 > 14:
            break
        list_of_edges.append((node, node+1, 1))
    G.add_weighted_edges_from(list_of_edges)
    nx.draw_networkx_labels(G, pos=nx.circular_layout(G))
    nx.draw(G, pos=nx.circular_layout(G), node_color='r', edge_color='b')
    mod = nx_comm.modularity(G, nx_comm.greedy_modularity_communities(G))

    print(f'NetX mod: {mod}')

    return G


def karate_graph():
    G = nx.karate_club_graph()
    nx.draw_networkx_labels(G, pos=nx.circular_layout(G))
    nx.draw(G, pos=nx.circular_layout(G), node_color='r', edge_color='b')

    print(math.ceil((time.perf_counter_ns() - startpoint) / 1000000))
    print("^ before greedy algorithm")

    mod = nx_comm.modularity(G, nx_comm.greedy_modularity_communities(G))

    print(math.ceil((time.perf_counter_ns() - startpoint) / 1000000))
    print("^ after greedy algorithm")

    print(f'NetX mod: {mod}')

    print(math.ceil((time.perf_counter_ns() - startpoint) / 1000000))
    print("^ before louvain algorithm")

    mod2 = nx_comm.modularity(G, nx_comm.louvain_communities(G))

    print(math.ceil((time.perf_counter_ns() - startpoint) / 1000000))
    print("^ after louvain algorithm")

    print(f'NetX mod: {mod2}')
    return G


def florentine_families_graph():
    G = nx.florentine_families_graph()
    mapping = {old_name: idx for idx, old_name in enumerate(G.nodes())}
    for u, v, d in G.edges(data=True):
        d['weight'] = 1
    G = nx.relabel_nodes(G, mapping)
    nx.draw_networkx_labels(G, pos=nx.circular_layout(G))
    nx.draw(G, pos=nx.circular_layout(G), node_color='r', edge_color='b')

    mod = nx_comm.modularity(G, nx_comm.greedy_modularity_communities(G))
    print(f'NetX mod: {mod}')
    return G


def small_graph():
    G = nx.Graph()
    G.add_nodes_from(range(0, 7))
    G.add_weighted_edges_from([(0, 0, 1), (0, 1, 1), (0, 2, 2), (0, 3, 1), (0, 5, 1),
                               (1, 1, 1), (1, 4, 2), (2, 2, 1), (2, 4, 1), (2, 6, 1),
                               (3, 3, 1), (4, 4, 3), (4, 6, 1), (5, 5, 1), (5, 6, 1), (6, 6, 1)])
    nx.draw_networkx_labels(G, pos=nx.circular_layout(G))
    nx.draw(G, pos=nx.circular_layout(G), node_color='r', edge_color='b')
    mod = nx_comm.modularity(G, nx_comm.greedy_modularity_communities(G))
    print(f'NetX mod: {mod}')
    return G


# graph = KozikGraph(graph=fast_graph())
# graph = KozikGraph(graph=small_graph())
# graph = KozikGraph(graph=karate_graph())
# graph = KozikGraph(graph=florentine_families_graph())
# graph = KozikGraph(graph=get_bitcoin_graph())
# graph = KozikGraph(graph=ring_graph())
# graph = KozikGraph(graph=ring_graph_after_1_step())
# graph = KozikGraph(graph=ring_graph_after_2_step())

print("startpoint = 0")
startpoint = time.perf_counter_ns()

graph = KozikGraph(graph=karate_graph())

fast_unfolding = FastUnfolding()

print(math.ceil((time.perf_counter_ns() - startpoint)/1000000))
print("^ before fast_unfolding")

fast_unfolding.run(graph)

print(math.ceil((time.perf_counter_ns() - startpoint)/1000000))
print("^ after fast_unfolding")

plt.show()
