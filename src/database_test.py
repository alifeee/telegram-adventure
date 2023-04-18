import sqlite3
import unittest
from database import Database
import json

EXAMPLE_NODES = [
    {
        "id": "forest hut",
        "title": "Forest Hut",
        "description": "You are in a forest hut.",
    },
    {
        "id": "forest path A",
        "title": "Forest Path A",
        "description": "You are on the left path.",
    },
    {
        "id": "forest path B",
        "title": "Forest Path B",
        "description": "You are on the right path.",
    },
    {
        "id": "forest exit",
        "title": "Forest Exit",
        "description": "You are at the exit of the forest.",
    }
]

EXAMPLE_EDGES = [
    {
        "source": "forest hut",
        "target": "forest path A",
        "properties": {
            "choice": "Go left",
        }
    },
    {
        "source": "forest hut",
        "target": "forest path B",
        "properties": {
            "choice": "Go right",
        }
    },
    {
        "source": "forest path A",
        "target": "forest exit",
        "properties": {
            "choice": "Go straight",
        }
    },
    {
        "source": "forest path B",
        "target": "forest exit",
        "properties": {
            "choice": "Go straight",
        }
    }
]


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database(":memory:")
        for node in EXAMPLE_NODES:
            self.db.cur.execute("INSERT INTO nodes (body) VALUES (?)",
                                (json.dumps(node),))
        for edge in EXAMPLE_EDGES:
            self.db.cur.execute("INSERT INTO edges (source, target, properties) VALUES (?, ?, ?)",
                                (edge["source"], edge["target"], json.dumps(edge["properties"])))
        self.db.conn.commit()

    def test_get_node(self):
        # Arrange
        # Act
        result = self.db.get_node("forest hut")

        # Assert
        self.assertEqual(result, EXAMPLE_NODES[0])

    def test_get_choices_for_node(self):
        # Arrange
        choices = [
            choice for choice in EXAMPLE_EDGES if choice["source"] == "forest hut"
        ]

        # Act
        result = self.db.get_choices_for_node("forest hut")

        # Assert
        self.assertEqual(result, choices)
