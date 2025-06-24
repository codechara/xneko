import pygame, colors

class IconButton:
    SIZE = (42, 42)

    def __init__(self, screen: pygame.Surface, symbol: str, action, position=(0, 0)):
        self.screen = screen
        self.symbol = symbol
        self.position = position
        self.action = action

        self.font = pygame.font.Font("assets/MaterialSymbols.ttf", 24)
        self.hover = False

    def tick(self, delta):
        pygame.draw.ellipse(self.screen, (colors.ICON_BUTTON, colors.ICON_BUTTON_HOVER)[self.hover], (self.position[0], self.position[1], IconButton.SIZE[0], IconButton.SIZE[1]))
        sd = self.font.render(self.symbol, True, colors.ICON_BUTTON_ICON)
        self.screen.blit(sd, (self.position[0]+(IconButton.SIZE[0]/2-sd.get_size()[0]/2), self.position[1]+(IconButton.SIZE[1]/2-sd.get_size()[1]/2)))

    def event(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEMOTION:
            self.hover = event.pos[0] > self.position[0] and event.pos[0] < self.position[0]+IconButton.SIZE[0] and event.pos[1] > self.position[1] and event.pos[1] < self.position[1] + IconButton.SIZE[1]

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hover:
                self.action()