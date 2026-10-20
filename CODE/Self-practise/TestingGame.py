# Basically the same program as Guided1, but this time I made it myself (kinda)
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((900, 900), pygame.RESIZABLE) # This is an upgrade I initially wasn't going to includes, it makes the screen be adjustable
pygame.display.set_caption("Practice game on my own!")
player = pygame.Rect(50, 50, 20, 20)

clock = pygame.time.Clock()

pygame.display.init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            # I aded these lines for it not to crash when I pressed start lol
    
    screen.fill((0, 0, 0)) # Deletes the previous square
    pygame.draw.rect(screen, (255, 0, 0), player) # Draws the square
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player.move_ip(5, 0)
    if keys[pygame.K_LEFT]:
        player.move_ip(-5, 0)
    if keys[pygame.K_UP]:
        player.move_ip(0, -5)
    if keys[pygame.K_DOWN]:
        player.move_ip(0, 5)
    
    pygame.display.flip()

    clock.tick(30)