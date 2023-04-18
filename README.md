# Telegram adventure

Attempt to make a choose-your-own-adventure game as a Telegram bot.

## Requirements

| Name | Version |
| ---- | ------- |
| Python | 3.11.0 |

## Quickstart

### Install dependencies

```bash
pip install -r requirements.txt
```

### Export environment variables ([see below](#telegram-access-token))

```bash
TELEGRAM_BOT_ACCESS_TOKEN=...
```

### Run

```bash
py .src/bot.py
```

## Development

### Test with `pytest`

```bash
ptw
```

### Story database

#### Create

```bash
sqlite3 adventure.db < sql/schema.sql
```

#### Load data

```bash
py ./sql/load_data.py
```

#### Dump data

```bash
sqlite3 adventure.db < sql/print_nodes.sql
sqlite3 adventure.db < sql/print_edges.sql
```

#### Show as a graph

Note: display layout is randomised, so the graph may look different each time.

```bash
py ./sql/display_graph.py
```

## Telegram Access token

To obtain an access token for telegram, see [help page](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Introduction-to-the-API), but in essence, talk to the [BotFather](https://t.me/botfather).

The access token is used via an environment variable, or a `.env` file, which is not tracked by git.

```bash
touch .env
```

```.env
TELEGRAM_BOT_ACCESS_TOKEN=...
```
