import pygame

from screen.example import ExampleScreen

pygame.init()

from window import Window
from properties import Properties
from screen_manager import ScreenManager

def main():
    config = Properties(".config").overwrite(Properties.Dot.CONFIG).read()
    window = Window()
    screen_manager = ScreenManager(config, window)

    screen_manager.set(ExampleScreen)
    screen_manager.loop()

if __name__ == "__main__":
    main()