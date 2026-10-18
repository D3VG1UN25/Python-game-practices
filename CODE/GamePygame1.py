# A game in the console created with the pygame library
# Game origin: https://ellibrodepython.com/juego-pygame
import pygame  
import sys

pygame.init()

wide, tall = 400, 300
screen = pygame.display.set_mode((wide, tall))
pygame.display.set_caption("Console test")

colour = input("Do you want red, green or blue? ").lower()
player = pygame.Rect(50, 50, 20, 20)
speed = 5

clock = pygame.time.Clock()

while True:

    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


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

        # Changes the screen's color and the player's
    screen.fill((20, 20, 20))
    if colour == "red":
        pygame.draw.rect(screen, (255, 0, 0), player)
    elif colour == "green":
        pygame.draw.rect(screen, (0, 255, 0), player)
    elif colour == "blue":
        pygame.draw.rect(screen, (0, 0, 255), player)
    else:
        pygame.draw.rect(screen, (255, 0, 0), player)
    # Keyboard inputs

    # To keep the player inside the screen
    player.clamp_ip(screen.get_rect())

    pygame.display.flip()

    clock.tick(30)