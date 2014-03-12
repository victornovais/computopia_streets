# coding: utf-8
import networkx as nx


def create_kanto_graph():
    G = nx.DiGraph()

    G.add_edges_from([
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
        (5, 6),
        (5, 8),
        (8, 9),
        (6, 7),
        (7, 9),
        (9, 1),
    ])

    return G

def create_manhattan_graph():
    G = nx.DiGraph()

    G.add_edges_from([
        # 1ª linha
        (1, 2),
        (2, 3),
        (3, 4),

        # 2ª linha
        (8, 7),
        (7, 6),
        (6, 5),

        # 3ª linha
        (9, 10),
        (10, 11),
        (11, 12),

        # 4ª linha
        (16, 15),
        (15, 14),
        (14, 13),

        # 5ª linha
        (20, 19),
        (19, 18),
        (18, 17),

        # 1ª coluna
        (17, 13),
        (13, 9),
        (9, 5),
        (5, 1),

        # 2ª coluna
        (2, 6),
        (6, 10),
        (10, 14),
        (14, 18),

        # 3ª coluna
        (19, 15),
        (15, 11),
        (11, 7),
        (7, 3),

        # 4ª coluna
        (4, 8),
        (8, 12),
        (12, 16),
        (16, 20),
    ])

    return G