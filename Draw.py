import tkinter as tk
from math import sin, cos, atan, sqrt
import time

from Polyhedra import Cube, Tetrahedron


WIDTH = 800
HEIGHT = 800

O_X = WIDTH/2
O_Y = HEIGHT/2
O_Z = 0

CUBE_EDGE = 150
DOT_RADIUS = 3

FRAME_COUNT = 100
FPS = 120.0

PI = 3.1415927



root = tk.Tk ()
root.geometry ('%dx%d+%d+%d' % (WIDTH, HEIGHT, 10, 10))
root.resizable (0, 0)       # Prevent resizing of windows, so we can keep center
root.title ("Simple Polyhedra")

canvas = tk.Canvas (root, width=WIDTH, height=HEIGHT)
canvas.pack ()

#greenbox_lower  = canvas.create_rectangle (25, HEIGHT-25, WIDTH-25, HEIGHT-50, fill="green")

canvas.create_line (0, O_Y, WIDTH, O_Y, fill="red")
canvas.create_line (O_X, 0, O_X, HEIGHT, fill="red")

cube = Cube (CUBE_EDGE, 300, 300, 100)
cube.rotate_Y (PI/4)
cube.rotate_X (atan (sqrt (2)))
cube.draw (canvas)

tetra = Tetrahedron (1.5*CUBE_EDGE, 500, 500, 0)
tetra.draw (canvas)

root.update ()
time.sleep (5)

while (True):
        canvas.create_line (0, O_Y, WIDTH, O_Y, fill="red")
        canvas.create_line (O_X, 0, O_X, HEIGHT, fill="red")

        cube.rotate_Z (PI/360)
        cube.rotate_Y (PI/360)
        cube.rotate_X (PI/360)
        cube.draw (canvas)

        tetra.rotate_Z (PI/360)
        tetra.rotate_Y (PI/360)
        tetra.rotate_X (PI/360)
        tetra.draw (canvas)

        root.update ()
        time.sleep (1/FPS)
        canvas.delete ("all")

root.mainloop ()




# Next steps: Get a cool 3D bouncing animation implemented, so you can have a sphere or cube bounce around. Actually, that's probably too difficult. Maybe draw a 3D room first, like Doom-style or something personalized.