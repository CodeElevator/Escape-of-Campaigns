from .objects import *
from rich.console import Console
import os
import sqlite3

conn = sqlite3.connect('player_data.db')
console = Console()

class Game:
    def __init__(self):
        self.health = 100
    
    def menu(self):
        console.print("Welcome to Escape of Campaigns ! \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", style = "bold white", justify="center", width=100, height=100)
