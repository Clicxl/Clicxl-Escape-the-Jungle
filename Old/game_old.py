import pygame
from sys import exit
from random import randint,choice
pygame.init()
screen = pygame.display.set_mode((1366,768))
pygame.display.set_caption("Clicxl : Escape The Jungle")
font  = pygame.font.Font('Assets/font/MinecraftFive-Bold.ttf',50)
clock = pygame.time.Clock()
font1  = pygame.font.Font('Assets/font/MinecraftFive-Bold.ttf',30)
icon  = pygame.image.load('Assets/icon.png').convert_alpha()
pygame.display.set_icon(icon)


i = 0



#Game Difficulty 
# def game_diff(scr):
#   diff_var = 15
#   diff = 1500
#   if scr ==  diff_var : 
#     diff -= 1000
#     diff_var += 5
#   return diff 


#Score
def dis_score():
  cur_time =  int(pygame.time.get_ticks()/1000) - start_time
  score_surf = font.render(f'Score: {cur_time}',False,'#DCDCDC')
  score_rect = score_surf.get_rect(center=(1200,50))
  screen.blit(score_surf,score_rect)
  return cur_time

#Game Mechanics 
def obst_movement(obstac_list):
  if obstac_list :
    for obstacle_rect in obstac_list:
      obstacle_rect.x -= 12

      if obstacle_rect.bottom == 580:
        screen.blit(rand_obs,obstacle_rect)
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
    runner_index += 0.12
    if runner_index >= len(runner_run):
      runner_index = 0
    runner_surf = runner_run[int(runner_index)]

def Par_draw():
  for j in range(5):
    Par_eff = 1
    for a in Par_bg:
      screen.blit(a,((j*bg_wid)+i*Par_eff,0))
      Par_eff += 0.2

def draw_grd():
  for x in range(15):
    screen.blit(ground_1,((x*grd_widh)+i * 3.2,550))



start_time = 0
score = 0
game_state = True
high_score = 0

# Ground
ground_1= pygame.image.load('Assets/ground/ground.png').convert_alpha()
grd_widh = ground_1.get_width()
grd_hgt =  ground_1.get_height()
#Rock
rock_surf= pygame.image.load('Assets/obstacle/stone.png').convert_alpha()
rock_surf = pygame.transform.scale(rock_surf,(27*4,22*3+20))
log_surf = pygame.image.load('Assets/obstacle/log.png').convert_alpha()
log_surf = pygame.transform.scale(log_surf,(27*4+15,22*3+5))
rand_obs = choice([rock_surf,log_surf])

#Sky Obs
bird_fly_3 = pygame.image.load('Assets/bird/bird_fly3.png').convert_alpha()
bird_fly_3 = pygame.transform.scale(bird_fly_3,(27*4,22*3))
bird_fly_2 = pygame.image.load('Assets/bird/bird_fly2.png').convert_alpha()
bird_fly_2 = pygame.transform.scale(bird_fly_2,(27*4,22*2+8))
bird_fly_1 = pygame.image.load('Assets/bird/bird_fly1.png').convert_alpha()
bird_fly_1 = pygame.transform.scale(bird_fly_1,(27*4,22*3))
monkey_surf = pygame.image.load('Assets/bird/monkey.png')
bird_index = 0 
bird_fly = [bird_fly_3,bird_fly_2,bird_fly_1]
bird_surf  = bird_fly[bird_index]

bg_rect_list = []
obstr_rect_list =  []


# Paralax Effect
Par_bg = []
for i in range(1,6):
  Par_bg_img = pygame.image.load(f'Assets/sky/Sky_{i}.png').convert_alpha()
  Par_bg_img = pygame.transform.scale(Par_bg_img,(1366,768-100))
  Par_bg.append(Par_bg_img)
bg_wid = Par_bg[0].get_width()


