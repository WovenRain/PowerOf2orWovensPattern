# Import and initialize the pygame library
import pygame
import math

pygame.init()
screensize = 600
screen = pygame.display.set_mode([screensize, screensize])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    numofnodes = 8
    d = 2*math.pi/numofnodes

    nodes = {}
    for i in range(numofnodes):
        nodes[i] = (
            (screensize-20)*(1 + math.sin(d * i))/2 + 10,
            (screensize-20)*(1 - math.cos(d * i))/2 + 10
        )

    # print the circles
    for i in range(numofnodes):
        pygame.draw.circle(screen, (150,150,150), nodes[i], 10)

    # black lines for increments of +1 : 0,1,2,3
    lastPosition = 0
    for increment in range(numofnodes):
        position = (lastPosition + increment)%numofnodes

        pygame.draw.line(screen, (0,0,0), nodes[lastPosition], nodes[position], 2)
        lastPosition = position

    # Red lines for increments of +3 : 0,3,6,9
    lastPosition = 0
    for increment in range(numofnodes):
        position = (lastPosition + increment*3)%numofnodes

        pygame.draw.line(screen, (200,0,0), nodes[lastPosition], nodes[position], 2)
        lastPosition = position

    # Green lines for increments of +5 : 0,5,10,15
    lastPosition = 0
    for increment in range(numofnodes):
        position = (lastPosition + increment*5)%numofnodes

        pygame.draw.line(screen, (0,200,0), nodes[lastPosition], nodes[position], 2)
        lastPosition = position

    # Blue lines for increments of +7 : 0,7,14,21
    lastPosition = 0
    for increment in range(numofnodes):
        position = (lastPosition + increment*7)%numofnodes

        pygame.draw.line(screen, (0,0,200), nodes[lastPosition], nodes[position], 2)
        lastPosition = position
    

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()