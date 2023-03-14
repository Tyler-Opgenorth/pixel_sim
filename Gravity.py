import random,pygame
"""
tyler opgenorth
"""
def Solid_update(map, x, y, pixel):
    if map[y - 1][x] == 0:
        map[y - 1][x] = pixel
        map[y][x] = 0
    elif map[y - 1][x - 1] == 0:
        map[y - 1][x - 1] = pixel
        map[y][x] = 0
    elif map[y - 1][x + 1] == 0:
        map[y - 1][x + 1] = pixel
        map[y][x] = 0
    elif map[y - 1][x] == 1:
        map[y - 1][x] = pixel
        map[y][x] = 1
    elif map[y - 1][x - 1] == 1:
        map[y - 1][x - 1] = pixel
        map[y][x] = 1
    elif map[y - 1][x + 1] == 1:
        map[y - 1][x + 1] = pixel
        map[y][x] = 1
    return map[y][x]


def Liquid_update(map, x, y, pixel):
    flow = random.randint(-1, 1)
    if map[y - 1][x] == 0:
        map[y - 1][x] = pixel
        map[y][x] = 0
    elif map[y - 1][x - 1] == 0:
        map[y - 1][x - 1] = pixel
        map[y][x] = 0
    elif map[y - 1][x + 1] == 0:
        map[y - 1][x + 1] = pixel
        map[y][x] = 0
    elif map[y][x + flow] == 0:
        map[y][x + flow] = pixel
        map[y][x] = 0
    elif map[y][x] != 6:
        if map[y - 1][x] == 6:
            map[y - 1][x] = pixel
            map[y][x] = 6
        elif map[y - 1][x - 1] == 6:
            map[y - 1][x - 1] = pixel
            map[y][x] = 6
        elif map[y - 1][x + 1] == 6:
            map[y - 1][x + 1] = pixel
            map[y][x] = 6
        elif map[y][x + flow] == 6:
            map[y][x + flow] = pixel
            map[y][x] = 6


    return map[y][x]


def display(color, size, surface):
    if size == 1:
        pygame.draw.rect(surface, color, (20, 20, 10, 10))
    if size == 2:
        pygame.draw.rect(surface, color, (20, 20, 20, 20))
    if size == 3:
        pygame.draw.rect(surface, color, (20, 20, 30, 30))




