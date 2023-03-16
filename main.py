"""
tyler opgenorth
-1 = wall
0 = air
1 = water
2 = barrier
3 = sand
4 = g_sand
5 = spark
6 = v_oil
7 = lava
8 = fire emitter
9 = water emitter
10 = gas
11 = electric
"""
from Gravity import *
import pygame
import random

screen_size = 500
screen = pygame.display.set_mode((screen_size, screen_size), pygame.NOFRAME)
pygame.display.set_caption('MatterBox')
pygame.init()
clock = pygame.time.Clock()
world = []
row = []
height = 50
width = 50
place = False
delete = False
selection = 1
selection_size = 1
paused = False
#generate world
world = []
row = []
for y in range(height):
    for x in range(width):
        if x == 0 or x == width-1 or y == 0 or y == height-1:
            row.append(-1)
        else:
            row.append(0)
    world.append(row)
    row = []
running = True
while running:
    #world speed
    clock.tick(60)
    #controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                place = True
            if event.button == 3:
                delete = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                place = False
            if event.button == 3:
                delete = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                selection += 1
                if selection > 11:
                    selection = 1
            if event.key == pygame.K_LEFT:
                selection -= 1
                if selection < 1:
                    selection = 11
            if event.key == pygame.K_r:
                world = []
                row = []
                for y in range(height):
                    for x in range(width):
                        if x == 0 or x == width - 1 or y == 0 or y == height - 1:
                            row.append(-1)
                        else:
                            row.append(0)
                    world.append(row)
                    row = []
            if event.key == pygame.K_UP:
                selection_size += 1
                if selection_size > 3:
                    selection_size = 1
            if event.key == pygame.K_DOWN:
                selection_size -= 1
                if selection_size < 1:
                    selection_size = 3
            if event.key == pygame.K_SPACE:
                paused = not paused
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_1:
                selection = 1
            if event.key == pygame.K_2:
                selection = 2
            if event.key == pygame.K_3:
                selection = 3
            if event.key == pygame.K_4:
                selection = 4
            if event.key == pygame.K_5:
                selection = 5
            if event.key == pygame.K_6:
                selection = 6
            if event.key == pygame.K_7:
                selection = 7
            if event.key == pygame.K_8:
                selection = 8
            if event.key == pygame.K_9:
                selection = 9
    #get mouse position
    mx, my = pygame.mouse.get_pos()
    #place blocks
    if place:
        for y in range(height):
            for x in range(width):
                if round(mx / (500 / width)) == x and round(my / (500 / width)) == y and world[y][x] == 0:
                    world[y][x] = selection
                if selection_size == 2:
                    if round(mx / (500 / width)) == x+1 and round(my / (500 / width)) == y and world[y][x] == 0:
                        world[y][x] = selection
                    if round(mx / (500 / width)) == x and round(my / (500 / width)) == y+1 and world[y][x] == 0:
                        world[y][x] = selection
                    if round(mx / (500 / width)) == x+1 and round(my / (500 / width)) == y+1 and world[y][x] == 0:
                        world[y][x] = selection
                if selection_size == 3:
                    if round(mx / (500 / width)) == x+1 and round(my / (500 / width)) == y and world[y][x] == 0:
                        world[y][x] = selection
                    if round(mx / (500 / width)) == x and round(my / (500 / width)) == y+1 and world[y][x] == 0:
                        world[y][x] = selection
                    if round(mx / (500 / width)) == x+1 and round(my / (500 / width)) == y+1 and world[y][x] == 0:
                        world[y][x] = selection
                    if round(mx / (500 / width)) == x-1 and round(my / (500 / width)) == y and world[y][x] == 0:
                        world[y][x] = selection
                    if round(mx / (500 / width)) == x and round(my / (500 / width)) == y+2 and world[y][x] == 0:
                        world[y][x] = selection
                    if round(mx / (500 / width)) == x+1 and round(my / (500 / width)) == y+2 and world[y][x] == 0:
                        world[y][x] = selection
                    if round(mx / (500 / width)) == x-1 and round(my / (500 / width)) == y+1 and world[y][x] == 0:
                        world[y][x] = selection
                    if round(mx / (500 / width)) == x-1 and round(my / (500 / width)) == y+2 and world[y][x] == 0:
                        world[y][x] = selection
    #delete blocks
    if delete:
        for y in range(height):
            for x in range(width):
                if round(mx / (500 / width)) == x and round(my / (500 / width)) == y and world[y][x] != -1:
                    world[y][x] = 0
                if selection_size == 2:
                    if round(mx / (500 / width)) == x+1 and round(my / (500 / width)) == y and world[y][x] != -1:
                        world[y][x] = 0
                    if round(mx / (500 / width)) == x and round(my / (500 / width)) == y+1 and world[y][x] != -1:
                        world[y][x] = 0
                    if round(mx / (500 / width)) == x+1 and round(my / (500 / width)) == y+1 and world[y][x] != -1:
                        world[y][x] = 0
                if selection_size == 3:
                    if round(mx / (500 / width)) == x+1 and round(my / (500 / width)) == y and world[y][x] != -1:
                        world[y][x] = 0
                    if round(mx / (500 / width)) == x and round(my / (500 / width)) == y+1 and world[y][x] != -1:
                        world[y][x] = 0
                    if round(mx / (500 / width)) == x+1 and round(my / (500 / width)) == y+1 and world[y][x] != -1:
                        world[y][x] = 0
                    if round(mx / (500 / width)) == x-1 and round(my / (500 / width)) == y and world[y][x] != -1:
                        world[y][x] = 0
                    if round(mx / (500 / width)) == x and round(my / (500 / width)) == y+2 and world[y][x] != -1:
                        world[y][x] = 0
                    if round(mx / (500 / width)) == x+1 and round(my / (500 / width)) == y+2 and world[y][x] != -1:
                        world[y][x] = 0
                    if round(mx / (500 / width)) == x-1 and round(my / (500 / width)) == y+1 and world[y][x] != -1:
                        world[y][x] = 0
                    if round(mx / (500 / width)) == x-1 and round(my / (500 / width)) == y+2 and world[y][x] != -1:
                        world[y][x] = 0
    #draw world
    for y in range(height):
        for x in range(0, width, 1):
            if world[y][x] == -1:
                pygame.draw.rect(screen, (255, 0, 0), (x*(500/width), y*(500/height), 50, 50))
            if world[y][x] == 0:
                pygame.draw.rect(screen, (0, 0, 0), (x*(500/width), y*(500/height), 50, 50))
            if world[y][x] == 1:
                pygame.draw.rect(screen, (30+random.randint(-10, 10),
                                          30+random.randint(-10, 10),
                                          205+random.randint(-10, 10)), (x*(500/width), y*(500/height), 50, 50))
            if world[y][x] == 2:
                pygame.draw.rect(screen, (155, 155, 155), (x*(500/width), y*(500/height), 50, 50))
            if world[y][x] == 3:
                pygame.draw.rect(screen, (100, 100, 100), (x*(500/width), y*(500/height), 50, 50))
            if world[y][x] == 4:
                pygame.draw.rect(screen, (100, 155, 200), (x*(500/width), y*(500/height), 50, 50))
            if world[y][x] == 5:
                pygame.draw.rect(screen, (245+random.randint(-10, 10),
                                          155+random.randint(-10, 10),
                                          155+random.randint(-10, 10)), (x*(500/width), y*(500/height), 50, 50))
            if world[y][x] == 6:
                pygame.draw.rect(screen, (240+random.randint(-10, 10),
                                          200+random.randint(-10, 10),
                                          100+random.randint(-10, 10)), (x*(500/width), y*(500/height), 50, 50))
            if world[y][x] == 7:
                pygame.draw.rect(screen, (155+random.randint(-10, 10),
                                          50+random.randint(-10, 10),
                                          50+random.randint(-10, 10)), (x*(500/width), y*(500/height), 50, 50))
            if world[y][x] == 8:
                pygame.draw.rect(screen, (255, 0, 0), (x*(500/width), y*(500/height), 50, 50))
            if world[y][x] == 9:
                pygame.draw.rect(screen, (0, 0, 255), (x*(500/width), y*(500/height), 50, 50))
            if world[y][x] == 10:
                pygame.draw.rect(screen, (0, 255, 0), (x*(500/width), y*(500/height), 50, 50))
            if world[y][x] == 11:
                pygame.draw.rect(screen, (0, 255, 255), (x*(500/width), y*(500/height), 50, 50))


    #update pixel positions

    if not paused:
        world.reverse()
        for y in range(0, height, 1):
            for x in range(0, width, 1):
                if world[y][x] == 1:
                    world[y][x] = Liquid_update(world, x, y, world[y][x])
                    if world[y-1][x] == 7:
                        world[y-1][x] = 2
                    if world[y][x+1] == 7:
                        world[y][x+1] = 2
                    if world[y][x-1] == 7:
                        world[y][x-1] = 2
                    if world[y+1][x+1] == 7:
                        world[y][x+1] = 2
                    if world[y-1][x-1] == 7:
                        world[y][x-1] = 2
                    if world[y+1][x-1] == 7:
                        world[y][x-1] = 2
                    if world[y-1][x+1] == 7:
                        world[y][x+1] = 2

                elif world[y][x] == 2:
                    pass

                elif world[y][x] == 3:
                    world[y][x] = Solid_update(world, x, y, world[y][x])

                elif world[y][x] == 4:
                    world[y][x] = Solid_update(world, x, y, world[y][x])

                elif world[y][x] == 5:
                    flow = random.randint(-1, 1)
                    if world[y - 1][x+flow] == 0:
                        world[y - 1][x+flow] = 5
                        world[y][x] = 0

                    #explode g_sand
                    elif world[y - 1][x+flow] == 4:
                        world[y - 1][x+flow] = 5
                        #one above
                        if world[y][x+flow] > 0:
                            world[y][x+flow] = 5
                        #one above and one to the right
                        if world[y][x+flow+1] > 0:
                            world[y][x+flow+1] = 5
                        # one above and one to the left
                        if world[y][x+flow-1] > 0:
                            world[y][x+flow-1] = 5
                        #one to the left
                        if world[y-1][x+flow-1] > 0:
                            world[y-1][x+flow-1] = 5
                        #one to the right
                        if world[y-1][x+flow+1] > 0:
                            world[y-1][x+flow+1] = 5
                        #one below and one to the right
                        if world[y-2][x+flow+1] > 0:
                            world[y-2][x+flow+1] = 5
                        #one below and one to the left
                        if world[y-2][x+flow-1] > 0:
                            world[y-2][x+flow-1] = 5
                        #one below
                        if world[y-2][x+flow] > 0:
                            world[y-2][x+flow] = 5
                    #make if 5 touches 6 6 becomes 5
                    elif world[y - 1][x+flow] == 6:
                        world[y - 1][x+flow] = 5
                    elif world[y - 1][x+flow] == 10:
                        world[y - 1][x+flow] = 5
                    else:
                        world[y][x] = 0

                elif world[y][x] == 6:
                    world[y][x] = Liquid_update(world, x, y, world[y][x])

                elif world[y][x] == 7:
                    world[y][x] = Liquid_update(world, x, y, world[y][x])
                    #burn flammable objects
                    if world[y][x+1] == 6 or world[y][x+1] == 4:
                        world[y][x+1] = 5
                    if world[y][x-1] == 6 or world[y][x-1] == 4:
                        world[y][x-1] = 5
                    if world[y+1][x] == 6 or world[y+1][x] == 4:
                        world[y+1][x] = 5
                    if world[y-1][x] == 6 or world[y-1][x] == 4:
                        world[y-1][x] = 5
                    if world[y+1][x+1] == 6 or world[y+1][x+1] == 4:
                        world[y+1][x+1] = 5
                    if world[y-1][x-1] == 6 or world[y-1][x-1] == 4:
                        world[y-1][x-1] = 5
                    if world[y+1][x-1] == 6 or world[y+1][x-1] == 4:
                        world[y+1][x-1] = 5
                    if world[y-1][x+1] == 6 or world[y-1][x+1] == 4:
                        world[y-1][x+1] = 5
                    #if 6 touches water 6 becomes barrier
                    if world[y-1][x] == 1:
                        world[y][x] = 2
                    if world[y][x+1] == 1:
                        world[y][x] = 2
                    if world[y][x-1] == 1:
                        world[y][x] = 2
                    if world[y+1][x+1] == 1:
                        world[y][x] = 2
                    if world[y-1][x-1] == 1:
                        world[y][x] = 2
                    if world[y+1][x-1] == 1:
                        world[y][x] = 2
                    if world[y-1][x+1] == 1:
                        world[y][x] = 2
                elif world[y][x] == 8:
                    if world[y-1][x] == 0:
                        world[y-1][x] = 5
                elif world[y][x] == 9:
                    if world[y-1][x] == 0:
                        world[y-1][x] = 1
                elif world[y][x] == 10:
                    flow = random.randint(-1, 1)
                    flow_2 = random.randint(-1, 1)
                    if world[y + flow_2][x + flow] == 0:
                        world[y + flow_2][x + flow] = 10
                        world[y][x] = 0
                elif world[y][x] == 11:
                    world[y][x] = Liquid_update(world, x, y, world[y][x])


        world.reverse()
    if selection == 1:
        display((0,0,255), selection_size, screen)

    if selection == 2:
        display((155, 155, 155), selection_size, screen)

    if selection == 3:
        display((100, 100, 100), selection_size, screen)

    if selection == 4:
        if selection_size == 1:
            pygame.draw.rect(screen, (100, 155, 200), (20, 20, 10, 10))
        if selection_size == 2:
            pygame.draw.rect(screen, (100, 155, 200), (20, 20, 20, 20))
        if selection_size == 3:
            pygame.draw.rect(screen, (100, 155, 200), (20, 20, 30, 30))

    if selection == 5:
        if selection_size == 1:
            pygame.draw.rect(screen, (255, 155, 155), (20, 20, 10, 10))
        if selection_size == 2:
            pygame.draw.rect(screen, (255, 155, 155), (20, 20, 20, 20))
        if selection_size == 3:
            pygame.draw.rect(screen, (255, 155, 155), (20, 20, 30, 30))

    if selection == 6:
        if selection_size == 1:
            pygame.draw.rect(screen, (240, 200, 100), (20, 20, 10, 10))
        if selection_size == 2:
            pygame.draw.rect(screen, (240, 200, 100), (20, 20, 20, 20))
        if selection_size == 3:
            pygame.draw.rect(screen, (240, 200, 100), (20, 20, 30, 30))

    if selection == 7:
        if selection_size == 1:
            pygame.draw.rect(screen, (155, 50, 50), (20, 20, 10, 10))
        if selection_size == 2:
            pygame.draw.rect(screen, (155, 50, 50), (20, 20, 20, 20))
        if selection_size == 3:
            pygame.draw.rect(screen, (155, 50, 50), (20, 20, 30, 30))

    if selection == 8:
        if selection_size == 1:
            pygame.draw.rect(screen, (255, 0, 0), (20, 20, 10, 10))
        if selection_size == 2:
            pygame.draw.rect(screen, (255, 0, 0), (20, 20, 20, 20))
        if selection_size == 3:
            pygame.draw.rect(screen, (255, 0, 0), (20, 20, 30, 30))
    if selection == 9:
        if selection_size == 1:
            pygame.draw.rect(screen, (0, 0, 255), (20, 20, 10, 10))
        if selection_size == 2:
            pygame.draw.rect(screen, (0, 0, 255), (20, 20, 20, 20))
        if selection_size == 3:
            pygame.draw.rect(screen, (0, 0, 255), (20, 20, 30, 30))
    if selection == 10:
        if selection_size == 1:
            pygame.draw.rect(screen, (0, 255, 0), (20, 20, 10, 10))
        if selection_size == 2:
            pygame.draw.rect(screen, (0, 255, 0), (20, 20, 20, 20))
        if selection_size == 3:
            pygame.draw.rect(screen, (0, 255, 0), (20, 20, 30, 30))
    pygame.display.flip()
    pygame.display.update()
    pygame.fullscreen = False
    pygame.borderless = True
pygame.quit()
