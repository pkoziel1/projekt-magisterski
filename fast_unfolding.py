from typing import Dict, List, Iterable

import numpy
import networkx as nx
from networkx import Graph
import random

from graph import KozikGraph, generate_child_kozik_graph


class FastUnfolding:
    def __init__(self):
        ...

    def run(self, graph: KozikGraph):
        while True:
            initial_modularity = graph.modularity()
            self.process_graph(graph)
            if graph.modularity() <= initial_modularity:
                break
            graph = generate_child_kozik_graph(graph)
        print(f'Modularity = {graph.modularity()}')

    def process_graph(self, graph: KozikGraph):
        self._assign_init_communities(graph)

        # temp - testing
        # graph.add_to_community(0, 4)
        # graph.add_to_community(0, 3)
        # graph.add_to_community(0, 2)
        # graph.add_to_community(0, 1)

        nodes = [node for node in graph.get_nodes()]
        # random.shuffle(nodes)
        for node in nodes:
            neighbours = graph.get_neighbours(node)
            neighbour_to_gain_map: Dict[int, float] = self.map_modularity_gain_to_neighbours(graph, node, neighbours)
            highest_gain_neighbour = max(neighbour_to_gain_map, key=neighbour_to_gain_map.get)
            print(neighbour_to_gain_map[highest_gain_neighbour])
            if neighbour_to_gain_map[highest_gain_neighbour] > 0: #parametr
                new_community = graph.get_node_community(highest_gain_neighbour)
                graph.add_to_community(new_community, node)
        new_graph = generate_child_kozik_graph(graph)
        print('stop')

    def _assign_init_communities(self, graph: KozikGraph):
        for community, node in enumerate(graph.get_nodes()):
            graph.add_to_community(node, community)

    def map_modularity_gain_to_neighbours(self, graph: KozikGraph, node: int, neighbours: Iterable[int]) -> dict[
        int, float]:
        gain_map = {}
        for neighbour in neighbours:
            neighbour_community = graph.get_node_community(neighbour)
            # if neighbour_community == graph.get_node_community(node):
            #     gain_map[neighbour] = -1
            #     continue

            gain_map[neighbour] = self._calculate_modularity_gain(graph, neighbour_community, node)
        return gain_map

    def _calculate_modularity_gain(self, graph: KozikGraph, community: int, node: int) -> float:
        Ein = graph.get_edges_inside_community_weight_sum(community)
        Etot = graph.get_edges_incident_to_community_weight_sum(community)
        ki = graph.get_edges_incident_to_node_weight_sum(node)
        kin = graph.get_edges_in_community_incident_to_node_weight_sum(node, community)
        m = graph.get_all_edges_weight_sum()
        print('stop')
        return (((Ein + kin) / (2 * m)) - (((Etot + ki) / (2 * m)) ** 2)) - (
                    (Ein / (2 * m)) - ((Etot / (2 * m)) ** 2) - ((ki / (2 * m)) ** 2))

