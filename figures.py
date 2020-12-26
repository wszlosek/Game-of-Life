from random import choices


def add_on(grid, *arg):
    for i in arg:
        grid[int(i[0])][int(i[1])] = 1

    return grid


def random_grid(grid, p=0.3):
    N = len(grid)

    for i in range(N):
        for j in range(N):
            grid[i][j] = (choices([0, 1],
                                  [float(1.0 - p), p]))[0]


''' STILL LIFES'''


def block(grid, x=0, y=0):
    x, y = y, x
    add_on(grid, (x, y), (x + 1, y),
                 (x + 1, y + 1), (x, y + 1))


def beehive(grid, x=0, y=0):
    x, y = y, x
    add_on(grid, (x + 1, y), (x + 1, y + 3),
          (x, y + 1), (x, y + 2), (x + 2, y + 1),
          (x + 2, y + 2))


def loaf(grid, x=0, y=0):
    x, y = y, x
    add_on(grid, (x + 1, y), (x + 1, y + 3),
          (x, y + 1), (x, y + 2), (x + 2, y + 1),
          (x + 3, y + 2), (x + 2, y + 3))


def tub(grid, x=0, y=0):
    x, y = y, x
    add_on(grid, (x + 1, y), (x + 2, y + 1),
          (x + 1, y + 2), (x, y + 1))


def boat(grid, x=0, y=0):
    tub(grid, x, y)
    x, y = y, x
    add_on(grid, (x, y))


''' OSCILLATORS '''


def blinker(grid, x=0, y=0):
    x, y = y, x
    add_on(grid, (x, y), (x, y + 1), (x, y + 2))


def vertical_blinker(grid, x=0, y=0):
    x, y = y, x
    add_on(grid, (x, y), (x + 1, y), (x + 2, y))


def toad(grid, x=1, y=1):
    block(grid, x + 1, y)
    x, y = y, x
    add_on(grid, (x + 1, y), (x, y + 3))


def beacon(grid, x=0, y=0):
    block(grid, x, y)
    block(grid, x+2, y+2)


def pulsar(grid, x=0, y=0):
    blinker(grid, x + 2, y)
    blinker(grid, x + 2, y + 5)
    vertical_blinker(grid, x, y + 2)
    vertical_blinker(grid, x + 5, y + 2)

    blinker(grid, x + 8, y)
    blinker(grid, x + 8, y + 5)
    vertical_blinker(grid, x + 7, y + 2)
    vertical_blinker(grid, x + 12, y + 2)

    blinker(grid, x + 2, y + 7)
    blinker(grid, x + 2, y + 12)
    vertical_blinker(grid, x, y + 8)
    vertical_blinker(grid, x + 5, y + 8)

    blinker(grid, x + 8, y + 7)
    blinker(grid, x + 8, y + 12)
    vertical_blinker(grid, x + 7, y + 8)
    vertical_blinker(grid, x + 12, y + 8)


def pentadecathlon(grid, x=0, y=0):
    tub(grid, x + 1, y)
    tub(grid, x + 6, y)
    x, y = y, x
    add_on(grid, (x + 1, y), (x + 1, y + 4))
    add_on(grid, (x + 1, y), (x + 1, y + 5))
    add_on(grid, (x + 1, y), (x + 1, y + 9))


''' SPACESHIPS'''


def glider(grid, x=0, y=0):
    x, y = y, x
    add_on(grid, (x, y + 1), (x + 1, y + 2),
                 (x, y + 3), (x - 1, y + 3),
                 (x + 1, y + 3))


def lightweight_spaceship(grid, x=0, y=0):
    vertical_blinker(grid, x, y + 1)
    blinker(grid, x + 1, y + 3)
    x, y = y, x
    add_on(grid, (x, y + 1), (x, y + 4), (x + 2, y + 4))


def heavyweight_spaceship(grid, x=0, y=0):
    vertical_blinker(grid, x, y + 2)
    blinker(grid, x, y + 4)
    blinker(grid, x + 3, y + 4)
    x, y = y, x
    add_on(grid, (x + 1, y + 1), (x, y + 3), (x, y + 4),
           (x + 1, y + 6), (x + 3, y + 6))


''' GUNS '''


def gosper_glider_gun(grid, x, y):
    block(grid, x, y + 6)
    vertical_blinker(grid, x + 10, y + 6)
    vertical_blinker(grid, x + 16, y + 6)
    vertical_blinker(grid, x + 20, y + 4)
    vertical_blinker(grid, x + 21, y + 4)
    block(grid, x + 34, y + 4)

    x, y = y, x
    add_on(grid, (x + 5, y + 11), (x + 4, y + 12),
           (x + 4, y + 13), (x + 10, y + 12),
           (x + 10, y + 13), (x + 9, y + 11),
           (x + 7, y + 14), (x + 5, y + 15),
           (x + 9, y + 15), (x + 7, y + 17),
           (x + 3, y + 22), (x + 7, y + 22),
           (x + 2, y + 24), (x + 3, y + 24),
           (x + 7, y + 24), (x + 8, y + 24))


def simkin_glider_gun(grid, x, y):
    block(grid, x + 1, y + 1)
    block(grid, x + 8, y + 1)
    block(grid, x + 5, y + 4)
    block(grid, x + 32, y + 12)
    blinker(grid, x + 22, y + 13)
    vertical_blinker(grid, x + 22, y + 11)
    blinker(grid, x + 22, y + 20)

    x, y = y, x
    add_on(grid, (x + 10, y + 23), (x + 10, y + 24),
           (x + 10, y + 26), (x + 10, y + 27),
           (x + 11, y + 28), (x + 12, y + 29),
           (x + 13, y + 28), (x + 14, y + 27),
           (x + 18, y + 21), (x + 19, y + 21),
           (x + 18, y + 22), (x + 21, y + 24))

