import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Pygame Demo")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

sky_surface = pygame.image.load("graphics/Sky.png").convert_alpha()
ground_surface = pygame.image.load("graphics/ground.png").convert_alpha()
text_surface = test_font.render("My game", False, (0, 0, 0)).convert_alpha()

snail_surface = pygame.image.load("graphics/snail/snail1.png")
snail_rect = snail_surface.get_rect(midbottom = (700, 300))
snail_x_pos = 700

player_surface = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (100, 300))
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print('collision')
    
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (350, 50))
    screen.blit(snail_surface, snail_rect)
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(player_surface, player_rect)
    if not snail_rect.colliderect(player_rect):
        snail_rect.left -= 4

    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        print(mouse_pos)
        print('collision')
    pygame.display.update()
    clock.tick(60)