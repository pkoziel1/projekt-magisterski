from collections import defaultdict
from typing import List, Iterable, Dict, Optional, Tuple
import matplotlib.pyplot as plt
from networkx import Graph
import networkx as nx
from networkx.classes.reportviews import EdgeDataView


class KozikGraph:
    def __init__(self, graph: Graph):
        self.graph = graph
        # community -> list of nodes
        self.communities: Dict[int: List[int]] = defaultdict(list)
        print("stop")

    def get_nodes(self) -> Iterable[int]:
        return self.graph.nodes

    def get_weight(self, u: int, v: int) -> int:
        return self.graph.get_edge_data(u, v)['weight']

    def get_edges_weight_sum(self, edges: Iterable[Tuple[int, int]]) -> int:
        return sum([self.get_weight(*edge) for edge in edges])

    def get_edges_incident_to(self, u: int) -> EdgeDataView:
        return self.graph.edges(u)

    def get_all_edges(self) -> EdgeDataView:
        return self.graph.edges()

    def get_neighbours(self, u: int) -> Iterable[int]:
        return self.graph.neighbors(u)

    def get_edges_incident_to_node_weight_sum(self, u: int) -> int:
        edges = self.get_edges_incident_to(u)
        return self.get_edges_weight_sum(edges)

    def get_all_edges_weight_sum(self) -> int:
        return self.get_edges_weight_sum(self.get_all_edges())

    # =========================== COMMUNITY
    def get_node_community(self, u: int) -> Optional[int]:
        for community, nodes in self.communities.items():
            if u in nodes:
                return community
        return None

    def get_community_nodes(self, community: int) -> List[int]:
        return self.communities[community]

    def add_to_community(self, community: int, u: int):
        self.delete_from_community(u)
        self.communities[community].append(u)

    def delete_from_community(self, u: int):
        community = self.get_node_community(u)
        if community is not None:
            self.communities[community].pop(self.communities[community].index(u))

    def get_edges_inside_community_weight_sum(self, community: int) -> int:
        return self.get_edges_weight_sum(self.get_edges_inside_community(community))

    def get_edges_incident_to_community_weight_sum(self, community: int) -> int:
        return self.get_edges_weight_sum(self.get_edges_incident_to_community(community))

    def get_edges_inside_community(self, community: int) -> List[Tuple[int, int]]:
        community_nodes = self.get_community_nodes(community)
        return [
            edge
            for node in community_nodes
            for edge in self.get_edges_incident_to(node)
            if edge[0] in community_nodes and edge[1] in community_nodes
        ]

    def get_edges_incident_to_community(self, community: int) -> List[Tuple[int, int]]:
        community_nodes = self.get_community_nodes(community)
        return [
            edge
            for node in community_nodes
            for edge in self.get_edges_incident_to(node)
        ]

    def get_edges_in_community_incident_to_node_weight_sum(self, u: int, community: int):
        community_nodes = self.get_community_nodes(community)
        edges = [edge for edge in self.get_edges_incident_to(u)
                 if edge[0] in community_nodes or edge[1] in community_nodes]
        return self.get_edges_weight_sum(edges)

    # =========================== UTILS

    @classmethod
    def load_karate_graph(cls):
        G = nx.karate_club_graph()
        return cls(graph=G)


def generate_child_kozik_graph(kozik_graph: KozikGraph) -> KozikGraph:
    # create new nodes and edges....
    G = nx.Graph()
    new_nodes = [community for community, members in kozik_graph.communities.items() if members]
    G.add_nodes_from(new_nodes)

    new_edges = []
    for community in new_nodes:
        # ...
        # ...
        # ...
        new_edge = ...
        new_edges.append(new_edge)

    # ..
    # ..
    return KozikGraph(graph=G)
