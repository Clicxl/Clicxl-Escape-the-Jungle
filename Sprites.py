import pygame,sys
from pygame.locals import *
from Settings import *

class Player(pygame.sprite.Sprite):
  def __init__(self,game,x,y,jump):
    self.game = game
    self._layer = PLAYER_LAYER
    self.groups = self.game.all_sprites
    super().__init__(self.groups)
    
    self.x = x
    self.y = y
    self.jump = jump
    
    self.image = pygame.image.load('Assets/player/player_stand.png').convert_alpha()
    self.image = pygame.transform.scale(self.image,(14*10,35*5))
    self.rect = self.image.get_rect()
    self.rect.x = self.x
    self.rect.y = self.y
    
  def update(self):
      pass
    
    