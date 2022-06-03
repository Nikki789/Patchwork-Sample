from graphics import * 
#Main function to call derivative functions
def main():
    size,inputtedColours = getInputs()
    drawPatchwork(size,inputtedColours)
    
#Get inputs function - calls functions to get size and colours
def getInputs():
    size = getSize()
    inputtedColours = getColours()
    return size,inputtedColours
    
#Get Size function - gets input, checks if it's a digit then checks if it's in the valid sizes
#IsDigit - Checks if the entered number is positive integer instead of float
#Returns: Int size
def getSize():
    validSizes = [5,7,9]
    size = 0
    while size not in validSizes:
        size = input("Please enter a size from [5,7,9]: ")
        if size.isdigit() and int(size) in validSizes:
            size = int(size)
        else:
            print("Invalid size entered,please try again")
    return size

#Get colours function: Takes input,compares to list of acceptable colours
#Removes accepted entries from comparison list and displays remaining entries
#Returns: List of strings containing the inputted colours
def getColours():
    acceptedColours = ["red","green","blue","magenta","orange","pink"]
    inputtedColours = []
    while len(inputtedColours) < 3:
        colour = input("\nPlease enter three colours - red,green,blue,magenta,orange,pink: ")
        if (colour not in acceptedColours):
            if (colour in inputtedColours):
                print("Colour " +  colour +  " already entered,please try again")
            else:
                print("Invalid colour entered,please try again")
        else:
            inputtedColours.append(colour)
            acceptedColours.remove(colour)
    return inputtedColours

#Function to draw a basic triangle
#Parameter: win: Graphics window
#Parameter: p1: the top left point of the triangle
#Parameter: p2: the top right point of the triangle
#Parameter: p3: the bottom left point of the triangle
#Parameter: colour: the user decides colour for the triangle
def drawTriangle(win,p1,p2,p3,colour):
    triangle = Polygon(p1,p2,p3)
    triangle.setFill(colour)
    triangle.setOutline(colour)
    triangle.draw(win)
    
#Function to draw a basic circle
#Parameter: win: Graphics window
#Parameter: centre:the centre of the circle
#Parameter: radius:the radius of the circle
#Parameter: colour: the user decides colour for the circle
def drawCircle(win, centre, radius,colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setOutline(colour) 
    circle.draw(win) 

#Function finalNumPatch - draws the final number patch
#Parameter: win: Graphics window
#Parameter: topx,topy: the x- and y-coordinates of the top-left corner of the patch
#Parameter: colour: user's inputted colour
def finalNumPatchwork(win,topx,topy,colour):
    for rectx in range (90,-10,-10):
            rect = Rectangle(Point(topx+rectx, topy+90-rectx), Point(topx+rectx+10,topy+100-rectx))
            rect.setFill(colour)
            rect.setOutline(colour)
            rect.draw(win)
            

#Function penultimateNumPatchwork - draws the penultimate number patch
#Parameter: win: Graphics window
#Parameter: topx,topy: the x- and y-coordinates of the top-left corner of the patch
#Parameter: colour: user's inputted colour
def penultimateNumPatchwork(win,topx,topy,colour):
    for y in range(0,100,40):
        for x in range(0,100,40):
            drawTriangle(win,Point(x+topx,y+topy),Point(20+x+topx,y+topy),Point(10+x+topx,10+y+topy),colour)
            
            drawTriangle(win,Point(x+topx,10+y+topy),Point(20+x+topx,10+y+topy),Point(10+x+topx,20+y+topy),colour)
        for j in range(30,80,40):
            drawCircle(win,Point(j+topx,10+y+topy),10,colour)
    for y1 in range(30,80,40):
        for centreX in range(10,100,40):
            drawCircle(win,Point(centreX+topx,y1+topy),10,colour)
        for triangleX in range(20,90,40):
            drawTriangle(win,Point(triangleX+topx,y1-10+topy),Point(triangleX+10+topx,y1+topy),Point(triangleX+topx,y1+10+topy),colour)
            drawTriangle(win,Point(triangleX+10+topx,y1-10+topy),Point(triangleX+20+topx,y1+topy),Point(triangleX+10+topx,y1+10+topy),colour)


#Main function to draw patchwork
#Parameter: Size: Size of screen as int 
#Parameter: InputtedColours: decides colouration
def drawPatchwork(size,inputtedColours):
    win = GraphWin("Patchwork", size*100,size*100)
    #Draws the finalNumPatchwork
    #topy:columns;topx:rows
    for topy in range(0, size):
        for topx in range(topy, size - topy):
            finalNumPatchwork(win,topx*100,topy*100,inputtedColours[0])
        for topx in range((size -1) - topy,topy + 1):
            finalNumPatchwork(win,topx*100,topy*100,inputtedColours[0])
    #Draws the penultimateNumPatchwork
    #topx:columns;topy:rows
    for topx in range(0,size//2):
        for topy in range(topx + 1,size-1 - topx):
            penultimateNumPatchwork(win,topx*100,topy*100,inputtedColours[1])
    for topx in range(3,size):
        for topy in range(size-topx,topx):
            penultimateNumPatchwork(win,topx*100,topy*100,inputtedColours[2])
   


    