# Telegram adventure

Attempt to make a choose-your-own-adventure game as a Telegram bot.

## Development

### Requirements

| Name | Version |
| ---- | ------- |
| Python | 3.11.0 |

### Install dependencies

```bash
pip install -r requirements.txt
```

### Test

```bash
pytest
```

#### Watch file changes

```bash
ptw
```

## Story Database

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

### Show as graph

Note: display layout is randomised, so the graph may look different each time.

```bash
py ./sql/display_graph.py
```

## Telegram bot

### Run

```bash
py .src/bot.py
```

### Access token

To obtain an access token, see [help page](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Introduction-to-the-API), but in essence, talk to the [BotFather](https://t.me/botfather).

The access token is used via environment variables, or a `.env` file, which is not tracked by git.

```bash
touch .env
```

```.env
TELEGRAM_BOT_ACCESS_TOKEN=...
```
