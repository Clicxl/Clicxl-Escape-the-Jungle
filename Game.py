import pygame,sys
from pygame.locals import *
from Settings import *
from Sprites import *

class Game:
  def __init__(self):
    pygame.init()
    self.clock = pygame.time.Clock()
    self.screen = pygame.display.set_mode(SCREEN)
    self.Bigfont = pygame.font.Font('Assets/font/MinecraftFive-Bold.ttf',50)
    self.Smallfont = pygame.font.Font('Assets/font/MinecraftFive-Bold.ttf',30)
    self.Running = True
  
  def new(self):
    self.Playing = True
    self.all_sprites = pygame.sprite.LayeredUpdates()
    self.obsticals = pygame.sprite.LayeredUpdates()
    
    self.player = Player(self,580,200,50)
  def events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and pygame.key.get_pressed()[K_ESCAPE]):
        pygame.quit()
        sys.exit()
        
  def update(self):
    self.all_sprites.update()
  def draw(self):
    self.screen.fill('Black')
    self.all_sprites.draw(self.screen)
    self.clock.tick()
    pygame.display.flip()
  def main(self):
    while True:
      self.events()
      self.update()
      self.draw()
  def game_over(self):
    pass
  def intro_screen(self):
    pass
  
if __name__ == '__main__':
  Game = Game()
  Game.intro_screen()
  Game.new()
  Game.main()