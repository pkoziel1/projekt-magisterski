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
    G.add_weighted_edges_from([(0, 2, 1), (0, 3, 1), (0, 4, 1), (0, 5, 1), (1, 2, 1), (1, 4, 1), (2, 4, 1),
                               (2, 5, 1), (2, 6, 1), (3, 7, 1), (4, 10, 1), (5, 7, 1), (5, 11, 1),
                               (6, 7, 1), (6, 11, 1), (8, 9, 1), (8, 10, 1), (8, 11, 1), (8, 14, 1),
                               (8, 15, 1), (9, 12, 1), (9, 14, 1), (10, 11, 1), (10, 12, 1), (10, 13, 1),
                               (10, 14, 1), (11, 13, 1)])
    nx.draw_networkx_labels(G, pos=nx.circular_layout(G))
    nx.draw(G, pos=nx.circular_layout(G), node_color='r', edge_color='b')
    plt.show()


graph = KozikGraph.load_karate_graph()
print("stop")
# graph = KozikGraph(graph=get_bitcoin_graph())
# graph = KozikGraph(graph=fast_graph())

fast_unfolding = FastUnfolding()

fast_unfolding.process_graph(graph)

print('stoped')
