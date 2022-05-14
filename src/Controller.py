# importing libraries
import pygame
import time
import random 

from src import apple
from src import snake

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Snake Game")
fps = pygame.time.Clock()



window_x = 480
window_y = 480

#start window#
start_window = pygame.display.set_mode((window_x, window_y))
font = pygame.font.SysFont(None, 30)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    start_window.blit(screen_text, [x, y])
  
def start():
    exit_game = False
    while not exit_game:
        start_window.fill(("light blue"))
        text_screen("Snake Game", "black", 170, 90)
        text_screen("by Team 10", "black", 180, 130)
        text_screen("Press the space bar to play", "black", 110, 220)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_window() #IDK WHAT TO PUT HERE
                  
        pygame.display.update()
        fps.tick(60)

#start()
#######

game_window = pygame.display.set_mode((window_x, window_y))
background = pygame.image.load("assets/background.jpg")

# snake
snake_position = [0, 0]
snake_body = [[100, 42.5]]
snake_speed = 5

# apple
x_coordinates = [0, 40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440]
y_coordinates = [0, 40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440]

apple_position = [random.choice(x_coordinates), random.choice(y_coordinates)]

apple_img = pygame.image.load("assets/apple.png")
apple_regenerate = True

# setting the direction
direction = 'RIGHT'
change_to = direction

score = 0

  
# showing the score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)


# end screen - game over
def gameover():
    my_font = pygame.font.SysFont('times new roman', 40)
    gameover_text = my_font.render('Game Over | Score: ' + str(score), True,
                                   'red','white')
    gameover_rect = gameover_text.get_rect()

    gameover_rect.midtop = (window_x / 2, window_y / 2)

    game_window.blit(gameover_text, gameover_rect)
    pygame.display.flip()
  ###


    time.sleep(5)
    pygame.quit()
    quit()


def snake():
    pygame.draw.rect(game_window, 'forestgreen',
                     pygame.Rect(pos[0], pos[1], 40, 40))


def apple():
    pygame.draw.rect(
        game_window, 'gray',
        pygame.Rect(apple_position[0], apple_position[1], 0.5, 0.5))
    game_window.blit(apple_img, apple_position)


# MainLoop (continous)
while True:
    game_window.blit(background, (0, 0))
    # key clicks
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # if multiple keys are clicked
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'

    # user controlled snake
    if direction == 'UP':
        snake_position[1] -= 40
    if direction == 'DOWN':
        snake_position[1] += 40
    if direction == 'LEFT':
        snake_position[0] -= 40
    if direction == 'RIGHT':
        snake_position[0] += 40

    # snake growing
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == apple_position[0] and snake_position[
            1] == apple_position[1]:
        score += 1
        apple_regenerate = False
    else:
        snake_body.pop()

    if not apple_regenerate:
        apple_position = [
            random.choice(x_coordinates),
            random.choice(y_coordinates)
        ]

    apple_regenerate = True

    #snake & apple location!
    for pos in snake_body:
        snake()
        apple()

    # for when the snake dies :(
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        gameover()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        gameover()

    # eating the apple! munch munch
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
          pygame.mixer.Sound("resources/ding.mp3")
          gameover()

      
    # THE score !!
    show_score(1, 'white', 'times new roman', 20)
    pygame.display.update()
    fps.tick(snake_speed)

    # increases speed when the score more than 7
    if score > 7:
        snake_speed += 0.25
        fps.tick(snake_speed)


