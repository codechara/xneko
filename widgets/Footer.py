import pygame, colors, buildConfig

from widgets.FooterIcon import FooterIcon

class Footer:
    HEIGHT = 64

    def __init__(self, screen: pygame.Surface, title="Footer"):
        self.screen = screen
        self.title = title

        self.icon_left: FooterIcon = None
        self.icon_right: FooterIcon = None

        self.font = pygame.font.Font("assets/Roboto.ttf", 22)

    def tick(self, delta):
        footer = pygame.Surface((self.screen.get_width(), Footer.HEIGHT))
        footer.fill(colors.FOOTER)
        footer_title = self.font.render(self.title, True, colors.FOOTER_LABEL)

        if self.icon_left:
            footer.blit(footer_title, (64, 64/2-footer_title.get_height()/2))
        else:
            footer.blit(footer_title, (22, 64/2-footer_title.get_height()/2))

        self.screen.blit(footer, (0, 0))

        if self.icon_left:
            self.icon_left.position = (12, 12)
            self.icon_left.tick(delta)

        if self.icon_right:
            self.icon_right.position = (self.screen.get_width()-FooterIcon.SIZE[0]-12, 12)
            self.icon_right.tick(delta)

    def event(self, event):
        if self.icon_left:
            self.icon_left.event(event)

        if self.icon_right:
            self.icon_right.event(event)