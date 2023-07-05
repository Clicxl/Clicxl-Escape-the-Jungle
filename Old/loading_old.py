# Imports
import pygame, sys, threading
from random import choice

pygame.init()

# Screen and font
screen = pygame.display.set_mode((1366,768))
pygame.display.set_caption("Clicxl : Escape The Jungle")
font  = pygame.font.Font('Assets/font/MinecraftFive-Bold.ttf',50)
clock = pygame.time.Clock()
font1  = pygame.font.Font('Assets/font/MinecraftFive-Bold.ttf',30)
icon  = pygame.image.load('Assets/icon.png').convert_alpha()
pygame.display.set_icon(icon)
font1  = pygame.font.Font('Assets/font/MinecraftFive-Bold.ttf',30)

# Loading Bar and variables
loading_bar = pygame.image.load("Assets/loading_bar.png")
loading_bar_rect = loading_bar.get_rect(center=(1366/2, 768-37))
loading_finished = False
loading_progress = 0
loading_bar_width = 0

def doWork():
	# Do some math WORK amount times
	global loading_finished, loading_progress

	for i in range(50100000):
		math_equation = 523687 / 789456 * 89456
		loading_progress = i 

	loading_finished = True

# Finished text
studio = font.render("Thunder.py", False, "Black")
studio_rect = studio.get_rect(center=(640, 360))

ver_txt = font1.render('V2.1',True,'#585858')
ver_txt_rect = ver_txt.get_rect(midleft=(10,10))

sub_list = choice(['RESHAPING FOREST','CARVING LAYOUT','CLEARING DARKNESS','WARMING UP','FINDING BEST PATH','HAVE YOUR TRIED WORLD BUILDER'])
sub_txt = font1.render(f'{sub_list}...',True,'#585858')
sub_txt_rect = sub_txt.get_rect(midright=(1340,768-75))



# Thread
threading.Thread(target=doWork).start()

loading_timer = pygame.USEREVENT + 2
pygame.time.set_timer(loading_timer,180)

# Game loop
while True:
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT:
      import credit_old
    if event.type == pygame.KEYDOWN :
      if event.key == pygame.K_ESCAPE:
        import credit_old

  screen.fill("White")
  screen.blit(studio,studio_rect)
  screen.blit(sub_txt,sub_txt_rect)
  screen.blit(ver_txt,ver_txt_rect)

  loading_bar_width = loading_progress / 50000000 * 1370
  loading_bar = pygame.transform.scale(loading_bar, (int(loading_bar_width), 50))
  loading_bar_rect = loading_bar.get_rect(midleft=(0, 768-25))
  screen.blit(loading_bar, loading_bar_rect)

  if loading_finished == True:
    import main_menu_old

  pygame.display.update()
  clock.tick(60)

