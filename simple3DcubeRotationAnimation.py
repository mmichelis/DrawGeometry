import tkinter as tk
from math import sin, cos, atan, sqrt
import time


WIDTH = 800
HEIGHT = 800

O_X = WIDTH/2
O_Y = HEIGHT/2

CUBE_EDGE = 150
DOT_RADIUS = 3

FRAME_COUNT = 720
FPS = 90.0

PI = 3.1415926



def create_Cube ():
        # Draw all 12 edges of the cube between the 8 vertices
        """
        The way I draw my cube:
         5  6
        4  7
         1  2
        0  3
        """
        
        # Symmetric w.r.t. origin
        # vertices = [[O_X-sin(rot)*CUBE_EDGE     , O_Y+cos(rot)*CUBE_EDGE],
        #             [O_X-cos(rot-PI/6)*CUBE_EDGE, O_Y-sin(rot-PI/6)*CUBE_EDGE],
        #             [O_X                        , O_Y], 
        #             [O_X+cos(rot+PI/6)*CUBE_EDGE, O_Y+sin(rot+PI/6)*CUBE_EDGE], 
        #             [O_X                        , O_Y], 
        #             [O_X-cos(rot+PI/6)*CUBE_EDGE, O_Y-sin(rot+PI/6)*CUBE_EDGE], 
        #             [O_X+sin(rot)*CUBE_EDGE     , O_Y-cos(rot)*CUBE_EDGE], 
        #             [O_X+cos(rot-PI/6)*CUBE_EDGE, O_Y+sin(rot-PI/6)*CUBE_EDGE]]

        # I'm adding a z-coordinate for the calculations, origin at 0
        # vertices = [[O_X                        , O_Y+CUBE_EDGE],
        #             [O_X-cos(PI/6)*CUBE_EDGE    , O_Y+sin(PI/6)*CUBE_EDGE],
        #             [O_X                        , O_Y], 
        #             [O_X+cos(PI/6)*CUBE_EDGE    , O_Y+sin(PI/6)*CUBE_EDGE], 
        #             [O_X                        , O_Y], 
        #             [O_X-cos(PI/6)*CUBE_EDGE    , O_Y-sin(PI/6)*CUBE_EDGE], 
        #             [O_X                        , O_Y-CUBE_EDGE], 
        #             [O_X+cos(PI/6)*CUBE_EDGE, O_Y-sin(PI/6)*CUBE_EDGE]]
        

        vertices = [[O_X+0.5*CUBE_EDGE, O_Y+0.5*CUBE_EDGE, -0.5*CUBE_EDGE],
                    [O_X-0.5*CUBE_EDGE, O_Y+0.5*CUBE_EDGE, -0.5*CUBE_EDGE],
                    [O_X-0.5*CUBE_EDGE, O_Y+0.5*CUBE_EDGE, 0.5*CUBE_EDGE], 
                    [O_X+0.5*CUBE_EDGE, O_Y+0.5*CUBE_EDGE, 0.5*CUBE_EDGE], 
                    [O_X+0.5*CUBE_EDGE, O_Y-0.5*CUBE_EDGE, -0.5*CUBE_EDGE], 
                    [O_X-0.5*CUBE_EDGE, O_Y-0.5*CUBE_EDGE, -0.5*CUBE_EDGE], 
                    [O_X-0.5*CUBE_EDGE, O_Y-0.5*CUBE_EDGE, 0.5*CUBE_EDGE], 
                    [O_X+0.5*CUBE_EDGE, O_Y-0.5*CUBE_EDGE, 0.5*CUBE_EDGE]]


        return vertices


