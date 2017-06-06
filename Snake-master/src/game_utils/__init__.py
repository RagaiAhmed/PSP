"""Setup the global variables"""
from turtle import Turtle # imports modules
GRID_SQUARE_SIZE = 20  # sets the square size
turtle = Turtle(visible=False) # declaring a turtle
screen = turtle.screen # declaring a windows
screen.colormode(255) # sets rgb value limits between 0 , 255
move_time=400 # a variable holds the time in millis between move steps of the snake

