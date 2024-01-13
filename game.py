import pygame
pygame.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SCREEN_fill = ((0,0,0))
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player1_image = pygame.image.load("yellow_monster.png")
player1_rect = player1_image.get_rect
player1_rect.left = 0
player1_rect.bottom = SCREEN_HEIGHT

player2_image = pygame.image.load("blue_monster.png")
player2_rect = player2_image.get_rect
player2_rect.right = 800
player2_rect.bottom = SCREEN_HEIGHT

player1_NORMAL_VELOCITY = 5
player1_BOOST_VELOCITY = 15
velocity = player1_NORMAL_VELOCITY
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player1_rect.left > 0:
        player1_rect.x -= velocity
    if keys[pygame.K_RIGHT] and player1_rect.right < SCREEN_WIDTH:
        player1_rect.x += velocity
    if keys[pygame.K_UP] and player1_rect.top > 100:
        player1_rect.y -= velocity
    if keys[pygame.K_DOWN] and player1_rect.bottom < SCREEN_HEIGHT:
        player1_rect.y += velocity
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player2_rect.left > 0:
        player2_rect.x -= velocity
    if keys[pygame.K_d] and player2_rect.right < SCREEN_WIDTH:
        player2_rect.x += velocity
    if keys[pygame.K_w] and player2_rect.top > 100:
        player2_rect.y -= velocity
    if keys[pygame.K_s] and player2_rect.bottom < SCREEN_HEIGHT:
        player2_rect.y += velocity
   
    screen.fill()
    screen.blit_player1()
    screen.blit_player2()
    pygame.display.update()