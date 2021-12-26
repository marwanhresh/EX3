from unittest import TestCase
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class TestGraph(TestCase):
    def test_graph_algo(self):
        g = DiGraph()
        g_algo = GraphAlgo(g)
        g_algo.get_graph().add_node(0)
        g_algo.get_graph().add_node(1)
        g_algo.get_graph().add_node(2)
        g_algo.get_graph().add_node(3)
        g_algo.get_graph().add_edge(0,1,1)
        g_algo.get_graph().add_edge(1,2,4)
        g_algo.get_graph().add_edge(1, 3, 1)
        g_algo.get_graph().add_edge(2, 3, 2)
        g_algo.get_graph().add_edge(3, 0, 1)
        g_algo.get_graph().add_edge(3, 2, 1)
        g_algo.get_graph().add_edge(3, 1, 2)
        g_algo.get_graph().add_edge(0, 2, 1)
        g_algo.get_graph().add_edge(1, 0, 2)
        g_algo.shortest_path(0,1)
        self.assertEqual(g_algo.shortest_path(0, 2), (1, [0, 2]))
        self.assertEqual(g_algo.shortest_path(0, 3), (2, [0, 1, 3]))
        self.assertEqual(g_algo.TSP([0,1,2,3]), ([0, 2, 3, 1], 7))
        self.assertEqual(g_algo.centerPoint(), (0,2))
        g_algo.plot_graph()

