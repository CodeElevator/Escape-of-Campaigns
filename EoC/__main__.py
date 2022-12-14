from .Game.game import Game
from rich import *
import sqlite3

conn = sqlite3.connect('./player_data.db')
cur = conn.cursor()

player_data = """
    CREATE TABLE IF NOT EXISTS "pdata" (
        "name" TEXT NOT NULL,
        "health" INTEGER,
        PRIMARY KEY("name")
    );
"""

# For understand that this is a script that can be run while the rest of the files are packages
if __name__ == '__main__':
    Game().menu()
    cur.execute(player_data)
    conn.commit()