BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def displayHM(np, time):
    hled = time[0] % 12
    mled = time[1] // 5
    for led in range(12):
        np[led] = BLACK
    if hled == mled:
        np[hled] = YELLOW
    else:
        np[hled] = RED
        np[mled] = GREEN
    np.write()


def displayS(np, time):
    sled = time[2] // 2.5
    for led in range(24):
        if sled < led:
            np[led] = BLACK
        else:
            np[led] = BLUE
    np.write()

