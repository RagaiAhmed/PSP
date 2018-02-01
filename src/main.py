import os
import sys

sys.path.append(os.path.abspath(__file__)[:-12])

from src.game_utils.game_setup import *
from src.tasks import submit_your_functions

"""
    This file is the one you will use to run the game. don't mind the code here. 
    Check basic_functions.py to know what tools you have and
    tasks.py to know what you'll have to do.
"""


def main():
    # Don't modify the below code
    submit_your_functions()
    run_game_loop()


main()
