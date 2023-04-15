import sqlite3
import json
import networkx as nx
import matplotlib.pyplot as plt

conn = sqlite3.connect('adventure.db')
cur = conn.cursor()

# nodes from database
cur.execute('SELECT body FROM nodes')
nodeData = cur.fetchall()
nodes = [json.loads(d[0]) for d in nodeData]

# edges from database
cur.execute('SELECT source, target, properties FROM edges')
edgeData = cur.fetchall()
edges = [{'source': d[0], 'target': d[1],
          'properties': json.loads(d[2])} for d in edgeData]

print(nodes[0])
print(edges[0])

G = nx.DiGraph()

for node in nodes:
    G.add_node(node['id'], label=node['id'])

for edge in edges:
    G.add_edge(edge['source'], edge['target'])

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)
plt.show()