def draw_Cube (vertices):
        # Draw Edges

        # canvas.create_line (vertices[0][0], vertices[0][1], 
        #                     vertices[1][0], vertices[1][1])

        # canvas.create_line (vertices[0][0], vertices[0][1], 
        #                     vertices[3][0], vertices[3][1])

        # canvas.create_line (vertices[0][0], vertices[0][1], 
        #                     vertices[4][0], vertices[4][1])

        # canvas.create_line (vertices[1][0], vertices[1][1], 
        #                     vertices[2][0], vertices[2][1])

        # canvas.create_line (vertices[1][0], vertices[1][1], 
        #                     vertices[5][0], vertices[5][1])

        # canvas.create_line (vertices[2][0], vertices[2][1], 
        #                     vertices[3][0], vertices[3][1])

        # canvas.create_line (vertices[2][0], vertices[2][1], 
        #                     vertices[6][0], vertices[6][1])

        # canvas.create_line (vertices[3][0], vertices[3][1], 
        #                     vertices[7][0], vertices[7][1])

        # canvas.create_line (vertices[4][0], vertices[4][1], 
        #                     vertices[5][0], vertices[5][1])

        # canvas.create_line (vertices[4][0], vertices[4][1], 
        #                     vertices[7][0], vertices[7][1])

        # canvas.create_line (vertices[5][0], vertices[5][1], 
        #                     vertices[6][0], vertices[6][1])

        # canvas.create_line (vertices[6][0], vertices[6][1],     
        #                     vertices[7][0], vertices[7][1])


        # Draw Faces
        # Store faces in a list

        faces = [(vertices[0][0], vertices[0][1], 
                  vertices[1][0], vertices[1][1],
                  vertices[5][0], vertices[5][1], 
                  vertices[4][0], vertices[4][1],
                  "#7777FF",
                  vertices[0][2]+vertices[1][2]+vertices[5][2]+vertices[4][2])
                 ,
                 (vertices[0][0], vertices[0][1], 
                  vertices[4][0], vertices[4][1],
                  vertices[7][0], vertices[7][1], 
                  vertices[3][0], vertices[3][1],
                  "#77FF77",
                  vertices[0][2]+vertices[4][2]+vertices[7][2]+vertices[3][2])
                 ,
                 (vertices[0][0], vertices[0][1], 
                  vertices[1][0], vertices[1][1],
                  vertices[2][0], vertices[2][1], 
                  vertices[3][0], vertices[3][1],
                  "#FF7777",
                  vertices[0][2]+vertices[1][2]+vertices[2][2]+vertices[3][2]) 
                 ,
                 (vertices[4][0], vertices[4][1], 
                  vertices[5][0], vertices[5][1],
                  vertices[6][0], vertices[6][1], 
                  vertices[7][0], vertices[7][1],
                  "#800000",
                  vertices[4][2]+vertices[5][2]+vertices[6][2]+vertices[7][2])
                 ,
                 (vertices[1][0], vertices[1][1], 
                  vertices[2][0], vertices[2][1],
                  vertices[6][0], vertices[6][1], 
                  vertices[5][0], vertices[5][1],
                  "#008000",
                  vertices[1][2]+vertices[2][2]+vertices[6][2]+vertices[5][2])
                 ,
                 (vertices[2][0], vertices[2][1], 
                  vertices[3][0], vertices[3][1],
                  vertices[7][0], vertices[7][1], 
                  vertices[6][0], vertices[6][1],
                  "#000080",
                  vertices[2][2]+vertices[3][2]+vertices[7][2]+vertices[6][2])]

        # Sort with descending z-value sums, the lowest z-value sum should appear most in front

        faces.sort (key=(lambda f: f[9]), reverse=True)

        canvas.create_polygon (faces[0][0:8], fill=faces[0][8])

        canvas.create_polygon (faces[1][0:8], fill=faces[1][8])

        canvas.create_polygon (faces[2][0:8], fill=faces[2][8])

        canvas.create_polygon (faces[3][0:8], fill=faces[3][8])

        canvas.create_polygon (faces[4][0:8], fill=faces[4][8])

        canvas.create_polygon (faces[5][0:8], fill=faces[5][8])


        # Draw Vertices
        # for i in range(8):
        #         canvas.create_oval (vertices[i][0]-DOT_RADIUS, vertices[i][1]                               -DOT_RADIUS, 
        #                         vertices[i][0]+DOT_RADIUS, vertices[i][1]+DOT_RADIUS,
        #                         fill="blue")



