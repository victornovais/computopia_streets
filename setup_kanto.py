# coding: utf-8
import networkx as nx
import matplotlib.pyplot as plt


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

nx.draw_spectral(G, node_size=800)

plt.savefig("kanto_graph.png") # save as png
plt.show()