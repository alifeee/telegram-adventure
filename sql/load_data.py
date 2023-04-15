import sqlite3
import json


conn = sqlite3.connect('adventure.db')
cur = conn.cursor()

# nodes
with open('./data/nodes.json') as f:
    nodes = json.load(f)

for node in nodes:
    body = json.dumps(node)
    cur.execute('INSERT INTO nodes (body) VALUES (?)', (body,))

# edges
with open('./data/edges.json') as f:
    edges = json.load(f)

for edge in edges:
    source = edge['source']
    target = edge['target']
    properties = json.dumps(edge['properties'])
    cur.execute('INSERT INTO edges (source, target, properties) VALUES (?, ?, ?)',
                (source, target, properties))

conn.commit()
