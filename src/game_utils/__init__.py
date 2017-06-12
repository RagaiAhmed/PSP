import pip

try:

    import pygame

except ImportError as e:

    print("PyGame package isn't installed..\n\tInstalling PyGame package ::")
    pip.main(['install',"pygame"])
    try:
        import pygame

    except ImportError:
        print("There was a problem while installing PyGame !!\n"
              "Please install PyGame package")
        quit()

    print("Installation Ended !")
print("\nGame Starting"
      " , Enjoy ^^")
