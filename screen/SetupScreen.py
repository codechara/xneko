import pygame, colors, os, buildConfig

from ScreenManager import Screen
from widgets.IconButton import IconButton
from widgets.Button import Button
from widgets.ButtonOutline import ButtonOutline

class SetupScreen(Screen):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)

        if os.path.exists(".session"):
            # Сессия существует, логин/регистрация не нужна
            pass

        self.font_small = pygame.font.Font("assets/Roboto.ttf", 12)
        self.font = pygame.font.Font("assets/Roboto.ttf", 16)
        self.font_welcome = pygame.font.Font("assets/Roboto-Bold.ttf", 48)
        self.server_settings = IconButton(self.screen, "", exit)
        self.first_play = Button(self.screen, ("", "Я играю впервые"), exit)
        self.have_account = ButtonOutline(self.screen, ("", "У меня уже есть аккаунт"), exit)

    def loop(self, delta):
        #self.screen.fill(colors.BACKGROUND)
        #self.screen.blit(self.font_small.render(buildConfig.VERSION, True, colors.PRIMARY), (12, self.screen.get_size()[1]-28))
        #self.server_settings.position = (self.screen.get_size()[0]-IconButton.SIZE[0]-IconButton.SIZE[0]/3, IconButton.SIZE[1]/3)
        #self.server_settings.tick(delta)

        #welcome = self.font_welcome.render("Добро пожаловать!", True, colors.FONT)
        #self.screen.blit(welcome, (self.screen.get_size()[0]/2-welcome.get_size()[0]/2, self.screen.get_size()[1]/3-welcome.get_size()[1]/2))

        #a = self.font.render("Вы играете впервые, или у вас уже есть аккаунт?", True, colors.FONT)
        #self.screen.blit(a, (self.screen.get_size()[0]/2-a.get_size()[0]/2, self.screen.get_size()[1]/2-a.get_size()[1]/2))

        #self.first_play.position = (self.screen.get_width()/2-self.first_play.width-5, self.screen.get_height()-self.screen.get_height()/3)
        #self.first_play.tick(delta)
        #self.have_account.position = (self.screen.get_width()/2+5, 0)
        #self.have_account.tick(delta)

        #
        # ================
        #

        #self.screen.fill(colors.BACKGROUND)
#
        #self.screen.blit(self.font_small.render(buildConfig.VERSION, True, colors.PRIMARY), (4, self.screen.get_size()[1]-16))
        #self.server_settings.position = (self.screen.get_size()[0]-IconButton.SIZE[0]-IconButton.SIZE[0]/3, IconButton.SIZE[1]/3)
        #self.server_settings.tick(delta)
#
        #welcome = self.font_welcome.render("Привет!", True, colors.FONT)
        #self.screen.blit(welcome, (25, 25))
#
        #firstplay = self.font.render("Играете впервые, или у вас есть аккаунт?", True, colors.FONT)
        #self.screen.blit(firstplay, (25, 100))
#
        #self.have_account.position = (25, self.screen.get_height()-Button.CIRCLE[1]-25)
        #self.have_account.tick(delta)
#
        #self.first_play.position = (25, self.have_account.position[1]-12-Button.CIRCLE[1])
        #self.first_play.tick(delta)

    def event(self, e):
        self.server_settings.event(e)
        self.first_play.event(e)
        self.have_account.event(e)