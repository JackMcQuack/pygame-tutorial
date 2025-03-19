import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Pygame Demo")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)
game_active = True

sky_surface = pygame.image.load("graphics/Sky.png").convert_alpha()
ground_surface = pygame.image.load("graphics/ground.png").convert_alpha()

text_surface = test_font.render("My game", False, (64, 64, 64))
text2_surface = test_font.render("Game over, press space to try again", False, (64, 64, 64))
text_rect = text_surface.get_rect(center = (400, 50))
text2_rect = text2_surface.get_rect(center = (400, 50))
snail_surface = pygame.image.load("graphics/snail/snail1.png")
snail_rect = snail_surface.get_rect(midbottom = (700, 300))

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
                if game_active and player_rect.bottom == 300:
                    player_gravity = -20
                else:
                    snail_rect.left = 700
                    game_active = True
            
 
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                player_gravity = -20

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        pygame.draw.rect(screen, '#c0e8ec', text_rect)
        pygame.draw.rect(screen, '#c0e8ec', text_rect, 20)
        screen.blit(text_surface, text_rect)
        screen.blit(snail_surface, snail_rect)
        if snail_rect.right <= 0:
            snail_rect.left = 800
        snail_rect.left -= 6

        player_gravity += 1
        player_rect.y += player_gravity
        player_rect.bottom = min(300, player_rect.bottom)
        screen.blit(player_surface, player_rect)

        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill('Green')
        screen.blit(text2_surface, text2_rect)

    pygame.display.update()
    clock.tick(60)