from Game import *
from rich import *
import sqlite3
import os
import platform

try:
    conn = sqlite3.connect('Database/gamestats.db')
    conn2 = sqlite3.connect('Database/player_data.db')
except sqlite3.OperationalError:
    os.system('mkdir Database')
    if platform.system == 'Linux':
        os.system('touch gamestats.db && touch player_data.db')
    elif platform.system == 'Windows':
        os.system('type nul > gamestast.db && type nul > player_data.db')

cur = conn.cursor()
cur2 = conn2.cursor()

gamestats = """

"""

player_data = """

"""