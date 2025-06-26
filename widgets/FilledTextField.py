import enum

import pygame, os, buildConfig, colors

class FilledTextField:
    class Types(enum.Enum):
        TEXT = 0,
        PASSWORD = 1

    HEIGHT = 48

    def __init__(self, screen, label, width=255, position=(0, 0), limit=-1, type: Types=Types.TEXT):
        self.screen = screen
        self.label = label
        self.limit = limit
        self.type = type
        self.position = position
        self.width = width

        self.active = False

    def tick(self, delta):
        pygame.draw.rect(self.screen, colors.FTF, (self.position[0], self.position[1], self.width, FilledTextField.HEIGHT))

    def event(self, event):
        pass