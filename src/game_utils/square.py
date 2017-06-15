from src import GRID_SQUARE_SIZE, turtle
from src.game_utils.point import Point


# makes a class square which handles x and y positions as points
class Square:
    """ A better way to represent a square """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        """
        equivalence of 2 squares
        :param other: square to compare to
        :return: true/false
        """
        return Point(self.x, self.y) == Point(other.x, other.y)

    def __ne__(self, other):
        """
        Non equivalence of 2 squares
        :param other: square to compare to
        :return: true/false
        """
        return not self.x == other.x

    def __str__(self):
        return Point(self.x, self.y).__str__()

    def __repr__(self):
        return self.__str__()


# a function to create a square
def create_square(x, y):
    return Square(x, y)


def draw_square(point):
    """ 
        draw a black box at its coordinates, leaving a small gap between cubes
        @:return square
     """

    turtle.goto(point.x - GRID_SQUARE_SIZE // 2 - 1, point.y - GRID_SQUARE_SIZE // 2 - 1)
    # goes to the edge of the square
    turtle.begin_fill()
    # starts to fill it with color
    for _ in range(4):
        turtle.forward(GRID_SQUARE_SIZE - GRID_SQUARE_SIZE // 10)
        turtle.left(90)
        # draws each side
    turtle.end_fill()
    # end filling
