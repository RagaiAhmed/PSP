from src.game_utils import *
from tkinter import messagebox, simpledialog, colorchooser
from turtle import Turtle

import pickle

GRID_SQUARE_SIZE = 20
move_time = 180

turtle = Turtle(visible=False)
screen = turtle.screen

screen.colormode(255)
screen.setup(width=790, height=590)
screen.title("Protonic snake!!")

messagebox.showinfo("Some Info >.<",
                    "This game is made for PSP protons summer project.\n"
                    "\n"
                    "By using the template of Eng. Amr Fathy.\n"
                    "\n"
                    "Members of the Team :::\n"
                    "   1- Hana Ghanem \n"
                    "   2- Ragai Ahmed ")

name = None
color = None
while name is None or name == "":
    name = simpledialog.askstring("Snake Master"
                                  , "Enter your name :")

while color is None:
    color = colorchooser.askcolor(title="Your Snake Color")[0]

try:
    file = open("lb", "rb")
    lb = pickle.load(file)
    file.close()
except EOFError and FileNotFoundError as e:
    lb = []