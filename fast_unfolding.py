from typing import Dict, Iterable
from graph import KozikGraph, generate_child_kozik_graph


class FastUnfolding:
    def run(self, graph: KozikGraph):
        while True:
            initial_modularity = graph.modularity()
            self.process_graph(graph)
            if graph.modularity() <= initial_modularity:
                break
            graph = generate_child_kozik_graph(graph)
        print(f'Modularity = {graph.modularity()}')
        print('stop')

    def process_graph(self, graph: KozikGraph):
        for node in graph.get_nodes():
            neighbours = graph.get_neighbours(node)
            neighbour_to_gain_map: Dict[int, float] = self.map_modularity_gain_to_neighbours(
                graph, node, neighbours)
            if not neighbour_to_gain_map:
                continue
            highest_gain_neighbour = max(neighbour_to_gain_map, key=neighbour_to_gain_map.get)
            if neighbour_to_gain_map[highest_gain_neighbour] > 0:
                new_community = graph.get_node_community(highest_gain_neighbour)
                graph.add_to_community(new_community, node)

    def map_modularity_gain_to_neighbours(self, graph: KozikGraph, node: int, neighbours: Iterable[int]) -> dict[
        int, float]:
        gain_map = {}
        for neighbour in neighbours:
            neighbour_community = graph.get_node_community(neighbour)

            gain_map[neighbour] = self._calculate_modularity_gain(graph, neighbour_community, node)
        return gain_map

    def _calculate_modularity_gain(self, graph: KozikGraph, community: int, node: int) -> float:
        Ein = graph.get_edges_inside_community_weight_sum(community)
        Etot = graph.get_edges_incident_to_community_weight_sum(community)
        ki = graph.get_edges_incident_to_node_weight_sum(node)
        kin = graph.get_edges_in_community_incident_to_node_weight_sum(node, community)
        m = graph.get_all_edges_weight_sum()
        return 1000*((((Ein + kin) / (m)) - (((Etot + ki) / (m)) ** 2)) - (
                    (Ein / (m)) - ((Etot / (m)) ** 2) - ((ki / (m)) ** 2)))

