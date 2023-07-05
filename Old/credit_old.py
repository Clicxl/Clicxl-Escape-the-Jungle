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

exit_surf = font.render("Press Esc to exit",True,"White")
exit_rect = exit_surf.get_rect(center=(683,700))

credit = pygame.image.load('Assets/credits.jpg').convert_alpha()
credit_rect = credit.get_rect(center=(screen.get_rect().centerx,screen.get_rect().centery))


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.QUIT
			exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.QUIT
				exit()
			
	screen.blit(credit,credit_rect)
	screen.blit(exit_surf,exit_rect)
	pygame.display.update()
	clock.tick(60)