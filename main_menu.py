import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((1366,768))
pygame.display.set_caption("Clicxl : Escape The Jungle")
font  = pygame.font.Font('Assets/font/MinecraftFive-Bold.ttf',50)
font_bor = pygame.font.Font('Assets/font/MinecraftFive-Bold.ttf',55)
clock = pygame.time.Clock()
icon  = pygame.image.load('Assets/player/player_default.png').convert_alpha()
pygame.display.set_icon(icon)
# studio = font.render('Thunder.py',False,'White')
# studio_rect = studio.get_rect(center=(1366/2,768/2))

def main_menu():
  global logo,logo_rect,main_sruf,main_rect,space_cont,space_cont_rect
  main_sruf = pygame.image.load('Assets/main-scr.jpg').convert_alpha()
  main_rect = main_sruf.get_rect(topleft=(0,0))
  space_cont = font.render("Press space to Run",False,"White")
  space_cont_rect =  space_cont.get_rect(center=(683,700))

while True:
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT:
      pygame.QUIT 
      exit()
    main_menu()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE: 
        import game
  


  MENU_MOUSE_POS = pygame.mouse.get_pos()
  # Studio Name
  # screen.fill('Black')
  # # screen.blit(studio,studio_rect)
  # pygame.time.wait(5000)

  screen.blit(main_sruf,main_rect)
  screen.blit(space_cont , space_cont_rect)
  screen_intro_music = pygame.mixer.Sound('Assets/audio/intro.wav')
  screen_intro_music.set_volume(0.025)
  screen_intro_music.play(-1,0,1000)
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_SPACE:
        screen.fill('#000000')
        pygame.time.wait(2500)


  pygame.display.update()
  clock.tick(60)