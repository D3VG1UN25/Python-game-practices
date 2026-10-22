# Idk, just gonna do some random stuff here
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
player = pygame.Rect(90, 90, 30, 30)
pygame.display.set_caption("Random")
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 0, 255), player, border_radius=5)
    mouse = pygame.mouse.get_pos()
    player.center = mouse

    pygame.display.flip()
    player.clamp_ip(screen.get_rect())

    clock.tick(30)