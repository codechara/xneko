import pygame.event

from screen_manager import Screen

class ExampleScreen(Screen):
    def setup(self):
        self.state = False

        self.font = pygame.font.Font("assets/Roboto.ttf", 36)

    def tick(self, delta):
        if self.state:
            self.screen.fill((0, 0, 255))
        else:
            self.screen.fill((255, 0, 0))

        render = self.font.render("Tap on the window!", True, (0, 0, 0))
        self.screen.blit(render, (self.screen.get_size()[0]/2-render.get_size()[0]/2, self.screen.get_size()[1]/2-render.get_size()[1]/2))

    def event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.state = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.state = False