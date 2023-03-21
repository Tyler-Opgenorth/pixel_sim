import pygame
import random

# Define colors as constants
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (155, 155, 155)
LIGHT_GRAY = (255, 155, 155)
DARK_BLUE = (55, 55, 255)
LIGHT_BLUE = (55, 55, 55)
ORANGE = (255, 55, 55)

# Define matter types as constants
AIR = {'name': 'air', 'type': 'gas', 'density': 0, 'color': BLACK}
EDGE = {'name': 'edge', 'type': 'solid', 'density': 999, 'color': RED}
WATER = {'name': 'water', 'type': 'liquid', 'density': 10, 'color': BLUE}
ACID = {'name': 'acid', 'type': 'liquid', 'density': 10, 'color': DARK_BLUE}
OIL = {'name': 'oil', 'type': 'liquid', 'density': 5, 'color': LIGHT_BLUE}
SAND = {'name': 'sand', 'type': 'solid', 'density': 10, 'color': GRAY}
GUN_POWDER = {'name': 'gunpowder', 'type': 'solid', 'density': 10, 'color': LIGHT_GRAY}
LAVA = {'name': 'lava', 'type': 'liquid', 'density': 50, 'color': ORANGE}
TYPES = (AIR, EDGE, WATER, ACID, OIL, SAND, GUN_POWDER, LAVA)
# Define the Liquid_update function
def Liquid_update(place, x, y, pixel):
    flow = random.randint(-1, 1)
    if place[y - 1][x]['density'] < place[y][x]['density']:
        place[y][x], place[y - 1][x] = place[y - 1][x], place[y][x]
    elif place[y - 1][x + 1]['density'] < place[y][x]['density'] and random.choice((True, False)):
        place[y][x],place[y - 1][x + 1] = place[y - 1][x + 1],place[y][x]
    elif place[y - 1][x - 1]['density'] < place[y][x]['density'] and random.choice((True, False)):
        place[y][x], place[y - 1][x - 1] = place[y - 1][x - 1], place[y][x]

    elif place[y][x + flow]['density'] < place[y][x]['density']:
        place[y][x], place[y][x + flow] = place[y][x + flow], place[y][x]


    return place

# Initialize the Pygame library
pygame.init()

# Define the screen size and set up the window
screen_size = 500
size = 50
screen = pygame.display.set_mode((screen_size, screen_size), pygame.NOFRAME)
pygame.display.set_caption('MatterBox')
clock = pygame.time.Clock()

# Initialize the world array
world = []
row = []
for y in range(size):
    for x in range(size):
        if x == 0 or x == size-1 or y == 0 or y == size-1:
            row.append(EDGE)
        else:
            row.append(AIR)
    world.append(row)
    row = []
# Main game loop
running = True
place = False
place2 = False
selection=2
while running:
    # Set the frame rate
    clock.tick(60)

    # Handle Pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Place water at mouse position on click
            if event.button == 1:
                place = True
                selection +=1
                if selection >= len(TYPES):
                    selection =2
            if event.button == 3:
                place2 = not place2
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                place = False

    # Update the world
    x, y = pygame.mouse.get_pos()
    if place:

        if world[y // (screen_size // size)][x // (screen_size // size)] == AIR:
            world[y // (screen_size // size)][x // (screen_size // size)] = TYPES[selection]
    if place2:
        x, y = event.pos
        if world[y // (screen_size // size)][x // (screen_size // size)] != EDGE:
            world[y // (screen_size // size)][x // (screen_size // size)] = AIR
    for y in range(size):
        for x in range(size):
            world.reverse()
            # Update liquids
            if world[y][x]['type'] == 'liquid':
                world = Liquid_update(world, x, y, world[y][x])
            world.reverse()
    for y in range(size):
        for x in range(size):
            pygame.draw.rect(screen, (world[y][x]['color']), (x * (500 / size), y * (500 / size), 50, 50))

    # Update the screen
    pygame.display.flip()

# Quit the Pygame library
pygame.quit()
