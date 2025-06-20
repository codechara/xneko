import pygame

class Window:
    HIDDEN = 0
    WINDOWED = 1
    MINIMIZED = 2

    def __init__(self):
        self._screen = None
        self._mode = None

    def set_mode(self, mode: int) -> None:
        self._mode = mode

        if self._mode == Window.HIDDEN:
            pass