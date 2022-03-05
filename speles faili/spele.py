from tkinter import *
from random import *

#size of canvas
canvazwidth = 900
canvazheight = 900
#border line width and color
linewidth = 20
linecolor = 'red'
#start position of cube
xx = 20
yy = canvazheight - 20
cx = randrange(0, canvazwidth, 5)
cy = randrange(0, canvazheight, 5)
r = Tk()
#canvaz
MainCanvas = Canvas(
    width = canvazwidth,
    height = canvazheight
)
#starting canvaz
MainCanvas.pack()
#creation of cube
cubee = MainCanvas.create_rectangle(xx, yy, xx + 20, yy - 20, fill='yellow')
target = MainCanvas.create_rectangle(cx, cy, cx + 20, cy + 20, fill='brown')
#creating za lines
MainCanvas.create_line(0, 0, canvazwidth, 0, width=linewidth, fill=linecolor)
MainCanvas.create_line(canvazwidth, 0, canvazwidth, canvazheight, width=linewidth, fill=linecolor)
MainCanvas.create_line(0, canvazheight, canvazwidth, canvazheight, width=linewidth, fill=linecolor)
MainCanvas.create_line(0, 0, 0, canvazheight, width=linewidth, fill=linecolor)

#function to move cube
def MoveCube(direction):
    global xx, yy, cubee, target, cx, cy
    if direction == 'UP':
        yy -= 5
        MainCanvas.delete(cubee)
        cubee = MainCanvas.create_rectangle(xx, yy, xx + 20, yy - 20, fill='yellow')
    if direction == 'RIGHT':
        xx += 5
        MainCanvas.delete(cubee)
        cubee = MainCanvas.create_rectangle(xx, yy, xx + 20, yy - 20, fill='yellow')
    if direction == 'DOWN':
        yy += 5
        MainCanvas.delete(cubee)
        cubee = MainCanvas.create_rectangle(xx, yy, xx + 20, yy - 20, fill='yellow')
    if direction == 'LEFT':
        xx -= 5
        MainCanvas.delete(cubee)
        cubee = MainCanvas.create_rectangle(xx, yy, xx + 20, yy - 20, fill='yellow')
    if xx < cx + 20 and xx > cx and yy < cy + 20 and yy > cy:
        print("bruh") 
        MainCanvas.delete(target)
        cx = randrange(0, canvazwidth, 5)
        cy = randrange(0, canvazheight, 5)
        target = MainCanvas.create_rectangle(cx, cy, cx + 20, cy + 20, fill='brown')


def on_keypress(event):
    if event.keysym == "w":
        MoveCube('UP')
    if event.keysym == "a":
        MoveCube('LEFT')
    if event.keysym == "s":
        MoveCube('DOWN')
    if event.keysym == "d":
        MoveCube('RIGHT')

def on_keyrelease(event):
    global direction
    direction = None

r.bind_all('<KeyPress>', on_keypress)
r.bind_all('<KeyRelease>', on_keyrelease)
r.mainloop()