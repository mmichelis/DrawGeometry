from math import cos, sin, tan

PI = 3.1415927

class Cube:
    def __init__ (self, EDGE, O_X, O_Y, O_Z):
        """
        The way I draw my cube:
         5  6
        4  7
         1  2
        0  3
        """
        self.O_X = O_X
        self.O_Y = O_Y
        self.O_Z = O_Z

        self.vertices = [
            [O_X+0.5*EDGE, O_Y+0.5*EDGE, O_Z+0.5*EDGE],
            [O_X-0.5*EDGE, O_Y+0.5*EDGE, O_Z+0.5*EDGE],
            [O_X-0.5*EDGE, O_Y+0.5*EDGE, O_Z-0.5*EDGE], 
            [O_X+0.5*EDGE, O_Y+0.5*EDGE, O_Z-0.5*EDGE], 
            [O_X+0.5*EDGE, O_Y-0.5*EDGE, O_Z+0.5*EDGE], 
            [O_X-0.5*EDGE, O_Y-0.5*EDGE, O_Z+0.5*EDGE], 
            [O_X-0.5*EDGE, O_Y-0.5*EDGE, O_Z-0.5*EDGE], 
            [O_X+0.5*EDGE, O_Y-0.5*EDGE, O_Z-0.5*EDGE]
        ]


    def rotate_Z (self, rot):
        # rot is an angle in radians that determines how far we rotate the cube from its original position counterclockwise.

        #rotate around z-axis
        cos_r = cos (rot)
        sin_r = sin (rot)

        for v in self.vertices:
            x = v[0] - self.O_X
            y = v[1] - self.O_Y
            v[0] = self.O_X + x*cos_r - y*sin_r
            v[1] = self.O_Y + x*sin_r + y*cos_r


    def rotate_Y (self, rot):
        # rot is an angle in radians that determines how far we rotate the cube from its original position counterclockwise.

        #rotate around y-axis
        cos_r = cos (rot)
        sin_r = sin (rot)

        for v in self.vertices:
            x = v[0] - self.O_X
            z = v[2] - self.O_Z
            v[0] = self.O_X + x*cos_r - z*sin_r
            v[2] = self.O_Z + x*sin_r + z*cos_r


    def rotate_X (self, rot):
        # rot is an angle in radians that determines how far we rotate the cube from its original position counterclockwise.

        #rotate around x-axis
        cos_r = cos (rot)
        sin_r = sin (rot)

        for v in self.vertices:
            y = v[1] - self.O_Y
            z = v[2] - self.O_Z
            v[1] = self.O_Y + y*cos_r - z*sin_r
            v[2] = self.O_Z + y*sin_r + z*cos_r


    def draw (self, canvas):
        # Draw Faces
        # Store faces in a list

        vertices = self.vertices

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
        faces.sort (key=(lambda f: f[9]))

        canvas.create_polygon (faces[0][0:8], fill=faces[0][8])

        canvas.create_polygon (faces[1][0:8], fill=faces[1][8])

        canvas.create_polygon (faces[2][0:8], fill=faces[2][8])

        canvas.create_polygon (faces[3][0:8], fill=faces[3][8])

        canvas.create_polygon (faces[4][0:8], fill=faces[4][8])

        canvas.create_polygon (faces[5][0:8], fill=faces[5][8])



class Tetrahedron:
    def __init__ (self, EDGE, O_X, O_Y, O_Z):
        """
        The way I draw my tetrahedron:
          3
           1
         0  2 
        """
        self.O_X = O_X
        self.O_Y = O_Y
        self.O_Z = O_Z

        self.vertices = [
            [O_X-0.5*EDGE, O_Y+tan(PI/6)*0.5*EDGE, O_Z+tan(PI/6)*0.5*EDGE],
            [O_X         , O_Y+tan(PI/6)*0.5*EDGE, O_Z-0.5*EDGE/cos(PI/6)],
            [O_X+0.5*EDGE, O_Y+tan(PI/6)*0.5*EDGE, O_Z+tan(PI/6)*0.5*EDGE], 
            [O_X         , O_Y-0.5*EDGE/cos(PI/6), O_Z], 
        ]


    def rotate_Z (self, rot):
        # rot is an angle in radians that determines how far we rotate the cube from its original position counterclockwise.

        #rotate around z-axis
        cos_r = cos (rot)
        sin_r = sin (rot)

        for v in self.vertices:
            x = v[0] - self.O_X
            y = v[1] - self.O_Y
            v[0] = self.O_X + x*cos_r - y*sin_r
            v[1] = self.O_Y + x*sin_r + y*cos_r


    def rotate_Y (self, rot):
        # rot is an angle in radians that determines how far we rotate the cube from its original position counterclockwise.

        #rotate around y-axis
        cos_r = cos (rot)
        sin_r = sin (rot)

        for v in self.vertices:
            x = v[0] - self.O_X
            z = v[2] - self.O_Z
            v[0] = self.O_X + x*cos_r - z*sin_r
            v[2] = self.O_Z + x*sin_r + z*cos_r


    def rotate_X (self, rot):
        # rot is an angle in radians that determines how far we rotate the cube from its original position counterclockwise.

        #rotate around x-axis
        cos_r = cos (rot)
        sin_r = sin (rot)

        for v in self.vertices:
            y = v[1] - self.O_Y
            z = v[2] - self.O_Z
            v[1] = self.O_Y + y*cos_r - z*sin_r
            v[2] = self.O_Z + y*sin_r + z*cos_r


    def draw (self, canvas):
        # Draw Faces
        # Store faces in a list

        vertices = self.vertices

        faces = [(vertices[0][0], vertices[0][1], 
                  vertices[3][0], vertices[3][1],
                  vertices[2][0], vertices[2][1],
                  "#7777FF",
                  vertices[0][2]+vertices[3][2]+vertices[2][2])
                 ,
                 (vertices[0][0], vertices[0][1], 
                  vertices[1][0], vertices[1][1],
                  vertices[2][0], vertices[2][1],
                  "#FF7777",
                  vertices[0][2]+vertices[1][2]+vertices[2][2]) 
                 ,
                 (vertices[0][0], vertices[0][1], 
                  vertices[1][0], vertices[1][1],
                  vertices[3][0], vertices[3][1],
                  "#800000",
                  vertices[0][2]+vertices[1][2]+vertices[3][2])
                 ,
                 (vertices[1][0], vertices[1][1],
                  vertices[2][0], vertices[2][1], 
                  vertices[3][0], vertices[3][1],
                  "#000080",
                  vertices[1][2]+vertices[2][2]+vertices[3][2])]

        # Sort with descending z-value sums, the lowest z-value sum should appear most in front
        faces.sort (key=(lambda f: f[7]))

        canvas.create_polygon (faces[0][0:6], fill=faces[0][6])

        canvas.create_polygon (faces[1][0:6], fill=faces[1][6])

        canvas.create_polygon (faces[2][0:6], fill=faces[2][6])

        canvas.create_polygon (faces[3][0:6], fill=faces[3][6])

        

