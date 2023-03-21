import random,pygame
"""
tyler opgenorth
"""


def Solid_update(place, x, y, pixel):
    if place[y - 1][x] == 0:
        place[y - 1][x] = pixel
        place[y][x] = 0

    elif place[y - 1][x + 1] == 0 and random.choice((True, False)):
        place[y - 1][x + 1] = pixel
        place[y][x] = 0
    elif place[y - 1][x - 1] == 0 and random.choice((True, False)):
        place[y - 1][x - 1] = pixel
        place[y][x] = 0

    elif place[y - 1][x - 1] == 1 and random.choice((True, False)):
        place[y - 1][x - 1] = pixel
        place[y][x] = 1
    elif place[y - 1][x + 1] == 1 and random.choice((True, False)):
        place[y - 1][x + 1] = pixel
        place[y][x] = 1
    elif place[y - 1][x] == 1 and random.choice((True, False)):
         place[y - 1][x] = pixel
         place[y][x] = 1
    return place[y][x]


def Liquid_update(place, x, y, pixel):
    flow = random.randint(-1, 1)
    if place[y - 1][x] == 0:
        place[y - 1][x] = pixel
        place[y][x] = 0
    elif place[y - 1][x + 1] == 0 and random.choice((True, False)):
        place[y - 1][x + 1] = pixel
        place[y][x] = 0
    elif place[y - 1][x - 1] == 0 and random.choice((True, False)):
        place[y - 1][x - 1] = pixel
        place[y][x] = 0

    elif place[y][x + flow] == 0:
        place[y][x + flow] = pixel
        place[y][x] = 0
    elif place[y][x] != 6:
        if place[y - 1][x] == 6:
            place[y - 1][x] = pixel
            place[y][x] = 6
        elif place[y - 1][x - 1] == 6:
            place[y - 1][x - 1] = pixel
            place[y][x] = 6
        elif place[y - 1][x + 1] == 6:
            place[y - 1][x + 1] = pixel
            place[y][x] = 6
        elif place[y][x + flow] == 6:
            place[y][x + flow] = pixel
            place[y][x] = 6


    return place[y][x]


def display(color, size, surface):
    if size == 1:
        pygame.draw.rect(surface, color, (20, 20, 10, 10))
    if size == 2:
        pygame.draw.rect(surface, color, (20, 20, 20, 20))
    if size == 3:
        pygame.draw.rect(surface, color, (20, 20, 30, 30))




