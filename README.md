Weighted Graphs
1: Introduction

In graph theory, the traditional weighted graph consists of weights on edges only. Whereas weighing edges has many practical applications, weighing vertices as well also serve many purposes. In this paper, we will explore properties of a doubly-weighted graph—a graph in which both edges and vertices are weighted—and how they differ from an edge-only-weighted graph. Using these properties, we will explore and solve a problem by modeling it with a doubly-weighted graph.

links :

1.https://www.youtube.com/watch?v=_ZcfwrWvo28

2.http://olizardo.bol.ucla.edu/classes/soc-111/textbook/_book/2-2-the-building-blocks-of-graphs-edges-and-nodes.html#edges

3.https://www.youtube.com/watch?v=H922Eyzg-QU

Weighted Graphs :

A weighted graph is a graph with edges labeled by numbers (called weights). In general, we only consider nonnegative edge weights. Sometimes, ∞ can also be allowed as a weight, which in optimization problems generally means we must (or may not) use that edge.
In many applications, each edge of a graph has an associated numerical value, called a weight. Usually, the edge weights are nonnegative integers. Weighted graphs may be either directed or undirected.
The weight of an edge is often referred to as the “cost” of the edge. In applications, the weight may be a measure of the length of a route, the capacity of a line, the energy required to move between locations along a route, etc.

file:///C:/Users/USER1/Pictures/%D7%92%D7%A8%D7%A3.png

Shortest Paths :

The shortest path problem is about finding a path between 2 vertices in a graph such that the total sum of the edges weights is minimum.
Given a weighted graph, and a designated node S, we would like to find a path of least total weight from S to each of the other vertices in the graph. The total weight of a path is the sum of the weights of its edges.
We have seen that performing a DFS or BFS on the graph will produce a spanning tree, but neither of those algorithms takes edge weights into account.
Suppose we have a graph G of V nodes numbered from 1 to v . In addition, we have E edges that connect these nodes. We’re given two numbers S and D that represent the source node’s indices and the destination node, respectively.
Let’s check an example for better understanding. Suppose we have the following graph and we’re given S = 1 and D = 4:

file:///C:/Users/USER1/Pictures/ed.png

To go from node S to node D we have 4 paths:

1 \rightarrow 2 \rightarrow 4, with length equal to 2.
1 \rightarrow 2 \rightarrow 3 \rightarrow 4, with length equal to 3.
1 \rightarrow 3 \rightarrow 4, with length equal to 2.
1 \rightarrow 3 \rightarrow 2 \rightarrow 4, with length equal to 3.
As we can see, the shortest path has a length equal to 2. Also, we notice that we have two paths having a length equal to 2. Therefore, there are 2 shortest paths between node S and node D.
Explanation of classes:

class DiGraph(GraphInterface):


  dict of edges going in to node
  dict of edges going out of node
  list of all edges
  number of nodes
  number of edges

     add all nodes in list
    for n in raw_nodes:
        self.add_node(n.id, n.location)
    # add all edges in list
    for e in raw_edges:
        self.add_edge(e.src, e.dest, e.weight)

# returns all neighbors of node, all nodes that have a edge going in from node_id

def neighbors(self, node_id):

    returns all neighbors of node, all nodes that have a edge going in from node_id
    @return: The number of neighborrs
    if self.__edges_out.get(node_id):
        return [(k, v) for k, v in self.__edges_out[node_id].items()]
    else:
        return []

def v_size(self) -> int:

    Returns the number of vertices in this graph
    @return: The number of vertices in this graph
    return self.__nodes_count

def e_size(self) -> int:

    Returns the number of edges in this graph
    @return: The number of edges in this graph
    return self.__edges_count

def get_all_v(self) -> dict:

    return a dictionary of all the nodes in the Graph, each node is represented using a pair
     (node_id, node_data)
    return self.__nodes

def all_in_edges_of_node(self, id1: int) -> dict:

    return a dictionary of all the nodes connected to (into) node_id ,
    each node is represented using a pair (other_node_id, weight)
    return self.__edges_in[id1]

def all_out_edges_of_node(self, id1: int) -> dict:

   return a dictionary of all the nodes connected from node_id , each node is represented using a pair
    (other_node_id, weight)
    return self.__edges_out[id1]

def get_mc(self) -> int:

    Returns the current version of this graph,
    on every change in the graph state - the MC should be increased
    @return: The current version of this graph.
    raise self.mc

def add_edge(self, id1: int, id2: int, weight: float) -> bool:

    Adds an edge to the graph.
    @param id1: The start node of the edge
    @param id2: The end node of the edge
    @param weight: The weight of the edge
    @return: True if the edge was added successfully, False 
    Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
     check that nodes in edge exist
    if id1 in self.__nodes.keys() and id2 in self.__nodes.keys():
         check that edge does not exist already
            

def add_node(self, node_id: int, pos: tuple = None) -> bool:

    Adds a node to the graph.
    @param node_id: The node ID
    @param pos: The position of the node
    @return: True if the node was added successfully, False 
    Note: if the node id already exists the node will not be added
    

def remove_node(self, node_id: int) -> bool:

    Removes a node from the graph.
    @param node_id: The node ID
    @return: True if the node was removed successfully, False
    Note: if the node id does not exists the function will do nothing
    
        

def remove_edge(self, node_id1: int, node_id2: int) -> bool:

    
    Removes an edge from the graph.
    @param node_id1: The start node of the edge
    @param node_id2: The end node of the edge
    @return: True if the edge was removed successfully, False
    
    
