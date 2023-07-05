import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((1366,768))
pygame.display.set_caption("Clicxl : Escape The Jungle")
font  = pygame.font.Font('Assets/font/MinecraftFive-Bold.ttf',50)
font1  = pygame.font.Font('Assets/font/MinecraftFive-Bold.ttf',30)
clock = pygame.time.Clock()
icon  = pygame.image.load('Assets/icon.png').convert_alpha()
pygame.display.set_icon(icon)

main_surf = pygame.image.load('Assets/main-scr.jpg').convert_alpha()
main_rect = main_surf.get_rect(topleft=(0,0))
space_cont = font.render("Press space to Run",False,"White")
space_cont_rect =  space_cont.get_rect(center=(683,700))

while True:
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT:
      import credit_old
    if event.type == pygame.KEYDOWN :
      if event.key == pygame.K_ESCAPE:
        import credit_old
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE: 
        import game_old

  MENU_MOUSE_POS = pygame.mouse.get_pos()
  screen.blit(main_surf,main_rect)
  screen.blit(space_cont , space_cont_rect)
  screen_intro_music = pygame.mixer.Sound( 'Assets/audio/intro.wav')
  screen_intro_music.set_volume(0.025)
  screen_intro_music.play(-1,0,1000)


  pygame.display.update()
  clock.tick(60)