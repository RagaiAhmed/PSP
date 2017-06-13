import pip, time

try:

    import pygame

except ImportError as e:

    print("PyGame package isn't installed..\n\tInstalling PyGame package ::")
    pip.main(['install', "--user", "pygame"])
    time.sleep(1)
    try:
        import pygame

    except ImportError:
        print("Please restart the game \n"
              ", If the problem still happens check the instructions for installing pygame manually. ")
        quit()

    print("Installation Ended !")
print("\nGame Starting"
      " , Enjoy ^^")
