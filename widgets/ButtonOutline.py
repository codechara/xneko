import pygame, colors

from widgets.Button import Button

class ButtonOutline(Button):
    def tick(self, delta):
        s = 0
        symbol = self.font_icon.render(self.text[0], True, colors.BUTTON_OUTLINE_LABEL)
        text = self.font.render(self.text[1], True, colors.BUTTON_OUTLINE_LABEL)

        if self.text[0]:
            s = symbol.get_size()[0]+10+text.get_size()[0]
        else:
            s = text.get_size()[0]

        pygame.draw.ellipse(self.screen, colors.BUTTON_OUTLINE_OUTLINE, (self.position[0], self.position[1], Button.CIRCLE[0], Button.CIRCLE[1]))
        pygame.draw.ellipse(self.screen, colors.BUTTON_OUTLINE_OUTLINE, (self.position[0]+s, self.position[1], Button.CIRCLE[0], Button.CIRCLE[1]))
        pygame.draw.rect(self.screen, colors.BUTTON_OUTLINE_OUTLINE, (self.position[0]+Button.CIRCLE[0]/2, self.position[1], s, Button.CIRCLE[1]))

        pygame.draw.ellipse(self.screen, (colors.BUTTON_OUTLINE, colors.BUTTON_OUTLINE_HOVER)[self.hover], (self.position[0]+1, self.position[1]+1, Button.CIRCLE[0]-2, Button.CIRCLE[1]-2))
        pygame.draw.ellipse(self.screen, (colors.BUTTON_OUTLINE, colors.BUTTON_OUTLINE_HOVER)[self.hover], (self.position[0]+1+s, self.position[1]+1, Button.CIRCLE[0]-2, Button.CIRCLE[1]-2))
        pygame.draw.rect(self.screen, (colors.BUTTON_OUTLINE, colors.BUTTON_OUTLINE_HOVER)[self.hover], (self.position[0]+1+Button.CIRCLE[0]/2, self.position[1]+1, s, Button.CIRCLE[1]-2))

        self.width = s + Button.CIRCLE[1]

        if self.text[0]:
            self.screen.blit(symbol, (self.position[0]+self.width/2-s/2, self.position[1]+Button.CIRCLE[1]/2-symbol.get_height()/2))
            self.screen.blit(text, (self.position[0]+self.width/2-s/2+symbol.get_width()+10, self.position[1]+Button.CIRCLE[1]/2-text.get_height()/2))
        else:
            self.screen.blit(text, (self.position[0]+self.width/2-text.get_width()/2, self.position[1]+Button.CIRCLE[1]/2-text.get_height()/2))
