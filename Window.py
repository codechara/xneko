import pygame, buildConfig, enum, screeninfo
from pygame._sdl2 import Window as w

class Window:
    class Modes(enum.Enum):
        WINDOWED = 0
        MINIMIZED = 1
        HIDDEN = 2

    def __init__(self):
        self.mode = None
        self.screen = None
        self.__window = None

        self.set_mode(Window.Modes.WINDOWED)

    def set_mode(self, mode: Modes):
        if mode == Window.Modes.WINDOWED:
            monitor = screeninfo.get_monitors()[0]
            self.screen = pygame.display.set_mode((720, 480), pygame.RESIZABLE)
            self.__window = w.from_display_module()
            self.__window.position = (monitor.width / 2 - 720 / 2, monitor.height / 2 - 480 / 2)
        elif mode == Window.Modes.MINIMIZED:
            monitor = screeninfo.get_monitors()[0]
            self.screen = pygame.display.set_mode((300, 300), pygame.NOFRAME)
            self.__window = w.from_display_module()
            self.__window.position = (monitor.width - 310, monitor.height - 360)
        elif mode == Window.Modes.HIDDEN:
            monitor = screeninfo.get_monitors()[0]
            self.screen = pygame.display.set_mode((1, 1), pygame.HIDDEN)
            self.__window = w.from_display_module()
            self.__window.position = (0, 0)

        self.mode = mode
        pygame.display.set_caption("XNeko")
        pygame.display.set_icon(pygame.image.load("assets/icon.png").convert_alpha())