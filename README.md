# Telegram adventure

Attempt to make a choose-your-own-adventure game as a Telegram bot.

## Database

### Create

```bash
sqlite3 adventure.db < sql/schema.sql
```

### Load data

```bash
py ./sql/load_data.py
```

### Dump data

```bash
sqlite3 adventure.db < sql/print_nodes.sql
sqlite3 adventure.db < sql/print_edges.sql
```
