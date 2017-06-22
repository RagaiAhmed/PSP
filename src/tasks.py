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
        Uses an edited version of before implemented function in Snake class
    """
    move_snake_head_to_next()


def grow_snake(body):
    """
    This function is responsible for growing the snake when it eats food
    :param body : takes the snake body to grow  
    """
    body.append(body[-1])  # adds a cube at the last place in the body
    # where the added cube will follow the previous cube an so on


def frame_logic():
    """
        Controls Frame Logic
    """
    snake = get_snake()
    snake.move()
    body = snake.body
    if body[0] == get_food_position():  # if the snake ate a food
        food_location(body)  # calls a function to change food location taking care of not spawning on snake body
        increase_score()
        snake.grow()
    elif body[0] in body[1:] or is_out_of_screen(body[0]):  # checks if eaten itself or out of screen
        game_over()


def food_location(body):
    """
    
    :param body: Snake body to avoid
    :return: None
    """
    rnd_pnt = random_point()
    while rnd_pnt in body:
        rnd_pnt = random_point()
    change_food_location(rnd_pnt)


def submit_your_functions():
    check.proton_frame_logic = frame_logic
    check.proton_grow_snake=grow_snake
    check.proton_move_snake=move_snake
    check.proton_change_food_location=food_location
