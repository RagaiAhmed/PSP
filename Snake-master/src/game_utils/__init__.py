"""Setup the global variables"""
from turtle import Turtle # imports modules

GRID_SQUARE_SIZE = 20  # sets the square size
REFRESH_INTERVAL = 1000 # delay between each frame of updating object properties
turtle = Turtle(visible=False) # declaring a turtle
screen = turtle.screen # declaring a windows
move_time=400 # a variable holds the time in millis between move steps of the snake

def set_interval(interval):
    """
    Changes the refresh interval to a given number
    :param interval: the number to be set 
    :return: None
    """
    global REFRESH_INTERVAL
    REFRESH_INTERVAL = interval
