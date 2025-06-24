import pygame, colors, os, buildConfig

from ScreenManager import *
from widgets.IconButton import IconButton
from widgets.Button import Button
from widgets.ButtonOutline import ButtonOutline

class SetupScreen(Screen):
    def __init__(self, screen, screen_mgr: ScreenManager):
        super().__init__(screen, screen_mgr)

        if os.path.exists(".session"):
            # Сессия существует, логин/регистрация не нужна
            exit

        self.font_small = pygame.font.Font("assets/Roboto.ttf", 12)
        self.font = pygame.font.Font("assets/Roboto.ttf", 16)
        self.font_welcome = pygame.font.Font("assets/Roboto-Bold.ttf", 48)
        self.server_settings = IconButton(self.screen, "", self.change_server_screen)
        self.first_play = Button(self.screen, ("", "Я играю впервые"), exit)
        self.have_account = ButtonOutline(self.screen, ("", "У меня уже есть аккаунт"), exit)

    def loop(self, delta):
        self.screen.fill(colors.BACKGROUND)

        self.server_settings.position = (self.screen.get_width()-IconButton.SIZE[0]-12, 12)
        self.server_settings.tick(delta)

        self.screen.blit(self.font_small.render(buildConfig.VERSION, True, (0, 0, 0)), (12, self.screen.get_size()[1] - 28))

        hello = self.font_welcome.render("Добро пожаловать!", True, colors.BACKGROUND_FONT)
        first_play_text = self.font.render("Играете впервые, или у вас есть аккаунт?", True, colors.BACKGROUND_FONT)
        self.screen.blit(hello, (self.screen.get_width()/2-hello.get_width()/2, self.screen.get_height()/2-120))
        self.screen.blit(first_play_text, (self.screen.get_width()/2-first_play_text.get_width()/2, self.screen.get_height()/2-40))

        self.first_play.position = (self.screen.get_width()/2-self.first_play.width/2, self.screen.get_height()/2+12)
        self.first_play.tick(delta)
        self.have_account.position = (self.screen.get_width()/2-self.have_account.width/2, self.first_play.position[1]+24+Button.CIRCLE[1])
        self.have_account.tick(delta)

    def event(self, e):
        self.server_settings.event(e)
        self.first_play.event(e)
        self.have_account.event(e)

    def change_server_screen(self):
        from screen.SetupChangeServerScreen import SetupChangeServerScreen
        self.screen_mgr.set(SetupChangeServerScreen)