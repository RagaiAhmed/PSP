import src.game_utils.function_proxy as check
from src.basic_functions import *

"""
    This file is the one you'll be working on 
    read the documentation of the functions to know 
    what it must be able to do.
"""


def move_snake():
    """
    This function controls how the snake moves
    """
    move_snake_head_to_next()


def grow_snake(body):
    """
    This function is responsible for growing the snake when it eats food
    """
    body.append(body[len(body) - 1]) # adds a cube at the last place in the body


def frame_logic():  # Don't change the name of this function
    """
        Controls Frame Logic
    """
    snake=get_snake()
    snake.move()
    body=snake.body
    if body[0] == get_food_position():
        food_location(body)
        increase_score()
        snake.grow()
    elif body[0] in body[1:] or is_out_of_screen(body[0]):  # checks if eaten itself or out of screen
        game_over()


def food_location(body):
    rnd_pnt = random_point()
    while rnd_pnt in body:
        rnd_pnt = random_point()
    change_food_location(rnd_pnt)


# DO NOT CHANGE THIS FUNCTION
def submit_your_functions():
    check.proton_frame_logic = frame_logic
    check.proton_grow_snake=grow_snake
    check.proton_move_snake=move_snake
    check.proton_change_food_location=food_location
