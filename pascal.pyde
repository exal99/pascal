from pascal import *

add_library("peasycam")

cam = None

rotX, rotY, rotZ = 0, 0, 0

tri = None

box_size = 100

def setup():
    global tri
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
    point(0,0,0)
    #makeGrid(10,10,10)
    #drawPlane(0, 0, 0, getPlaneAt(5))
    drawTetrahedron(0,0,0, tri)
    #cubeText(0,0,0, "1")
    
def keyPressed():
    global tri
    if key == "+":
        if len(tri) == 0:
            tri = [[[1]]]
        else:
            tri.append(pascalPlane(len(tri) + 1, tri[-1]))
    if key == "-":
        tri = tri[:-1]
    
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
        """
        stroke(255,0,0)
        strokeWeight(10)
        line(-10, 0, 0, 10, 0, 0)
        stroke(0,255,0)
        line(0,-10,0,0,10,0)
        """
    pushMatrix()
    translate(x, y, z)
    fill(255)
    text(t, 0,0)
    popMatrix()
    """
    for ind, pos in enumerate(((x, y-box_size/2), (x + box_size/2, y), (x, y + box_size/2), (x - box_size/2, y))):
        pushMatrix()
        translate(pos[0],pos[1], z)
        rotateZ(ind * PI/2)
        rotateX(PI/2)
        text(t, 0, 0)
        popMatrix()
    pushMatrix()
    translate(x, y, z-box_size/2)
    rotateZ(PI)
    text(t, 0, 0)
    popMatrix()
    pushMatrix()
    translate(x, y, z+box_size/2)
    rotateZ(PI)
    text(t, 0, 0)
    popMatrix()
    """
    
    
def drawTetrahedron(x,y,z, tetrahedron):
    for plane_z, plane in enumerate(tetrahedron):
        drawPlane(x, y, plane_z * box_size + z, plane)

def good_range(beginning, s, step):
    a = beginning
    while a < s:
        yield a
        a += step

def drawPlane(x,y,z, plane):
    unitLength = 50
    sideLength = sqrt(2 * len(plane)/sqrt(3)) * unitLength
    #row, col = 0,0
    print(plane)
    print(x, y, z)
    y_start = y + (sqrt(3)/2 - 1/sqrt(3)) * sideLength
    
    for row, cell_y in enumerate(good_range(y_start, y_start + sqrt(3)/2 * unitLength * len(plane), sqrt(3)/2 * unitLength)):
        print(x - 0.5 * row * unitLength, unitLength * len(plane[row]), unitLength)
        for col, cell_x in enumerate(good_range(x - 0.5 * row * unitLength, unitLength * len(plane[row]), unitLength)):
            pushMatrix()
            translate(cell_x, cell_y, z)
            textSize(32)
            print(row, col, cell_x, cell_y)
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
                