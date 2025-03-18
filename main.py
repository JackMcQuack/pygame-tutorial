import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Pygame Demo")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

sky_surface = pygame.image.load("graphics/Sky.png").convert_alpha()
ground_surface = pygame.image.load("graphics/ground.png").convert_alpha()
ground_rect = ground_surface.get_rect(topleft = (0, 300))

text_surface = test_font.render("My game", False, (64, 64, 64))
text_rect = text_surface.get_rect(center = (400, 50))
snail_surface = pygame.image.load("graphics/snail/snail1.png")
snail_rect = snail_surface.get_rect(midbottom = (700, 300))
snail_x_pos = 700

player_gravity = 0

player_surface = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (100, 100))
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('jump')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                print('released')
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print('collision')
    
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, ground_rect)
    pygame.draw.rect(screen, '#c0e8ec', text_rect)
    pygame.draw.rect(screen, '#c0e8ec', text_rect, 20)
    # pygame.draw.line(screen, 'Black', (0, 0), (800, 400))
    screen.blit(text_surface, text_rect)
    screen.blit(snail_surface, snail_rect)
    if snail_rect.right <= 0:
        snail_rect.left = 800

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and player_rect.colliderect(ground_rect):
        player_gravity += -10

    if not player_rect.colliderect(ground_rect):
        player_gravity += 1
    elif player_rect.colliderect(ground_rect) and not keys[pygame.K_SPACE]:
        player_gravity = 0

    player_rect.bottom += player_gravity
    
    screen.blit(player_surface, player_rect)
    if not snail_rect.colliderect(player_rect):
        snail_rect.left -= 4

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(mouse_pos)
    #     print('collision')

    pygame.display.update()
    clock.tick(60)