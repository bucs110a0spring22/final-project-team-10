import os, sys, random
import pygame

def load_image(name, colorkey=None):
  	fullname = os.path.join('assets', name)
  	try:
  		image = pygame.image.load(fullname)
  	except pygame.error as message:
  		print('Cannot load image:', name)
  		raise SystemExit(message)
  	image = image.convert()
  	if colorkey is not None:
  		if colorkey is -1:
  			colorkey = image.get_at((0,0))
  		image.set_colorkey(colorkey)
  	return image
  
class Player(pygame.sprite.Sprite):

    
  def __init__(self, name, x, y):
    self.name = name
    pygame.sprite.Sprite.__init__(self)
    
    self.image = pygame.image.load("user-snake.png")
    self.rect = self.image.get_rect()
    
    self.rect.x = x
    self.rect.y = y
      
  def move(self):
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        self.rect.x = self.rect.x - 1
    elif keys[pygame.K_RIGHT]:
        self.rect.x = self.rect.x + 1
    elif keys[pygame.K_UP]:
        self.rect.y = self.rect.y + 1
    elif keys[pygame.K_DOWN]:
        self.rect.y = self.rect.y - 1