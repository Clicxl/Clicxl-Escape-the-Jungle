import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((1366,768))
pygame.display.set_caption("Clicxl : Escape The Jungle")
font  = pygame.font.Font('Assets/font/MinecraftFive-Bold.ttf',50)
clock = pygame.time.Clock()
font1  = pygame.font.Font('Assets/font/MinecraftFive-Bold.ttf',30)
icon  = pygame.image.load('Assets/icon.png').convert_alpha()
pygame.display.set_icon(icon)




while True:
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT:
      import credit_old
    if event.type == pygame.KEYDOWN :
      if event.key == pygame.K_ESCAPE:
        import credit_old  
  import loading_old



  pygame.display.update()
  clock.tick(60)

# Song by Music by Pixabay