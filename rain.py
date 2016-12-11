
#!/usr/bin/python

from __future__ import print_function
import sys
import random

import draw
import consts

def main():
    instance = draw.getInstance()
    window = draw.getWindow(instance)

    points = []

    for i in range(consts.DROP_COUNT):
        points.append([random.randint(0, consts.TK_WIN_WIDTH),
                       random.randint(-consts.TK_WIN_HEIGHT, 0),
                       random.randint(1, 5)])


    draw.resetBackground(window, consts.TK_COLOR_BLACK)

    graphicPoints = draw.init(window, points)

    for gPoint in graphicPoints:
        print(window.coords(gPoint))

    draw.attachUpdater(instance, window, graphicPoints)
    draw.attachMainloop(instance)

if __name__ == '__main__':
    main()
