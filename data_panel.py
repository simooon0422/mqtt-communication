import pygame
import time

# Initializing Pygame
pygame.init()

# Initializing surface
screen = pygame.display.set_mode((400, 300))

# Initializing Color
color = (0, 0, 0)

# Drawing Rectangle
# pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))


fontTitle = pygame.font.SysFont("arial", 20)

pygame.display.flip()

x = 0

while True:
    textTitle = fontTitle.render(f"Iteration: {x}", True, color)
    screen.fill((255, 255, 255))
    screen.blit(textTitle, (150, 200))
    pygame.display.flip()

    x = x + 1
    time.sleep(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
