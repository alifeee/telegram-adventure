.mode json
.headers ON

-- .import ./data/nodes.json nodes

-- INSERT INTO nodes (body)
SELECT load_file('./data/nodes.json');