class GraphAlgo(GraphAlgoInterface):

def get_graph(self) -> GraphInterface:

:return: the directed graph on which the algorithm works on.

def load_from_json(self, file_name: str) -> bool:

    Loads a graph from a json file.
    @param file_name: The path to the json file
    @returns True if the loading was successful, False o.w.

def save_to_json(self, file_name: str) -> bool:

    Saves the graph in JSON format to a file
    @param file_name: The path to the out file
    @return: True if the save was successful, False o.w.
    

def shortest_path(self, id1: int, id2: int) -> (float, list):

    Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
    @param id1: The start node id
    @param id2: The end node id
    @return: The distance of the path, a list of the nodes ids that the path goes through
    
    Example:
    
**>>> from GraphAlgo import GraphAlgo
>>> g_algo = GraphAlgo()
>>> g_algo.addNode(0)
>>> g_algo.addNode(1)
>>> g_algo.addNode(2)
>>> g_algo.addEdge(0,1,1)
>>> g_algo.addEdge(1,2,4)
>>> g_algo.shortestPath(0,1)
(1, [0, 1])
>>> g_algo.shortestPath(0,2)
(5, [0, 1, 2])**
    Notes:
    If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])

def TSP(self, node_lst: List[int]) -> (List[int], float):

    Finds the shortest path that visits all the nodes in the list
    :param node_lst: A list of nodes id's
    :return: A list of the nodes id's in the path, and the overall distance
    

def centerPoint(self) -> (int, float):

    Finds the node that has the shortest distance to it's farthest node.
    :return: The nodes id, min-maximum distance
    

def plot_graph(self) -> None:

    Plots the graph.
    If the nodes have a position, the nodes will be placed there.
    Otherwise, they will be placed in a random but elegant manner.
    @return: None
    
    
class GraphAlgoInterface:

This abstract class represents an interface of a graph.

def get_graph(self) -> GraphInterface:

    :return: the directed graph on which the algorithm works on.

def load_from_json(self, file_name: str) -> bool:

    Loads a graph from a json file.
    @param file_name: The path to the json file
    @returns True if the loading was successful, False o.w.
    raise NotImplementedError

def save_to_json(self, file_name: str) -> bool:

    Saves the graph in JSON format to a file
    @param file_name: The path to the out file
    @return: True if the save was successful, False         raise NotImplementedError

def shortest_path(self, id1: int, id2: int) -> (float, list):

    Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
    @param id1: The start node id
    @param id2: The end node id
    @return: The distance of the path, a list of the nodes ids that the path goes through
    
    Example:
    
>>> from GraphAlgo import GraphAlgo
>>> g_algo = GraphAlgo()
>>> g_algo.addNode(0)
>>> g_algo.addNode(1)
>>> g_algo.addNode(2)
>>> g_algo.addEdge(0,1,1)
>>> g_algo.addEdge(1,2,4)
>>> g_algo.shortestPath(0,1)
(1, [0, 1])
>>> g_algo.shortestPath(0,2)
(5, [0, 1, 2])
    Notes:
    If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])

def TSP(self, node_lst: List[int]) -> (List[int], float):

    Finds the shortest path that visits all the nodes in the list
    :param node_lst: A list of nodes id's
    :return: A list of the nodes id's in the path, and the overall distance

def centerPoint(self) -> (int, float):

   
    Finds the node that has the shortest distance to it's farthest node.
    :return: The nodes id, min-maximum distance

def plot_graph(self) -> None:

    Plots the graph.
    If the nodes have a position, the nodes will be placed there.
    Otherwise, they will be placed in a random but elegant manner.
    @return: None


class GraphInterface:

This abstract class represents an interface of a graph.

def v_size(self) -> int:

    Returns the number of vertices in this graph
    @return: The number of vertices in this graph

def e_size(self) -> int:

    Returns the number of edges in this graph
    @return: The number of edges in this graph

def get_all_v(self) -> dict:

    return a dictionary of all the nodes in the Graph, each node is represented using a pair
     (node_id, node_data)

def all_in_edges_of_node(self, id1: int) -> dict:

    return a dictionary of all the nodes connected to (into) node_id ,
    each node is represented using a pair (other_node_id, weight)

def all_out_edges_of_node(self, id1: int) -> dict:

    return a dictionary of all the nodes connected from node_id , each node is represented using a pair
    (other_node_id, weight)

def get_mc(self) -> int:

    Returns the current version of this graph,
    on every change in the graph state - the MC should be increased
    @return: The current version of this graph.
  

def add_edge(self, id1: int, id2: int, weight: float) -> bool:

    Adds an edge to the graph.
    @param id1: The start node of the edge
    @param id2: The end node of the edge
    @param weight: The weight of the edge
    @return: True if the edge was added successfully, False 
    Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
    
def add_node(self, node_id: int, pos: tuple = None) -> bool:

    Adds a node to the graph.
    @param node_id: The node ID
    @param pos: The position of the node
    @return: True if the node was added successfully, False 
    Note: if the node id already exists the node will not be added
    

def remove_node(self, node_id: int) -> bool:

    Removes a node from the graph.
    @param node_id: The node ID
    @return: True if the node was removed successfully, False 
    Note: if the node id does not exists the function will do nothing

def remove_edge(self, node_id1: int, node_id2: int) -> bool:

    Removes an edge from the graph.
    @param node_id1: The start node of the edge
    @param node_id2: The end node of the edge
    @return: True if the edge was removed successfully, False 
    Note: If such an edge does not exists the function will do nothing