def rotate_CubeZ (vertices, rot):
        # rot is an angle in radians that determines how far we rotate the cube from its original position.

        #rotate around z-axis
        cos_r = cos (rot)
        sin_r = sin (rot)

        for v in vertices:
                x = v[0] - O_X
                y = v[1] - O_Y
                v[0] = O_X + x*cos_r - y*sin_r
                v[1] = O_Y + x*sin_r + y*cos_r



def rotate_CubeY (vertices, rot):
        # rot is an angle in radians that determines how far we rotate the cube from its original position.

        #rotate around y-axis
        cos_r = cos (rot)
        sin_r = sin (rot)

        for v in vertices:
                x = v[0] - O_X
                z = v[2]
                v[0] = O_X + x*cos_r - z*sin_r
                v[2] = x*sin_r + z*cos_r


def rotate_CubeX (vertices, rot):
        # rot is an angle in radians that determines how far we rotate the cube from its original position.

        #rotate around x-axis
        cos_r = cos (rot)
        sin_r = sin (rot)

        for v in vertices:
                y = v[1] - O_Y
                z = v[2]
                v[1] = O_Y + y*cos_r - z*sin_r
                v[2] = y*sin_r + z*cos_r



root = tk.Tk ()
root.geometry ('%dx%d+%d+%d' % (WIDTH, HEIGHT, 10, 10))
root.resizable (0, 0)       # Prevent resizing of windows, so we can keep center
root.title ("Simple 3D Cube")

canvas = tk.Canvas (root, width=WIDTH, height=HEIGHT)
canvas.pack ()

#greenbox_upper  = canvas.create_rectangle (25, 25, WIDTH-25, 50, fill="green")
#greenbox_lower  = canvas.create_rectangle (25, HEIGHT-25, WIDTH-25, HEIGHT-50, fill="green")

canvas.create_line (0, O_Y, WIDTH, O_Y, fill="red")
canvas.create_line (O_X, 0, O_X, HEIGHT, fill="red")

cube = create_Cube ()

rotate_CubeY (cube, PI/4)
rotate_CubeX (cube, atan (sqrt (2)))
#rotate_CubeZ (cube, -PI/6)

print (cube)

draw_Cube (cube)
root.update ()

time.sleep (2)

while (1):
        for i in range (FRAME_COUNT):
                canvas.create_line (0, O_Y, WIDTH, O_Y, fill="red")
                canvas.create_line (O_X, 0, O_X, HEIGHT, fill="red")

                #draw_Cube (0)
                rotate_CubeX (cube, 2*PI/FRAME_COUNT)
                draw_Cube (cube)
                root.update ()

                time.sleep (1/FPS)

                #if i != 11:
                canvas.delete ("all")

        for i in range (FRAME_COUNT):
                canvas.create_line (0, O_Y, WIDTH, O_Y, fill="red")
                canvas.create_line (O_X, 0, O_X, HEIGHT, fill="red")

                #draw_Cube (0)
                rotate_CubeY (cube, 2*PI/FRAME_COUNT)
                draw_Cube (cube)
                root.update ()

                time.sleep (1/FPS)

                #if i != 11:
                canvas.delete ("all")

        for i in range (FRAME_COUNT):
                canvas.create_line (0, O_Y, WIDTH, O_Y, fill="red")
                canvas.create_line (O_X, 0, O_X, HEIGHT, fill="red")

                #draw_Cube (0)
                rotate_CubeZ (cube, 2*PI/FRAME_COUNT)
                draw_Cube (cube)
                root.update ()

                time.sleep (1/FPS)

                #if i != 11:
                canvas.delete ("all")


root.mainloop ()

