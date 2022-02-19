from tkinter import *

canvazwidth = 900
canvazheight = 900
linewidth = 20
linecolor = 'red'

MainCanvas = Canvas(
    width = canvazwidth,
    height = canvazheight
)

MainCanvas.pack()

MainCanvas.create_line(0, 0, canvazwidth, 0, width=linewidth, fill=linecolor)
MainCanvas.create_line(canvazwidth, 0, canvazwidth, canvazheight, width=linewidth, fill=linecolor)
MainCanvas.create_line(0, canvazheight, canvazwidth, canvazheight, width=linewidth, fill=linecolor)
MainCanvas.create_line(0, 0, 0, canvazheight, width=linewidth, fill=linecolor)




mainloop()