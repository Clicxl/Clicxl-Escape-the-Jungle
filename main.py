import pygame
from PIL import Image
from sys import exit
import main_menu,game
pygame.init()
screen = pygame.display.set_mode((1366,768))
font  = pygame.font.Font('font/MinecraftFive-Bold.ttf',50)
clock = pygame.time.Clock()

icon  = pygame.image.load('player/player_default.png').convert_alpha()
pygame.display.set_icon(icon)

while True:
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT:
      pygame.QUIT 
      exit()
  main_menu() 

  pygame.display.update()
  clock.tick(60)

# Song by Music by Pixabay