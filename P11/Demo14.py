import pygame
pygame.init()

screen = pygame.display.set_mode((600, 400))
x = 50
running = True

while running:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (x, 150, 50, 50))
    x += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
