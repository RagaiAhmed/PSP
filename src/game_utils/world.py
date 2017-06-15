import src, pygame.mixer, os
import src.game_utils.function_proxy
from src import screen, game_utils
from src import turtle, color, move_time
from src.game_utils.food import Food
from src.game_utils.snake import Snake
from src.game_utils.utils import get_random_point, set_turtle_color_rgb, set_turtle_color_string


class World:
    """
    Game world:
    - contains all the objects in the game
    - has the screen update handling
    - has game logic handling for each frame
    """

    def __init__(self):
        # game object has a screen, a turtle, a basic snake and a food
        self.artist = turtle
        self.artist.up()
        self.artist.speed(0)
        self.snake = Snake()
        self.food = Food(get_random_point())
        self.score = 0

        pygame.mixer.pre_init(0, 0, 0, 256)  # it sets values for the mixer,
        #  0 means default and 512 is the buffer size and is decreased to fix the latency
        pygame.mixer.init()
        self.win_snd = pygame.mixer.Sound(os.getcwd() + '/game_utils/Sounds/score.wav')
        self.lose_snd = pygame.mixer.Sound(os.getcwd() + '/game_utils/Sounds/lose.wav')

        self.bck_snd = pygame.mixer.Sound(os.getcwd() + '/game_utils/Sounds/background.wav')
        self.bck_snd.play(-1)  # -1 makes background sound runs for ever

        screen.tracer(0)
        # Can't refactor directions to one functions
        # because of the callback
        screen.onkeypress(self.snake.point_down, "Down")
        screen.onkeypress(self.snake.point_upwards, "Up")
        screen.onkeypress(self.snake.point_left, "Left")
        screen.onkeypress(self.snake.point_right, "Right")
        screen.listen()
        screen.ontimer(self.render_screen, src.move_time // 5)

    def next_frame(self):

        # Call protons function if it exists
        if game_utils.function_proxy.proton_frame_logic is not None:
            game_utils.function_proxy.proton_frame_logic()

        self.food.change_state()  # makes the food flash
        screen.ontimer(lambda: self.next_frame(), move_time)

    def render_screen(self):
        score_str = 'Score: ' + str(self.score)
        self.artist.clear()  # clears screen

        # draws snake with selected color
        set_turtle_color_rgb(int(color[0]), int(color[1]), int(color[2]))
        self.snake.draw_self()

        set_turtle_color_string("red")
        src.basic_functions.print_text_to_screen(-340, 270, score_str)

        self.food.draw_self()  # show the food and snake

        screen.update()
        screen.ontimer(self.render_screen, 15)

    def reset(self):
        self.snake.reset()
        self.score = 0
