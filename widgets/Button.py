import pygame, colors

class Button:
    CIRCLE = (42, 42)

    def __init__(self, screen: pygame.Surface, text: tuple, action, position=(0, 0)):
        self.screen = screen
        self.text = text
        self.action = action
        self.position = position

        self.font_icon = pygame.font.Font("assets/MaterialSymbols.ttf", 24)
        self.font = pygame.font.Font("assets/Roboto.ttf", 16)
        self.width = 0
        self.hover = False

    def tick(self, delta):
        s = 0
        symbol = self.font_icon.render(self.text[0], True, colors.BUTTON_LABEL)
        text = self.font.render(self.text[1], True, colors.BUTTON_LABEL)

        if self.text[0]:
            s = symbol.get_size()[0]+10+text.get_size()[0]
        else:
            s = text.get_size()[0]

        pygame.draw.ellipse(self.screen, colors.BUTTON, (self.position[0], self.position[1], Button.CIRCLE[0], Button.CIRCLE[1]))
        pygame.draw.ellipse(self.screen, colors.BUTTON, (self.position[0]+s, self.position[1], Button.CIRCLE[0], Button.CIRCLE[1]))
        pygame.draw.rect(self.screen, colors.BUTTON, (self.position[0]+Button.CIRCLE[0]/2, self.position[1], s, Button.CIRCLE[1]))

        self.width = s + Button.CIRCLE[1]

        if self.text[0]:
            self.screen.blit(symbol, (self.position[0]+self.width/2-s/2, self.position[1]+Button.CIRCLE[1]/2-symbol.get_height()/2))
            self.screen.blit(text, (self.position[0]+self.width/2-s/2+symbol.get_width()+10, self.position[1]+Button.CIRCLE[1]/2-text.get_height()/2))
        else:
            self.screen.blit(text, (self.position[0]+self.width/2-text.get_width()/2, self.position[1]+Button.CIRCLE[1]/2-text.get_height()/2))

    def event(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEMOTION:
            self.hover = event.pos[0] > self.position[0] and event.pos[0] < self.position[0]+self.width and event.pos[1] > self.position[1] and event.pos[1] < self.position[1]+Button.CIRCLE[1]

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.hover:
                self.action()