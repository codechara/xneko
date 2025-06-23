import pygame, os, buildConfig, colors
from ScreenManager import Screen
from widgets.Footer import Footer
from widgets.FooterIcon import FooterIcon

class SetupChangeServerScreen(Screen):
    def __init__(self, screen, screen_mgr):
        super().__init__(screen, screen_mgr)

        self.footer = Footer(self.screen, "Изменить адрес сервера")
        self.footer.icon_left = FooterIcon(self.screen, "", action=self.back)
        self.footer.icon_right = FooterIcon(self.screen, "", action=exit)

    def loop(self, delta: int):
        self.screen.fill(colors.BACKGROUND)

        self.footer.tick(delta)

    def event(self, event: pygame.event.Event):
        self.footer.event(event)

    def back(self):
        from screen.SetupScreen import SetupScreen
        self.screen_mgr.set(SetupScreen)