from .objects import *
from rich.console import Console
from rich.markdown import Markdown
import platform
import os
import sqlite3
from time import sleep

conn = sqlite3.connect('player_data.db')
cur = conn.cursor()
console = Console()
os_sys = platform.system()
clear_cmd = 'clear' if os_sys != 'Windows' else 'cls'

class Game:
    def __init__(self):
        self.health = 100
    
    def play(self):
        os.system(clear_cmd)
        console.print("The war between Celestia and Gamboo was horrible and the damage was making civials sick.")
        sleep(5)
        console.print("Not only mentally but physically (diseases, injuries, etc).")
        sleep(5)
        console.print("Nobody was able to stop the war, so a local spy agency decided to let their freshly trained soldier to kill the leader of Gamboo.")
        sleep(2)
        console.print("That soldier was you...")
    
    def menu(self):
        os.system(clear_cmd)
        console.print("Welcome to Escape of Campaigns ! \n\n\n\n\n\n", style = "bold white", justify="center")
        console.print("""
Time: Middle Age in a fantasy world, where internet and technology doesn't exist.
Gamboo Empire: An empire lead by General Gamboo, a very evil person who only wants money, pride, and power.
Celestia Kingdom: A kingdom lead by King Fallen, they only look to take care of their people and run buissness to make money. King Fallen has a daughter,
Adriana.\n\n\n\n\n
        """, style = "bold white", justify="center")
        console.print("[P]lay", end = '\t\t\t\t', style="green", justify='center')
        console.print("[Q]uit", style = 'red', justify='center')
        choice = input("P for Play and Q for quit, choose one: ")
        if choice == "P" or choice == "p":
            self.play()
        else:
            exit(0)
    
