import pygame

from screen.SetupScreen import SetupScreen
from Window import Window
from Properties import Properties
from ScreenManager import ScreenManager

pygame.init()

def main():
    config = Properties(".config").overwrite(Properties.Dot.CONFIG).read()
    window = Window()
    screen_manager = ScreenManager(config, window)

    screen_manager.set(SetupScreen)
    screen_manager.loop()

if __name__ == "__main__":
    main()