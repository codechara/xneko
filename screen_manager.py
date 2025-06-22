import pygame

import buildConfig
from properties import Properties
from window import Window
from screen.screen import Screen

class ScreenManager:
    def __init__(self, config: Properties, window: Window):
        self.window = window
        self.config = config

        self.clock = pygame.time.Clock()
        self.screen: Screen = None

    def set(self, screen_class: type[Screen]):
        self.screen = screen_class(self.window.screen)

    def loop(self):
        delta = 0

        while True:
            self.screen.tick(delta)

            for event in pygame.event.get():
                self.screen.event(event)

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            pygame.display.flip()
            delta = self.clock.tick(buildConfig.FPS)