from pascal import *

add_library("peasycam")

cam = None

rotX, rotY, rotZ = 0, 0, 0

tri = None


unitLength = 100

pan_move = (0,0)

def setup():
    global tri, cam
    size(800, 600, P3D)
    cam = PeasyCam(this, 100)
    cam.setMinimumDistance(50)
    cam.setMaximumDistance(5000)
    tri = pascal3D(5)
    print(len(tri))
    

def draw():
    global tri
    background(0)
    fill(255, 0,0)
    strokeWeight(5)
    drawTetrahedron(0,0,0, tri)
    cam.pan(*pan_move)
    #noLoop()
    
def keyPressed():
    global tri, pan_move
    if key == "+":
        if len(tri) == 0:
            tri = [[[1]]]
        else:
            tri.append(pascalPlane(len(tri) + 1, tri[-1]))
    if key == "-":
        tri = tri[:-1]
    
    pan_speed = 5
    if key == "w":
        pan_move = (0, -pan_speed)
    if key == "a":
        pan_move = (-pan_speed, 0)
    if key == "s":
        pan_move = (0, pan_speed)
    if key == "d":
        pan_move = (pan_speed, 0)

def keyReleased():
    global pan_move
    if key in ("w", "a", "s", "d"):
        pan_move = (0,0)
    
def cubeText(x,y,z, t):
    debug = False
    textAlign(CENTER)
    rectMode(CENTER)
    noFill()
    if debug:
        pushMatrix()
        translate(x,y,z)
        stroke(255)
        strokeWeight(1)
        box(box_size)
        strokeWeight(10)
        point(0,0,0)
        popMatrix()
    pushMatrix()
    translate(x, y, z)
    orientation = cam.getRotations() if cam else (0,0,0)
    rotateX(orientation[0])
    rotateY(orientation[1])
    rotateZ(orientation[2])
    fill(255)
    text(t, 0,0)
    popMatrix()
    
    
def drawTetrahedron(x,y,z, tetrahedron):
    for plane_z, plane in enumerate(tetrahedron):
        drawPlane(x, y, plane_z * unitLength * sqrt(3)/2 + z, plane)

def good_range(beginning, s, step):
    a = beginning
    while a < s:
        yield a
        a += step

def drawPlane(x,y,z, plane):
    sideLength = sqrt(2 * len(plane)/sqrt(3)) * unitLength
    #row, col = 0,0
    y_start = y - (sqrt(3)/2 - 1/sqrt(3)) * sideLength * len(plane) / 2 if len(plane) != 1 else 0
    #print(plane)
    for row, cell_y in enumerate(good_range(y_start, y_start + sqrt(3)/2 * unitLength * len(plane), sqrt(3)/2 * unitLength)):
        x_start = x - 0.5 * row * unitLength
        for col, cell_x in enumerate(good_range(x_start, unitLength * len(plane[row]) + x_start, unitLength)):
            pushMatrix()
            translate(cell_x, cell_y, z)
            textSize(32)
            #print(cell_x, cell_y)
            cubeText(0, 0, 0, plane[row][col])
            popMatrix()

def makeGrid(w, h, d):
    for z in range(0, box_size * h, box_size):
        for y in range(0, box_size * d, box_size):
            for x in range(0, box_size * w, box_size):
                pushMatrix()
                translate(x,y,z)
                cubeText(0, 0, 0, "%d %d %d" %(x, y, z))
                fill(0,0,255)
                #box(5)
                popMatrix()
                