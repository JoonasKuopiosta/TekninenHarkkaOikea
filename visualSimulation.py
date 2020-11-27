from graphics import *
import time

class VisualSimulation:

    def __init__(self, width, height, worldWidth, worldHeight, personList, obstacleList):
        self.width          = width
        self.height         = height
        self.worldWidth     = worldWidth
        self.worldHeight    = worldHeight
        self.widthRatio     = width / worldWidth
        self.heightRatio    = height / worldHeight
        
        self.win = self.graphicsInit(personList, obstacleList)
        
    
    
    def graphicsInit(self, personList, obstacleList):
        win = GraphWin(width = self.width, height = self.height, autoflush=False) # create a window
        win.setCoords(0, 0, self.width, self.height)
        
        for person in personList:
            
            shapes = person.getDraw()
            for shape in shapes:
                shape.draw(win) # draw it to the window
        
        for obstacle in obstacleList:
            
            #line = obstacle.getDraw()
            #line.draw(win)
            
            cords0 = self.worldCordsToScreen([obstacle.x0, obstacle.y0])
            cords1 = self.worldCordsToScreen([obstacle.x1, obstacle.y1])
            
            newPos0 = Point(cords0[0], cords0[1])
            newPos1 = Point(cords1[0], cords1[1])
            
            newLine = Line(newPos0, newPos1)
            obstacle.line = newLine
            newLine.draw(win)
        
        return win
        


    def animationStep(self, personList, obstacleList):
        for person in personList:
            
            cords = self.worldCordsToScreen([person.x, person.y])
            
            newPos = Point(cords[0], cords[1])
            
            shapes = person.getDraw()
            
            self.movePersonGraphicsTo(shapes, newPos)
            
        
        self.win.update()
    
    
    def animationFinal(self):
        time.sleep(1)
        self.win.getMouse() # Waits the user to click the screen
        self.win.close()
    
    
    def worldCordsToScreen(self, cords):
        
        worldX = cords[0]
        worldY = cords[1]
        
        screenX = worldX * self.widthRatio
        screenY = worldY * self.heightRatio
        
        return [screenX, screenY]
    
    
    def movePersonGraphicsTo(self, shapes, newCenter):
        
        myNewX = newCenter.getX()
        myNewY = newCenter.getY()
        
        oldCenter = shapes[0].getCenter()
            
        myXUpd = myNewX - oldCenter.getX()
        myYUpd = myNewY - oldCenter.getY()
        
        for shape in shapes:
        
            shape.move(myXUpd, myYUpd)
        
        return True
    
    #def moveLineTo(self, line, newPos0, newPos1):
        
        