# module to draw things with tkinter

from Tkinter import *
import sys
import random
import math

import consts

def getInstance():
    ''' Returns a Tkinter instance for future Tkinter calls '''
    return Tk()

def getWindow(pInstance):
    ''' Returns a canvas object to draw on '''
    canvas = Canvas(pInstance, width=consts.TK_WIN_WIDTH, height=consts.TK_WIN_HEIGHT)
    canvas.focus_set()
    canvas.pack()
    return canvas

def attachUpdater(instance, window, data):
    instance.after(consts.TK_UPDATE_TIMER, updateHandler,
                    instance, window, data)

def updateHandler(instance, window, data):
    gravity(window, data)
    attachUpdater(instance, window, data)

def attachMainloop(pInstance):
    ''' Calls Tkinter mainloop() function '''
    pInstance.mainloop()

def gravity(window, drops):
    for drop in drops:
        dropCoords = window.coords(drop)
        window.move(drop, 0, 1 + ((dropCoords[2] - dropCoords[0]) * 0.8))
        if dropCoords[1] > consts.TK_WIN_HEIGHT * 1.05:
            x = random.randint(0, consts.TK_WIN_WIDTH)
            y = random.randint(-consts.TK_WIN_HEIGHT, 0)
            z = random.randint(1, 5)
            window.coords(drop,
                          x, y,
                          x + 2 + (z * 0.2), y + 10 + z)

def init(window, drops):
    items = []
    for drop in drops:
        items.append(drawRectangle(window,
                                   drop[0], drop[1],
                                   2 + (drop[2] * 0.2), 10 + drop[2],
                                   random.choice(consts.TK_RDM_COLORS)))
    return items

def resetBackground(window, color):
    window.create_rectangle(0, 0, consts.TK_WIN_WIDTH, consts.TK_WIN_HEIGHT, fill=color)

def drawRectangle(window, x, y, xvector, yvector, color):
    return window.create_rectangle(x, y, x + xvector, y + yvector, fill=color)
