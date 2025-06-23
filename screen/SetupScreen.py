import os

import pygame, colors

import buildConfig
from ScreenManager import Screen
from widgets.IconButton import IconButton
from widgets.Button import Button
from widgets.ButtonOutline import ButtonOutline

class SetupScreen(Screen):
    def setup(self):
        if os.path.exists(".session"):
            # Сессия существует, логин/регистрация не нужна
            pass

        self.font_small = pygame.font.Font("assets/Roboto.ttf", 12)
        self.font = pygame.font.Font("assets/Roboto.ttf", 16)
        self.font_welcome = pygame.font.Font("assets/Roboto-Bold.ttf", 32)
        self.server_settings = IconButton(self.screen, "", exit)

        self.button = Button(self.screen, ["", "Hello мир!"], exit, (10, 10))
        self.button_outline = ButtonOutline(self.screen, ["", "Аутлайн"], exit, (10, 62))

    def loop(self, delta):
        self.screen.fill(colors.BACKGROUND)
        self.screen.blit(self.font_small.render(buildConfig.VERSION, True, colors.PRIMARY), (12, self.screen.get_size()[1]-28))
        self.server_settings.position = (self.screen.get_size()[0]-IconButton.SIZE[0]-IconButton.SIZE[0]/3, IconButton.SIZE[1]/3)
        self.server_settings.tick(delta)

        welcome = self.font_welcome.render("Добро пожаловать!", True, colors.FONT)
        self.screen.blit(welcome, (self.screen.get_size()[0]/2-welcome.get_size()[0]/2, self.screen.get_size()[1]/3-welcome.get_size()[1]/2))

        a = self.font.render("Вы играете впервые, или у вас уже есть аккаунт?", True, colors.FONT)
        self.screen.blit(a, (self.screen.get_size()[0]/2-a.get_size()[0]/2, self.screen.get_size()[1]/2-a.get_size()[1]/2))

        self.button.tick(delta)
        self.button_outline.tick(delta)

    def event(self, e):
        self.server_settings.event(e)
        self.button.event(e)
        self.button_outline.event(e)