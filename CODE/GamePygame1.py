# A game in the console created with the pygame library
import pygame  
import sys

pygame.init()

wide, tall = 400, 300
screen = pygame.display.set_mode((wide, tall))
pygame.display.set_caption("Console test")

player = pygame.Rect(50, 50, 20, 20)
speed = 5

clock = pygame.time.Clock()

while True:

    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Keyboard inputs
    keys = pygame.key.get_pressed()

    # Changes the direction speed of a movement when holding certain keys
    if keys[pygame.K_LEFT]: 
        player.x -= speed
    if keys[pygame.K_RIGHT]: 
        player.x += speed
    if keys[pygame.K_UP]: 
        player.y -= speed
    if keys[pygame.K_DOWN]: 
        player.y += speed
        
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), player)

    # To keep the player inside the screen
    player.clamp_ip(screen.get_rect())

    pygame.display.flip()

    clock.tick(30)