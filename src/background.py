import pygame
from pygame.locals import *
import random

def draw_square():
    surface.fill((110, 110, 5))
    surface.blit(square, (square_x, square_y))
    pygame.display.flip()

if __name__ == '__main__':
    pygame.init()

    surface = pygame.display.set_mode((500, 500))
    surface.fill((110, 110, 5))

    square = pygame.image.load("assets/square.png").convert()

    square_x, square_y = 100, 100

    surface.blit(square, (square_x, square_y))

    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_LEFT:
                    square_x -= 10
                    draw_square()
                if event.key == K_RIGHT:
                   square_x += 10
                    draw_square()
                if event.key == K_UP:
                    square_y -= 10
                    draw_square()
                if event.key == K_DOWN:
                    square_y += 10
                    draw_square()

            elif event.type == QUIT:
                running = False
                
class Background:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake Game")
    def render_background(self):
        bg = pygame.image.load("assets/background.jpg")
        self.surface.blit(bg, (0,0))

    def play(self):
        self.render_background()
        pygame.display.flip()  
