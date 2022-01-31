from tkinter import *
import math
root = Tk()
myCanvas = Canvas(root, width=1920, height=1080)
myCanvas.pack()

def create_circle(x, y, r, canvasName, color): #center coordinates, radius, color
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, outline=color)

def plot_pixel(x, y, canvasName, color):
    return create_circle(x, y, 0, myCanvas, color)

corna = 9
cornb = 21
side = 16

for i in range(1920):
    for j in range(1080):
        x = corna + i * side / 100
        y = cornb + j * side / 100
        c = math.floor(x * x + y * y)
        if c % 3 == 0:
            plot_pixel(i, j, myCanvas, color="blue")
        elif c % 2 == 0:
            plot_pixel(i, j, myCanvas, color="green")
        else:
            plot_pixel(i, j, myCanvas, color="red")



#create_circle(100, 100, 20, myCanvas)
#create_circle(50, 25, 10, myCanvas)

#plot_pixel(100, 100, myCanvas)
root.mainloop() #Start for running camera/canvas?
