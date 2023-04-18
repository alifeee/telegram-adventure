import sqlite3
import json

# schema
#
# CREATE TABLE IF NOT EXISTS nodes (
#     body TEXT,
#     id TEXT GENERATED ALWAYS AS (json_extract(body, '$.id')) VIRTUAL NOT NULL UNIQUE ON CONFLICT REPLACE
# );

# CREATE TABLE IF NOT EXISTS edges (
#     source TEXT,
#     target TEXT,
#     properties TEXT,
#     UNIQUE (source, target) ON CONFLICT REPLACE,
#     FOREIGN KEY (source) REFERENCES nodes(id),
#     FOREIGN KEY (target) REFERENCES nodes(id)
# );


class Database:
    def __init__(self, db: str):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        # get schema from "../sql/schema.sql" and execute it
        with open("./sql/schema.sql", "r") as f:
            schema = f.read()
        self.cur.executescript(schema)
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def get_node(self, node_id: str):
        # id, body. return body or error
        self.cur.execute("SELECT body FROM nodes WHERE id=?", (node_id,))
        result = self.cur.fetchone()
        if result is None:
            raise ValueError(f"Node {node_id} does not exist.")
        body = json.loads(result[0])
        return body

    def get_choices_for_node(self, node_id: str):
        # return {source, target, properties}
        self.cur.execute(
            "SELECT source, target, properties FROM edges WHERE source=?", (
                node_id,)
        )
        result = self.cur.fetchall()
        if result is None:
            raise ValueError(f"Node {node_id} has no choices.")
        return [{
            "source": source,
            "target": target,
            "properties": json.loads(properties)
        } for source, target, properties in result]
