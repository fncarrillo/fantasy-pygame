import sys, pygame

pygame.init()
size = width, height = 800, 600

screen = pygame.display.set_mode(size)

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()