#Player 
# runner_stand = pygame.image.load('player/player_stand.png').convert_alpha()
# runner_stand = pygame.transform.scale(runner_stand,(14*6,35*5))
runner_run_1 = pygame.image.load('Assets/player/player_walk_1.png').convert_alpha()
runner_run_1 = pygame.transform.scale(runner_run_1,(14*10,35*5))
runner_run_2 = pygame.image.load('Assets/player/player_walk_2.png').convert_alpha()
runner_run_2 = pygame.transform.scale(runner_run_2,(14*7.5,35*5))
runner_run_3 = pygame.image.load('Assets/player/player_walk_3.png').convert_alpha()
runner_run_3 = pygame.transform.scale(runner_run_3,(14*10,35*5))
runner_run = [runner_run_1,runner_run_2,runner_run_3]
runner_index = 0
runner_jump = pygame.image.load('Assets/player/player_jump.png').convert_alpha()
runner_jump = pygame.transform.scale(runner_jump,(14*10,35*5.75))
runner_surf = runner_run[runner_index]
runner_rect = runner_surf.get_rect(midbottom=(200,580))
player_grav = 0


#End Screen
end_surf = pygame.image.load('Assets/endscreen.png').convert_alpha()
end_rect = end_surf.get_rect(topleft=(0,0))



bird_timer = pygame.USEREVENT + 2
pygame.time.set_timer(bird_timer,180)

#Timer
obstrical_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstrical_timer,1400) # Main Switch For Enemy


while True:
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT:
      import credit_old
    if event.type == pygame.KEYDOWN :
      if event.key == pygame.K_ESCAPE:
        import credit_old 



  #Gravity Cont
    if game_state == True: 
      diff_time = pygame.time.get_ticks()
      if event.type == pygame.MOUSEBUTTONDOWN and runner_rect.bottom == 580:
        if runner_rect.collidepoint(event.pos): 
          player_grav = -26.5
          player_jump_sound = pygame.mixer.Sound('Assets/audio/jump.mp3')
          player_jump_sound.set_volume(0.25)
          player_jump_sound.play()          
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE and runner_rect.bottom ==  580:
          player_grav = -26.5
          player_jump_sound = pygame.mixer.Sound('Assets/audio/jump.mp3')
          player_jump_sound.set_volume(0.25)
          player_jump_sound.play()


      #Game Mechanics     
      if event.type == obstrical_timer:
        custom_spawn = randint(1,4)
        if custom_spawn == 1 or custom_spawn == 2 or  custom_spawn == 3 and randint(0,2):
          obstr_rect_list.append(rand_obs.get_rect(midbottom=(randint(1385,1500),580)))
        elif custom_spawn == 4:
          obstr_rect_list.append(bird_surf.get_rect(midbottom=(randint(1385,1500),355)))



      #Bird Animation
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
    Par_draw()
    draw_grd()
    # screen.blit(ground_1,(i,550))
    # screen.blit(ground_1,(width+i,550))


    if i <= -1366:
      screen.blit(Par_bg_img,(1366+i,0))
      screen.blit(ground_1,(1366+i,550))
      i = 0

    i -= 4

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

  elif game_state == False:
    
    
    score_msg=font.render(f'Your Score: {score}',False,'#90A6FF')
    score_msg_rect = score_msg.get_rect(center=(600,200))
    end_msg = font.render('Press Space to continue',False,'#90A6FF')
    end_msg_rect = end_msg.get_rect(center=(1366/2,600))
    obstr_rect_list.clear()
    runner_rect.midbottom = (200,580)
    player_grav = 0

    #High Score
    if high_score<=score:
      high_score = score 
    high_scr_msg=font.render(f'Your High Score: {high_score}',False,'#90A6FF')
    high_scr_msg_rect = high_scr_msg.get_rect(center=(687,300))
    
    screen.blit(end_surf,end_rect)
    screen.blit(score_msg,score_msg_rect)
    screen.blit(end_msg,end_msg_rect)
    screen.blit(high_scr_msg,high_scr_msg_rect)

    death= pygame.mixer.Sound('Assets/audio/death.mp3')
    death.set_volume(0.25)
    death.play(0)
    i = 0


  pygame.display.update()
  clock.tick(60)