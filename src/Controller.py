import apples
import background
import player

class Controller:
  
  def __init__(self, width=720, height=720):
    self.width = width
    self.height = height
		self.screen = pygame.display.set_mode(self.width, self.height)
    self.background = pygame.Surface(self.screen.get_size()).convert()
		self.backgroundImage = background.Background("background.png", [0,0], (width, height))
    
  def mainloop(self):
    #select state loop
    
  
  ### below are some sample loop states ###

  def menuloop(self):
    
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
      font = pygame.font.Font(None, size)
      game_over_surface = font.render('Score: ' + str(score), True, purple )
      game_over_rect = game_over_surface.get_rect()
      game_over_rect.midtop = (windows_x, windows_y)
      pygame.quit()
      quit()

      #event loop

      #update data

      #redraw
