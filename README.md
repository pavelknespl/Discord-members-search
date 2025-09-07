# Common Server Members Finder

**Find users who are on both Discord servers**

This small Python bot helps you quickly identify which members are present on two Discord servers where your bot is added.  
Useful for community managers who want to compare participants between servers.

---

## Features

- Fetch members from two servers where your bot is present.  
- Compare them and output a list of common users.  
- Results can be displayed in the console or saved to a file (CSV/TXT).  
- Fully respects Discord API and rate limits.

---

## Requirements

- Python 3.8+  
- `discord.py` library  
- Discord bot with **Server Members Intent** enabled

Install `discord.py`:

```bash
pip install -U discord.py
