try:  # try to import PyGame package

    import pygame

except ImportError:  # if the package not found

    import pip

    print("PyGame package isn't installed..\n\tInstalling PyGame package ::")

    pip.main(['install', "--user", "pygame"])  # installs PyGame for the current user

    print("Installation Ended !")
    print("Please restart the game \n"
          ", If the problem still happens check the instructions for installing pygame manually. ")
    quit()

print("\nGame Starting, Enjoy! ")
