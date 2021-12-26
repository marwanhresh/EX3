import copy
import random
import sys
from typing import List
import json
import pygame
from collections import deque
from itertools import permutations
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from DiGraph import DiGraph
from Node import Node
from Edge import Edge


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, graph=None):
        if graph:
            self.__graph = graph
        else:
            self.__graph = DiGraph()

    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """
        return self.__graph

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """

        nodes = []
        edges = []
        try:
            with open(file_name) as f:
                graph_json = json.load(f)

            for node in graph_json['Nodes']:
                nodes.append(Node(node["id"], node.get("pos")))

            for edge in graph_json['Edges']:
                edges.append(Edge(edge["src"], edge["dest"], edge["w"]))

            self.__graph = DiGraph(nodes, edges)
            return True
        except Exception as e:
            return False

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        graph_json = {"Nodes": {}, "Edges": {}}
        for k, node in self.__graph.get_all_v().items():
            graph_json["Nodes"].update({"id": k, "pos": node.location})
        for edge in self.__graph.all_edges:
            graph_json["Edges"].update({"src": edge.src, "w": edge.weight, "dest": edge.dest})

        with open(file_name, 'w') as f:
            json.dump(graph_json, f)

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through
        Example:
#      >>> from GraphAlgo import GraphAlgo
#       >>> g_algo = GraphAlgo()
#        >>> g_algo.addNode(0)
#        >>> g_algo.addNode(1)
#        >>> g_algo.addNode(2)
#        >>> g_algo.addEdge(0,1,1)
#        >>> g_algo.addEdge(1,2,4)
#        >>> g_algo.shortestPath(0,1)
#        (1, [0, 1])
#        >>> g_algo.shortestPath(0,2)
#        (5, [0, 1, 2])
        Notes:
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """
        # init distences list
        distance_nodes = {k: (float('inf'), []) for k, v in self.__graph.get_all_v().items()}
        distance_nodes[id1] = (0, [id1])
        visited = []
        pq = deque([])
        pq.append((0, id1))

        while pq:
            # get unvisited node from queue
            (dist, current_vertex) = pq.popleft()
            visited.append(current_vertex)

            for neighbor_id, neighbor in self.__graph.neighbors(current_vertex):
                distance = neighbor.weight
                if neighbor_id not in visited:
                    old_cost = distance_nodes[neighbor_id][0]
                    new_cost = distance_nodes[current_vertex][0] + distance
                    if new_cost < old_cost:
                        pq.append((new_cost, neighbor_id))
                        # add to the path the neibor
                        path = copy.copy(distance_nodes[current_vertex][1])
                        path.append(neighbor_id)
                        distance_nodes[neighbor_id] = (new_cost, path)\
                            if distance_nodes[current_vertex][1] else (new_cost, [neighbor_id])
        distance = distance_nodes[id2][0]
        path = distance_nodes[id2][1]
        return distance, path

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """
        min_cost = sys.maxsize
        path_list = []
        next_permutation = permutations(node_lst)
        for permutation in next_permutation:
            current_path_cost = 0
            for i in range(len(node_lst)):
                current = permutation[i]
                previous = permutation[i-1]
                if self.__graph.all_in_edges_of_node(current).get(previous):
                    current_path_cost += self.__graph.all_in_edges_of_node(current)[previous].weight
                else:
                    current_path_cost = sys.maxsize
            if current_path_cost < min_cost:
                min_cost = current_path_cost
                path_list = permutation
        return list(path_list), min_cost

    def centerPoint(self) -> (int, float):
        """
        Finds the node that has the shortest distance to it's farthest node.
        :return: The nodes id, min-maximum distance
        """
        min_max_dist = sys.maxsize
        # go over all possible starting nodes
        for node_src in self.__graph.get_all_v():
            max_dist = 0
            # go over all possible ending nodes
            for node_dst in self.__graph.get_all_v():
                if node_src != node_dst:
                    # get the shortest path from start to end
                    dist, path = self.shortest_path(node_src, node_dst)
                    # get the forthest distence from start to a end node
                    if dist > max_dist:
                        max_dist = dist
            # get the smallest forthest distance
            if max_dist < min_max_dist:
                min_max_dist = max_dist
                min_max_id = node_src
        return min_max_id, min_max_dist

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        _quit = False
        pygame.init()
        screen = pygame.display.set_mode()

        for edge in self.__graph.all_edges:  # drawing lines
            start_node_location_x, start_node_location_y = (self.__graph.get_all_v().get(edge.src).location[0],
                                                            self.__graph.get_all_v().get(edge.src).location[
                                                                1]) if self.__graph.get_all_v().get(
                edge.src).location else (random.randint(a=1, b=1000), random.randint(a=1, b=1000))
            dest_node_location_x, dest_node_location_y = (self.__graph.get_all_v().get(edge.dest).location[0],
                                                          self.__graph.get_all_v().get(edge.dest).location[
                                                              1]) if self.__graph.get_all_v().get(
                edge.dest).location else (random.randint(a=1, b=1000), random.randint(a=1, b=1000))
            start = (start_node_location_x, start_node_location_y)
            end = (dest_node_location_x, dest_node_location_y)
            pygame.draw.aaline(screen, (255, 255, 255), start, end, 1)
        while not _quit:
            pygame.display.flip()

