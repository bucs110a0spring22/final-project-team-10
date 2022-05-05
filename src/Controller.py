import apples
import background
import player

class Controller:
  
  def __init__(self, width=720, height=720):
    self.width = width
    self.height = height
    self.screen = pygame.display.set_mode((self.width, self.height))
    self.background = pygame.Surface(self.screen.get_size()).convert()
    self.backgroundImage = background.Background("background.png", [0,0], (width, height))
    self.player = player.Player("Snake", 0,0)
    
    
  def mainloop(self):
    #select state loop
    self.gameOn = True
    pygame.key.set_repeat(1, 1)
    while self.gameOn == True:
      self.background.fill((250, 250, 250))
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      if event.type == pygame.KEYDOWN:
        self.player.move(keys)
    self.gameOver = False
  
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
      gameoverloop_surface = font.render('Score: ' + str(score), True, purple )
      gameoverloop_surface_rect = gameoverloop_surface.get_rect()
      gameoverloop_rect.midtop = (windows_x, windows_y)
      pygame.quit()
      quit()

      #event loop

      #update data

      #redraw
