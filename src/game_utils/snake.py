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
        self.body = [create_square(0, 0)]

        self.move_direction = Directions.Right
        self.crashed = False  # Used to indicate end of game
        self.next_position = get_next_point(self.head_position, self.move_direction)

    def reset(self):

        self.head_position = create_point(GRID_SQUARE_SIZE, 0)  # keeps track of where it needs to go next
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

    """
            due to some bugs we needed to do some things. 

            bug description:
                when you press an arrow key the snake changes direction but there is a twist
                the snake can't go to the opposite direction he is going

                the bug is when you moving any direction let it be up and you need to go down
                if you press down you won't go down because it is the opposite direction
                but if ou pressed right and down quickly 
                it will go down forming the bug

            Reason:
                because in the if condition and to prevent going the opposite direction 
                it checks the direction variable 
                which can be changed many times in the same frame
                since it's linked with the button press not frame cycle 

            Fix :
                making the if condition check not the direction variable 
                but the current head position and next head position calculated each frame
                therefore if you are going up and pressed down it won't go down and if you pressed
                right and down quickly it will still know that you are going up and will go right as you
                ordered but not down

            More Explanation:
                using the difference between the next and current head positions we can determine the 
                direction which is the REAL direction used by the previous frame 
                we can say that it gives us the directional vector by the difference of two points on a plane
            """

    def point_upwards(self):
        if (self.next_position.y - self.head_position.y) / GRID_SQUARE_SIZE == direction_val[Directions.Down][1]:
            # check for the bug description above to know how this condition work
            return
        self.move_direction = Directions.Up

    def point_left(self):
        if (self.next_position.x - self.head_position.x) / GRID_SQUARE_SIZE == direction_val[Directions.Right][0]:
            # check for the bug description above to know how this condition work
            return
        self.move_direction = Directions.Left

    def point_right(self):
        if (self.next_position.x - self.head_position.x) / GRID_SQUARE_SIZE == direction_val[Directions.Left][0]:
            # check for the bug description above to know how this condition work
            return
        self.move_direction = Directions.Right

    def point_down(self):
        if (self.next_position.y - self.head_position.y) / GRID_SQUARE_SIZE == direction_val[Directions.Up][1]:
            # check for the bug description above to know how this condition work
            return
        self.move_direction = Directions.Down

    def move_head_to_next_location(self):

        long = len(self.body)  # takes the length of the body
        for i in range(1, long):
            self.body[long - i] = self.body[long - i - 1]
            # takes every part from the end and changes it's position to the previous one

        self.head_position = get_next_point(self.head_position, self.move_direction)
        # calc the next head position

        self.body[0] = self.head_position
        # set the next head position

        self.next_position = get_next_point(self.head_position, self.move_direction)

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
