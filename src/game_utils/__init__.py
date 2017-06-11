import os, platform

try:

    import pygame

except ImportError as e:

    print("PyGame package isn't installed..\n\tInstalling PyGame package ::")

    if platform.system() == "Linux":
        print("\tPermission Requested ::")
        os.system("xterm -e bash -c 'sudo pip install pygame'")

    else:
        os.system('pip install pygame')

    try:
        import pygame

    except ImportError:
        print("There was a problem while installing PyGame !!\n"
              "Please install PyGame package")
        quit()

    print("Installation Ended !")
print("\nGame Starting"
      " , Enjoy ^^")
