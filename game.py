import pygame
from sys import exit
from random import randint
pygame.init()
screen = pygame.display.set_mode((1366,768))
font  = pygame.font.Font('font/MinecraftFive-Bold.ttf',50)
clock = pygame.time.Clock()
icon  = pygame.image.load('player/player_default.png').convert_alpha()
pygame.display.set_icon(icon) 
#Score
def dis_score():
  cur_time =  int(pygame.time.get_ticks()/1000) - start_time
  score_surf = font.render(f'Score: {cur_time}',False,(64,64,64))
  score_rect = score_surf.get_rect(center=(683,150))
  screen.blit(score_surf,score_rect)
  return cur_time

#Game Mechanics 
def obst_movement(obstac_list):
  if obstac_list:
    for obstacle_rect in obstac_list:
      obstacle_rect.x -= 5.5

      if obstacle_rect.bottom == 580:
        screen.blit(rock_surf,obstacle_rect)
      else:
        screen.blit(bird_surf,obstacle_rect)
    obstac_list = [obstacle for obstacle in obstac_list if obstacle.x > -100]
    return obstac_list
  else:
    return []

def collisions(player,obstacles):
  if obstacles:
    for obstacle_rect in obstacles:
      if player.colliderect(obstacle_rect):
        return False
  return True

def runner_ani():
  global runner_surf,runner_index
  if runner_rect.bottom < 580:
    runner_surf = runner_jump
  else:
    runner_index += 0.1
    if runner_index >= len(runner_run):
      runner_index = 0
    runner_surf = runner_run[int(runner_index)]

  # Walking anime on floor 
  # Player jump when not on floor

start_time = 0
score = 0
game_state = True


# Ground
ground_sruf = pygame.image.load('ground.png').convert_alpha()
ground_rect = ground_sruf.get_rect(topleft=(-1,550))
#Sky
sky_surf = pygame.image.load('sky1.png').convert_alpha()
sky_rect =  sky_surf.get_rect(topleft=(0,-20))

#Rock
rock_surf= pygame.image.load('Stone/stone.png').convert_alpha()
rock_surf = pygame.transform.scale(rock_surf,(27*4,22*3+10))

#Bird
bird_fly_3 = pygame.image.load('bird/bird_fly3.png').convert_alpha()
bird_fly_3 = pygame.transform.scale(bird_fly_3,(27*4,22*3))
bird_fly_2 = pygame.image.load('bird/bird_fly2.png').convert_alpha()
bird_fly_2 = pygame.transform.scale(bird_fly_2,(27*4,22*2+8))
bird_fly_1 = pygame.image.load('bird/bird_fly1.png').convert_alpha()
bird_fly_1 = pygame.transform.scale(bird_fly_1,(27*4,22*3))
bird_index = 0 
bird_fly = [bird_fly_3,bird_fly_2,bird_fly_1]
bird_surf  = bird_fly[bird_index]
# bird_surf = pygame.transform.scale(bird_surf,(27*4,22*3))


obstr_rect_list =  []

#Player 
# runner_stand = pygame.image.load('player/player_stand.png').convert_alpha()
# runner_stand = pygame.transform.scale(runner_stand,(14*6,35*5))
runner_run_1 = pygame.image.load('player/player_walk_1.png').convert_alpha()
runner_run_1 = pygame.transform.scale(runner_run_1,(14*10,35*5))
runner_run_2 = pygame.image.load('player/player_walk_2.png').convert_alpha()
runner_run_2 = pygame.transform.scale(runner_run_2,(14*7.5,35*5))
runner_run_3 = pygame.image.load('player/player_walk_3.png').convert_alpha()
runner_run_3 = pygame.transform.scale(runner_run_3,(14*10,35*5))
runner_run = [runner_run_1,runner_run_2,runner_run_3]
runner_index = 0
runner_jump = pygame.image.load('player/player_jump.png').convert_alpha()
runner_jump = pygame.transform.scale(runner_jump,(14*9,35*5))
runner_surf = runner_run[runner_index]
runner_rect = runner_surf.get_rect(midbottom=(200,580))
player_grav = 0

#End Screen
end_surf = pygame.image.load('endscreen.png').convert_alpha()
end_rect = end_surf.get_rect(topleft=(0,0))

#Timer
obstrical_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstrical_timer,2500) # Main Switch For Enemy

bird_timer = pygame.USEREVENT + 2
pygame.time.set_timer(bird_timer,200)

while True:
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT:
      pygame.QUIT
      exit()

  #Gravity Cont
    if game_state == True: 
      if event.type == pygame.MOUSEBUTTONDOWN and runner_rect.bottom == 580:
        if runner_rect.collidepoint(event.pos): 
          player_grav = -29
          player_jump_sound = pygame.mixer.Sound('audio/jump.mp3')
          player_jump_sound.set_volume(0.25)
          player_jump_sound.play()          
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE and runner_rect.bottom ==  580:
          player_grav = -29
          player_jump_sound = pygame.mixer.Sound('audio/jump.mp3')
          player_jump_sound.set_volume(0.25)
          player_jump_sound.play()

      #Game Mechanics     
      if event.type == obstrical_timer:
        custom_spwan = randint(0,4)
        if custom_spwan == 1 or custom_spwan == 2 or  custom_spwan == 3 and randint(0,2):
          obstr_rect_list.append(rock_surf.get_rect(midbottom=(randint(1400,1600),580)))
        elif custom_spwan == 4:
          obstr_rect_list.append(bird_surf.get_rect(midbottom=(randint(1400,1600),355)))

      if event.type == bird_timer:
        if bird_index == 0:
          bird_index = 1
        elif bird_index == 1:
          bird_index = 2
        else:
          bird_index = 0
        bird_surf = bird_fly[bird_index] 

    else:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          game_state = True
          start_time = int(pygame.time.get_ticks()/1000)




  if game_state ==  True:
    screen.blit(sky_surf,sky_rect)
    screen.blit(ground_sruf,ground_rect)
    score = dis_score()


    player_grav += 1
    runner_rect.y += player_grav 
    if runner_rect.bottom >= 580:
      runner_rect.bottom = 580
    runner_ani()
    screen.blit(runner_surf,runner_rect)

    # Obstacle Movement
    obstr_rect_list =obst_movement(obstr_rect_list)  


    #Collisions
    game_state = collisions(runner_rect,obstr_rect_list)

  else:
    score_msg=font.render(f'Your Score: {score}',False,'#90A6FF')
    score_msg_rect = score_msg.get_rect(center=(600,200))
    end_msg = font.render('Press Space to continue',False,'#90A6FF')
    end_msg_rect = end_msg.get_rect(center=(1366/2,600))
    obstr_rect_list.clear()
    runner_rect.midbottom = (100,580)
    player_grav = 0
    
    screen.blit(end_surf,end_rect)
    screen.blit(score_msg,score_msg_rect)
    screen.blit(end_msg,end_msg_rect)
    death= pygame.mixer.Sound('audio/death.mp3')
    death.set_volume(0.25)
    death.play(1)
    
  pygame.display.update()
  clock.tick(60)