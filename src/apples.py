import pygame

class apple(pygame.sprite.Sprite):
  def __init__(self,pos,apple.png):
      pygame.sprite.Sprite.__init__(self)
      self.image = pygame.image.load(apple.png)
      self.rect = self.image.get_rect()

      self.rect.x = x
      self.rect.y = y
      
      x=pos[0]
      y=pos[0]
  

  def draw_apple(self):
      pygame.draw.rect(apple.png)


#reminder for m (dont mind this lol): apples need a value to keep score