import networkx.algorithms.community as nx_comm
from fast_unfolding import FastUnfolding
from graph import KozikGraph
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx


def get_bitcoin_graph():
    data = pd.read_csv("soc-sign-bitcoinalpha.csv")
    source_list = list(data['source'])
    target_list = list(data['target'])
    rating_list = list(data['rating'])
    print('m =', sum(rating_list))
    G = nx.DiGraph()
    G.add_nodes_from(list(range(0, max(data['source']))))
    G.add_weighted_edges_from(list(zip(source_list, target_list, rating_list)))
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
    plt.show()
    print(greedy_modularity_communities(G))
    print('stop')
    return G


def ring_graph():
    G = nx.Graph()

    # G.add_nodes_from(range(0, 10))
    G.add_nodes_from(range(0, 150))
    list_of_edges = []
    # for z in range(0, 2):
    for z in range(0, 30):
        for x in range(z*5, z*5+4):
            for y in range(1, 5):
                if x + y > z*5+4:
                    continue
                list_of_edges.append((x, x + y, 1))
        # if z*5+5 < 10:
        if z*5+5 < 150:
            list_of_edges.append((z*5+4, z*5+5, 1))
    list_of_edges.append((0, 149, 1))
    # list_of_edges.append((0, 9, 1))
    G.add_weighted_edges_from(list_of_edges)
    nx.draw_networkx_labels(G, pos=nx.circular_layout(G))
    nx.draw(G, pos=nx.circular_layout(G), node_color='r', edge_color='b')
    plt.show()
    print(nx_comm.greedy_modularity_communities(G))
    print(nx_comm.modularity(G, nx_comm.label_propagation_communities(G)))
    print('stop')
    return G


# graph = KozikGraph.load_karate_graph()
# graph = KozikGraph(graph=get_bitcoin_graph())
graph = KozikGraph(graph=ring_graph())
# graph = KozikGraph(graph=fast_graph())
print('stop')
fast_unfolding = FastUnfolding()

fast_unfolding.process_graph(graph)

print('stoped')
