import pygame, os, buildConfig, colors

from widgets.IconButton import IconButton

class FooterIcon(IconButton):
    def tick(self, delta):
        pygame.draw.ellipse(self.screen, (colors.FOOTER, colors.FOOTER_ICON_HOVER)[self.hover], (self.position[0], self.position[1], IconButton.SIZE[0], IconButton.SIZE[1]))
        sd = self.font.render(self.symbol, True, colors.FOOTER_LABEL)
        self.screen.blit(sd, (self.position[0] + (IconButton.SIZE[0] / 2 - sd.get_size()[0] / 2), self.position[1] + (IconButton.SIZE[1] / 2 - sd.get_size()[1] / 2)))