from tkinter import *

GAME_WIDTH = 800
GAME_HEIGHT = 1000

ROAD_WIDTH = 300

ROAD_COLOR = '#5A5A5A'
BACKROUND_COLOR = '#000000'


window = Tk()
window.title('Auto Car')
window.resizable(False,False)

canvas = Canvas(window, bg=BACKROUND_COLOR, height=GAME_HEIGHT, width= GAME_WIDTH)
canvas.pack

window.mainloop()