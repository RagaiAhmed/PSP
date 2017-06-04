from src import game_utils
import src.game_utils.function_proxy
from src.game_utils.square import *
from src.game_utils.utils import *


class Snake:
    def __init__(self):
        """
        Snake setup
        """
        self.head_position = create_point(GRID_SQUARE_SIZE, 0)  # keeps track of where it needs to go next
        self.direction = Directions.Right
        # body is a queue of squares
        self.body = [create_square(0, 0)]

        self.move_direction = Directions.Right
        self.crashed = False  # Used to indicate end of game
        self.next_position = get_next_point(self.head_position, self.move_direction)

    def move(self):
        """
        Snake motion
        """
        if game_utils.function_proxy.proton_move_snake is not None:
            game_utils.function_proxy.proton_move_snake()


    def point_upwards(self):  # pretty obvious what these do
        if (self.next_position.x-self.head_position.x)/GRID_SQUARE_SIZE ==direction_val[Directions.Down][0]:
            return
        self.move_direction = Directions.Up

    def point_left(self):
        if (self.next_position.x-self.head_position.x)/GRID_SQUARE_SIZE ==direction_val[Directions.Right][0]:
            return
        self.move_direction = Directions.Left

    def point_right(self):
        if (self.next_position.x-self.head_position.x)/GRID_SQUARE_SIZE ==direction_val[Directions.Left][0]:
            return
        self.move_direction = Directions.Right

    def point_down(self):
        if (self.next_position.x-self.head_position.x)/GRID_SQUARE_SIZE ==direction_val[Directions.Up][0]:
            return
        self.move_direction = Directions.Down

    def move_head_to_next_location(self):

        long=len(self.body) # takes the length of the body
        for i in range (1,long):
            self.body[long-i]=self.body[long-i-1] # takes the every part and changes it's position to the next one
        self.head_position = get_next_point(self.head_position, self.move_direction) # calc the next head position
        self.body[0]=self.head_position  # set the next head position
        self.next_position = get_next_point(self.head_position, self.move_direction)
        # calculate the next move




    def grow(self):
        if game_utils.function_proxy.proton_grow_snake is not None:
            game_utils.function_proxy.proton_grow_snake(self.body)

    def draw_self(self):
        """
        Draws the snake on the screen
        :return: 
        """
        for square in self.body:
            draw_square(square)
