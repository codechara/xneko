import os

import pygame, colors

import buildConfig
from ScreenManager import Screen
from widgets.IconButton import IconButton


class SetupScreen(Screen):
    def setup(self):
        if os.path.exists(".session"):
            # Сессия существует, логин/регистрация не нужна
            pass

        self.font_small = pygame.font.Font("assets/Roboto.ttf", 12)
        self.font = pygame.font.Font("assets/Roboto.ttf", 16)
        self.server_settings = IconButton(self.screen, "", exit)

    def loop(self, delta):
        self.screen.fill(colors.BACKGROUND)
        self.screen.blit(self.font_small.render(buildConfig.VERSION, True, colors.PRIMARY), (12, self.screen.get_size()[1]-28))
        self.server_settings.position = (self.screen.get_size()[0]-IconButton.SIZE[0]-IconButton.SIZE[0]/3, IconButton.SIZE[1]/3)
        self.server_settings.tick(delta)

    def event(self, e):
        self.server_settings.event(e)