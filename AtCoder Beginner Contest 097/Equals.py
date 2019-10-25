import networkx as nx
import matplotlib.pyplot as plt
n, m = map(int, input().split())
G = nx.Graph()
A = list(map(int, input().split()))
G.node(range(1,n+2))
for i in range(m):
    s, e = map(int, input().split())
    G.add_edge(s,e)
nx.draw_networkx(G)
plt.show()
