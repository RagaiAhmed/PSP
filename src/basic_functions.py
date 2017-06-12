import datetime, src, pickle, tkinter.messagebox, src.game_utils.game_setup, time
from src.game_utils.utils import turtle, clear_turtle, kill_game, get_random_point, out_of_screen, get_next_point
from src.game_utils.square import create_square
from src.game_utils.game_setup import game_world
import winsound

def change_food_location(point):
    game_world.food.change_location(point)


def get_food_position():
    return game_world.food.position


def calculate_snake_next_position():
    return game_world.snake.next_position


def get_snake():
    return game_world.snake


def get_point_in_direction(point, direction):
    return get_next_point(point, direction)


def point_snake_up():
    game_world.snake.point_upwards()


def point_snake_down():
    game_world.snake.point_down()


def point_snake_left():
    game_world.snake.point_left()


def point_snake_right():
    game_world.snake.point_right()


def move_snake_head_to_next():
    game_world.snake.move_head_to_next_location()


def clear_screen():
    clear_turtle()


def get_snake_body():
    return game_world.snake.body


def add_next_position_to_snake_body(snake):
    snake.body.append(create_square(snake.x, snake.y))


def game_over():
    src.lb.append([src.name.split()[0]  # first name
                      , game_world.score  # score
                      , datetime.date.today()  # date
                   ])

    src.lb.sort(key=lambda x: x[1], reverse=True)
    src.lb = src.lb[:5]  # maximum names are 5

    strng = 'HighScores:\n'
    for i in range(len(src.lb)):
        strng += "{}) {} : {} \n" \
                 "  Date : {}\n" \
                 "".format(str(i + 1), src.lb[i][0], str(src.lb[i][1]), str(src.lb[i][2]))

    file = open("lb", "wb")
    pickle.dump(src.lb, file)
    file.close()

    if tkinter.messagebox.askquestion("Game Over",
                                          "You have got a Score of {}\n"
                                          " \n"
                                          " {}"
                                          " \n"
                                          " \n"
                                          " Do you want to play again ?".format(
                                              game_world.score, strng)) == 'no':
        time.sleep(0.5)
        kill_game()
    else:
        src.move_time = 400
        src.game_utils.game_setup.game_world.reset()
        time.sleep(0.5)


def set_color_string(color):
    turtle.fillcolor(color)


def increase_score():
    game_world.score += 1


def reset_score():
    game_world.score = 0


def print_text_to_screen(x, y, text):
    """
    print a string on the screen
    :param x: an int representing the x coordinate of the position of text
    :param y: an int representing the y coordinate of the position of text
    :param text: a string representing the text to be printed on screen 
    """
    turtle.setpos((x, y))
    turtle.write(text, move='False', align='center', font=('Arial', 16, 'normal'))


def is_out_of_screen(point):
    """
    Checks if a given point is out of the screen

    :param point: A Point that has x and y coordinates
    :return returns a Boolean, A True or a False
    """
    return out_of_screen(point)


def random_point():
    """
    :return: returns a Point(x,y) on the screen
    """
    return get_random_point()


def Increase_speed():
    """
    Changes snake moving speed
    :return: None 
    """
    src.move_time *= 3 / 5
