from src.game_utils import *
from tkinter import messagebox, simpledialog, colorchooser, OptionMenu, Tk, StringVar, Button, BOTTOM
from turtle import Turtle
import pickle



class window():
    """
        a class type of an option window for snake speed
    """
    def __init__(self):

        self.master = Tk()
        self.master.title("Snake Speed")
        self.master.geometry("{}x{}+{}+{}".format(200, 80, (self.master.winfo_screenwidth() - 200) // 2
                                                  , (self.master.winfo_screenheight() - 80) // 2))
        self.master.resizable(width=False, height=False)

        self.value = StringVar(self.master)
        self.value.set("Fast")

        self.Opp = OptionMenu(self.master, self.value, "Slow", "Fast", "Very Fast")
        self.Opp.pack()

        self.button = Button(self.master, text="Ok", command=self.ok)
        self.button.pack(side=BOTTOM)

        self.master.mainloop()

    def ok(self):
        global move_time

        stng = self.value.get()

        if stng == "Slow":
            move_time = 180

        elif stng == "Fast":
            move_time =120

        else:
            move_time = 80

        self.master.quit()
        self.master.destroy()



GRID_SQUARE_SIZE = 20

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

move_time = 1000

window()  # opens an option window for setting speed

try:
    file = open("lb", "rb")
    lb = pickle.load(file)
    file.close()
except EOFError and FileNotFoundError as e:
    lb = []
