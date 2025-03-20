import pygame
from sys import exit

def display_score():
    global current_time 
    current_time = (pygame.time.get_ticks() - start_time) // 150
    score_surface = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rect)

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Pygame Demo")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 45)
game_active = True
start_time = 0
current_time = 0

sky_surface = pygame.image.load("graphics/Sky.png").convert_alpha()
ground_surface = pygame.image.load("graphics/ground.png").convert_alpha()

# text_surface = test_font.render("My game", False, (64, 64, 64))
# text_rect = text_surface.get_rect(center = (400, 50))

snail_surface = pygame.image.load("graphics/snail/snail1.png")
snail_rect = snail_surface.get_rect(midbottom = (700, 300))

player_gravity = 0
player_surface = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (100, 100))

player_stand_surface = pygame.image.load("graphics/player/player_stand.png")
player_stand_scaled = pygame.transform.scale(player_stand_surface, (200, 250))
player_stand_rect = player_stand_scaled.get_rect(midbottom = (350, 350))

snail_stand_surface = pygame.image.load("graphics/snail/snail1.png")
snail_stand_scaled = pygame.transform.scale(snail_stand_surface, (200, 100))
snail_stand_rect = snail_stand_scaled.get_rect(midbottom = (450, 350))

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_active and player_rect.bottom == 300:
                    player_gravity = -20
                if not game_active:
                    start_time = pygame.time.get_ticks()
                    snail_rect.left = 700
                    game_active = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                player_gravity = -20

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        display_score()
        # pygame.draw.rect(screen, '#c0e8ec', text_rect)
        # pygame.draw.rect(screen, '#c0e8ec', text_rect, 20)
        # screen.blit(text_surface, text_rect)

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
        endtext_surface = test_font.render(f"Game over, press space to try again. Your score is {current_time}!", False, (64, 64, 64))
        endtext_rect = endtext_surface.get_rect(center = (400, 50))
        screen.fill((94, 129, 162))
        screen.blit(endtext_surface, endtext_rect)
        screen.blit(player_stand_scaled, player_stand_rect)
        screen.blit(snail_stand_scaled, snail_stand_rect)

    pygame.display.update()
    clock.tick(60)