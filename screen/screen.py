import pygame

class Screen:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

        self.setup()

    def setup(self):
        pass

    def tick(self, delta: int):
        pass

    def event(self, event: pygame.event.Event):
        pass