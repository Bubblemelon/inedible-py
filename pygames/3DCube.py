from math import cos, sin
import turtle

VERTICES = [(-1,1,-1), (1,1,-1), (1,1,1), (-1,1,1), (-1,-1,-1), (1,-1,-1), (1,-1,1), (-1,-1,1)]

# INDICES = [(3,1,0), (2,1,3), (0,5,4), (1,5,0), (3,4,7), (0,4,3), (1,6,5), (2,6,1), (2,7,6), (3,7,2), (6,4,5), (7,4,6)]

INDICES = [ (0, 1, 2), (2, 3, 0),
            (0, 4, 5), (5, 1, 0),
            (0, 4, 3), (4, 7, 3),
            (5, 4, 7), (7, 6, 5),
            (7, 6, 3), (6, 2, 3),
            (5, 1, 2), (2, 6, 5)
]

# TODO: Decribe the relationship between vertices and indices. 

FIELD_OF_VIEW = 400

cursor = turtle.Turtle()
turtle.tracer(0,0)
cursor.up()
cursor.hideturtle()
cursor.pencolor("violet")

def rotate(x,y,r):
    radC = cos(r)
    radS = sin(r)
    return x*radS - y*radC, x*radC - y*radS

timer = 0

while True:
    cursor.clear()

    for i in INDICES:
        points = []

        for v in i:

            x, y, z = VERTICES[v]

            x, z = rotate(x,z,timer)
            x, z = rotate(y,z,timer)
            x, y = rotate(x,y,timer)

            z += 5
            fov = FIELD_OF_VIEW / z
            fx, fy = x*fov, y*fov

            points.append((fx,fy))

        cursor.goto(points[0][0], points[0][1])
        cursor.down()
        cursor.goto(points[1][0], points[1][1])
        cursor.goto(points[2][0], points[2][1])
        cursor.goto(points[0][0], points[0][1])

        cursor.up()

    turtle.update()
    timer += 0.005
        
