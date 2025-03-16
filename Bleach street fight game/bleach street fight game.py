import pygame
from pygame import mixer
from fighter import Fighter

pygame.init()

#create game window
SCREEN_WIDTH = 1460
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bleach chaos")

#set framerate
clock = pygame.time.Clock()
FPS = 60

#define colours
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#define game variables
intro_count = 3
last_count_update = pygame.time.get_ticks()
score = [0, 0]#player score. [p1, p2]
round_over = False
ROUND_OVER_COOLDOWN = 2000


#define fighter variable
SHINIGAMI_SIZE = 128
SHINIGAMI_SCALE = 3
SHINIGAMI_OFFSET = [48, 42]
SHINIGAMI_DATA = [SHINIGAMI_SIZE, SHINIGAMI_SCALE, SHINIGAMI_OFFSET]
AIZEN_SIZE = 128
AIZEN_SCALE = 3
AIZEN_OFFSET = [51, 40]
AIZEN_DATA = [AIZEN_SIZE,AIZEN_SCALE, AIZEN_OFFSET]

#load music and sounds
pygame.mixer.music.load("assets/audio/Haruka Kanata.mp3")
pygame.mixer_music.set_volume(0.2)
pygame.mixer.music.play(-1, 0.0, 5000)
knife_fx = pygame.mixer.Sound("assets/audio/sword.mp3")
knife_fx.set_volume(0.75)
punch_fx = pygame.mixer.Sound("assets/audio/punch.mp3")
punch_fx.set_volume(0.5)


#load background image
bg_image = pygame.image.load("assets/images/background/bleach world.png").convert_alpha()

#load spritesheets
shinigami_sheet = pygame.image.load("assets/images/ichigo sprites/shinigami.png").convert_alpha()
aizen_sheet = pygame.image.load("assets/images/Aizen sprites/aizen.png").convert_alpha()

#load victory image
victory_img = pygame.image.load("assets/icons/victory.png").convert_alpha()

#display icon on window
icon = pygame.image.load("assets/icons/bleach.png").convert_alpha()
pygame.display.set_icon(icon)


#define number of steps in each animation
SHINIGAMI_ANIMATION_STEPS = [6, 8, 10, 4, 3, 3, 3]
AIZEN_ANIMATION_STEPS = [6, 8, 12, 5, 3, 2, 3]

#define font
count_font = pygame.font.Font("assets/fonts/turok.ttf", 80)
score_font = pygame.font.Font("assets/fonts/turok.ttf", 30)

#function for drawing text
def draw_text(text, font, text_col, x, y):
   img = font.render(text,True, text_col)
   screen.blit(img, (x, y))

#function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

#function for drawing fighter health bars
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, BLACK, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, WHITE, (x, y, 400, 30))
    pygame.draw.rect(screen, RED, (x, y, 400 * ratio, 30))

#create two instances of fighters
fighter_1 = Fighter(1, 300, 500, False, SHINIGAMI_DATA, shinigami_sheet, SHINIGAMI_ANIMATION_STEPS, punch_fx)
fighter_2 = Fighter(2, 1100, 500, True, AIZEN_DATA, aizen_sheet, AIZEN_ANIMATION_STEPS, knife_fx)

#game loop
run = True
while run:
    clock.tick(FPS)

    #draw background
    draw_bg()

    #show player stats
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 1040, 20)
    draw_text("Ichigo: " + str(score[0]), score_font, BLACK, 20, 60)
    draw_text("Aizen: " + str(score[1]), score_font, BLACK, 1040, 60)
    #update countdown
    if intro_count <= 0: 
      #move fighters
      fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, round_over)
      fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, round_over)
    else:
      #display count timer
      draw_text(str(intro_count), count_font, BLACK, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
      #update count timer
      if (pygame.time.get_ticks() - last_count_update) >= 1000:
         intro_count -= 1
         last_count_update = pygame.time.get_ticks()  
         



    #update fighters
    fighter_1.update()
    fighter_2.update()

    #draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    #check for player defeat
    if round_over == False:
        if fighter_1.alive == False:
           score[1] += 1
           round_over = True
           round_over_time = pygame.time.get_ticks()
        elif fighter_2.alive == False:
           score[0] += 1
           round_over = True
           round_over_time = pygame.time.get_ticks()
    else:
      #display victory image
       screen.blit(victory_img, (600, 200))
       if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
          round_over = False
          intro_count = 3           
          fighter_1 = Fighter(1, 300, 500, False, SHINIGAMI_DATA, shinigami_sheet, SHINIGAMI_ANIMATION_STEPS, punch_fx)
          fighter_2 = Fighter(2, 1100, 500, True, AIZEN_DATA, aizen_sheet, AIZEN_ANIMATION_STEPS, knife_fx)
 
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update display
    pygame.display.update()

#exit pygame
pygame.quit()


