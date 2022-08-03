from Game import *
from rich import *
import sqlite3
import os
import platform

try:
    conn = sqlite3.connect('Database/player_data.db')
except sqlite3.OperationalError:
    os.system('mkdir Database')
    os.system('cd ./Database')
    if platform.system == 'Linux':
        os.system('touch player_data.db')
    elif platform.system == 'Windows':
        os.system('type nul > player_data.db')
    else:
        os.system('echo \'\' > player_data.db')
    os.system('cd ..')
    conn = sqlite3.connect('Database/player_data.db')

cur = conn.cursor()

player_data = """
    CREATE TABLE IF NOT EXISTS "pdata" (
        "name" TEXT NOT NULL,
        PRIMARY KEY("name")
    );
"""

cur.execute(player_data)
conn.commit()
cur.close()