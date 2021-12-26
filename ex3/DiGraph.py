import datetime

from GraphInterface import GraphInterface
from Node import Node
from Edge import Edge


class DiGraph(GraphInterface):
    def __init__(self, raw_nodes=[], raw_edges=[]):
        self.__nodes = {}
        # dict of edges going in to node
        self.__edges_in = {}
        # dict of edges going out of node
        self.__edges_out = {}
        # list of all edges
        self.__all_edges = []
        # number of nodes
        self.__nodes_count = len(raw_nodes)
        # number of edges
        self.__edges_count = len(raw_edges)
        self.mc = 0

        # add all nodes in list
        for n in raw_nodes:
            self.add_node(n.id, n.location)
        # add all edges in list
        for e in raw_edges:
            self.add_edge(e.src, e.dest, e.weight)

    @property
    def all_edges(self):
        return self.__all_edges

    # returns all neighbors of node, all nodes that have a edge going in from node_id
    def neighbors(self, node_id):
        """
        returns all neighbors of node, all nodes that have a edge going in from node_id
        @return: The number of neighborrs
        """
        if self.__edges_out.get(node_id):
            return [(k, v) for k, v in self.__edges_out[node_id].items()]
        else:
            return []

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        return self.__nodes_count

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        return self.__edges_count

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph, each node is represented using a pair
         (node_id, node_data)
        """
        return self.__nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
         """
        return self.__edges_in[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """
        return self.__edges_out[id1]

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        raise self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        # check that nodes in edge exist
        if id1 in self.__nodes.keys() and id2 in self.__nodes.keys():
            # check that edge does not exist already
            if id1 not in self.__edges_out.keys() or id2 not in self.__edges_out[id1].keys():
                new_edge = Edge(id1, id2, weight)
                if new_edge.src not in self.__edges_out.keys():
                    self.__edges_out[new_edge.src] = {new_edge.dest: new_edge}
                else:
                    self.__edges_out[new_edge.src][new_edge.dest] = new_edge
                if new_edge.dest not in self.__edges_in.keys():
                    self.__edges_in[new_edge.dest] = {new_edge.src: new_edge}
                else:
                    self.__edges_in[new_edge.dest][new_edge.src] = new_edge
                self.__all_edges.append(new_edge)
                self.__edges_count += 1
                return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added
        """
        # check that node does not already exist
        if node_id not in self.__nodes.keys():
            new_node = Node(node_id, pos)
            new_node.last_change = datetime.datetime.now()
            self.__nodes[node_id] = new_node
            self.__nodes_count += 1
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        Note: if the node id does not exists the function will do nothing
        """
        success = True
        edges_to_remove = []
        if node_id in self.__nodes.keys():
            node = self.__nodes[node_id]
            # remove all edges going in to node_id
            if node.id in self.__edges_in.keys():
                for k, edge in self.__edges_in[node.id].items():
                    edges_to_remove.append((edge.src, edge.dest))

            # remove all edges going out of node_id
            if node.id in self.__edges_out.keys():
                for k, edge in self.__edges_out[node.id].items():
                    edges_to_remove.append((edge.src, edge.dest))

            for src, dst in edges_to_remove:
                success = success and self.remove_edge(src, dst)
            # remove node
            del self.__nodes[node_id]
            # decrease node count
            self.__nodes_count -= 1
        return success

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        """
        if node_id2 in self.__edges_in.keys() and node_id1 in self.__edges_out.keys():
            del self.__edges_in[node_id2][node_id1]
            del self.__edges_out[node_id1][node_id2]
            self.__edges_count -= 1
            return True
        return False



