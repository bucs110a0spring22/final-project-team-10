import pygame

class Apple(pygame.sprite.Sprite):
  def__init__(self,pos,fn):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load(fn)
      self.rect = self.image.get_rect()

      self.rect.x = x
      self.rect.y = y
      
      x=pos[0]
      y=pos[0]
  

  def draw_apple(self):
      pygame.draw.rect(apple.png)