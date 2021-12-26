from unittest import TestCase
from DiGraph import DiGraph


class TestGraph(TestCase):
    def test_d_graph(self):
        g = DiGraph()  # creates an empty directed graph
        for n in range(4):
            g.add_node(n, int(n))
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)
        self.assertEqual(g.v_size(), 4)
        self.assertEqual(g.e_size(), 5)
        self.assertEqual(str(g.get_all_v()), "{0: id =0 location=0, 1: id =1 location=1, 2: id =2 location=2, 3: id =3 location=3}")
        self.assertEqual(str(g.all_in_edges_of_node(3)), "{2: src =2 dest=3 w=1.1, 1: src =1 dest=3 w=1.9}" )
        self.assertEqual(str(g.all_out_edges_of_node(1)), "{0: src =1 dest=0 w=1.1, 2: src =1 dest=2 w=1.3, 3: src =1 dest=3 w=1.9}")
        self.assertTrue(g.remove_node(1))
        self.assertEqual(str(g.all_in_edges_of_node(3)), "{2: src =2 dest=3 w=1.1}")
        self.assertEqual(g.e_size(), 1)
        self.assertTrue(g.remove_edge(2, 3))
        self.assertEqual(str(g.all_in_edges_of_node(3)), "{}")
        self.assertEqual(g.v_size(), 3)
        self.assertEqual(g.e_size(), 0)

