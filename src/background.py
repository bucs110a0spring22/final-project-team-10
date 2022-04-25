class Background:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake Game")
    def render_background(self):
        bg = pygame.image.load("assets/background.jpg")
        self.surface.blit(bg, (0,0))

    def play(self):
        self.render_background()
        #self.snake.walk()
        #self.apple.draw()
        #self.display_score()
        pygame.display.flip()  
