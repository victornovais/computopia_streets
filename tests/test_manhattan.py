# coding: utf-8
import unittest
import networkx as nx
from graph import create_manhattan_graph


class KantoStreetsTest(unittest.TestCase):
    def setUp(self):
        self.Graph = create_manhattan_graph()

    def test_grafo_deve_ser_unidirecionado(self):
        self.assertTrue(self.Graph.is_directed())

    def test_todos_nos_devem_possuir_arestas_de_chegada(self):
        nodes = self.Graph.nodes()

        for node in nodes:
            node_predecessors = self.Graph.predecessors(node)
            self.assertTrue(node_predecessors)

    def test_todos_nos_devem_possuir_arestas_de_saida(self):
        nodes = self.Graph.nodes()

        for node in nodes:
            node_sucessors = self.Graph.successors(node)
            self.assertTrue(node_sucessors)

    def test_a_partir_do_no_1_e_possivel_alcancar_qualquer_no(self):
        nodes = self.Graph.nodes()
        source_node = 1

        for target_node in nodes:
            self.assertTrue(nx.has_path(self.Graph, source_node, target_node))

    def test_a_partir_de_qualquer_no_e_possivel_alcancar_o_no_1(self):
        nodes = self.Graph.nodes()
        target_node = 1

        for source_node in nodes:
            self.assertTrue(nx.has_path(self.Graph, source_node, target_node))