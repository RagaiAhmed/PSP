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
    # to obvious to be explained
    move_snake_head_to_next()
    body=get_snake_body()
    if body[0] in body[1:] or is_out_of_screen(body[0]):
        game_over()
    screen.ontimer(move_snake, move_time)


def grow_snake(body):
    """
    This function is responsible for growing the snake when it eats food
    """
    body.append(body[len(body) - 1])


# TODO:: implement this
def frame_logic():  # Don't change the name of this function
    """
        This function now only changes the food location each frame into a random location which is obviously wrong :D, 
        add your own code that defines what happens when each frame is drawn, it should basically move the snake and 
        update the score and the food. 
        a simple code example: 
            move_snake()
            if (get_food_position() == calculate_snake_next_position()):
                change_food_location(random_point())
                grow_snake()
    """
    body=get_snake_body()
    if body[0]==get_food_position():
        rnd_pnt=random_point()
        while rnd_pnt in body:
            rnd_pnt=random_point()
        change_food_location(rnd_pnt)
        increase_score()
        get_snake().grow()
        Increase_speed()


# TODO:: (optional) add to this function if needed
def setup():  # Don't change the name of this function
    """
    This function contains the game setup logic, add any code here that you want to 
    execute before the game is loaded  
    """
    # change speed
    set_game_speed(180)
    # change color
    set_color_string("blue")


# DO NOT CHANGE THIS FUNCTION
def submit_your_functions():
    check.proton_frame_logic = frame_logic
    check.proton_grow_snake=grow_snake
    check.proton_move_snake=move_snake

