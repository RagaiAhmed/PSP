# The first code to be excuted
from src.game_utils import *  # at first it imports another modules and __init__.py code execute
from tkinter import messagebox, simpledialog, colorchooser
import pickle

# after importing it makes a screen and a turtle
screen.setup(width=790, height=590)  # window dimensions
screen.title("Protonic snake!!")  # window title

messagebox.showinfo("Some Info >.<",
                    "This game is made for PSP protons summer project.\n By using the template of Eng. Amr Fathy.\n Members of the Team :::\n 1- Hana Ghanem \n 2- Ragai Ahmed ")
# some info about the project
name = simpledialog.askstring("Snake Master","Enter your name :")  # gets the name
while name==None:
    name=simpledialog.askstring("Snake Master","You can't just cancel :3 \n please , Enter your name :")
color = colorchooser.askcolor(title="Your Snake Color")[0]  # gets snake color
while color==None:
    color = colorchooser.askcolor(title="Your Snake Color,Please")[0]  # gets snake color

# getting stored leaderboard
try:
    file = open("lb", "rb")
    lb = pickle.load(file)
    file.close()
except EOFError and FileNotFoundError as e:
    lb = []
