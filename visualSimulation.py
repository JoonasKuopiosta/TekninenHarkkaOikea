from graphics import *
import time

class VisualSimulation:

    def __init__(self, width, height, worldWidth, worldHeight, personList):
        self.width          = width
        self.height         = height
        self.worldWidth     = worldWidth
        self.worldHeight    = worldHeight
        self.widthRatio     = width / worldWidth
        self.heightRatio    = height / worldHeight
        
        self.win = self.graphicsInit(personList)
        
    
    
    def graphicsInit(self, personList):
        win = GraphWin(width = self.width, height = self.height, autoflush=False) # create a window
        win.setCoords(0, 0, self.width, self.height)
        
        for person in personList:
            
            circle = person.getDraw()
            circle.draw(win) # draw it to the window
        
        return win
        


    def animationStep(self, personList):
        for person in personList:
            cords = self.worldCordsToScreen([person.x, person.y])
            
            newPos = Point(cords[0], cords[1])
            
            circle = person.getDraw()
            self.moveTo(circle, newPos)
            
            #circle.setFill('blue')
        
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
    
    
    def moveTo(self, shape, newCenter):
        myNewX = newCenter.getX()
        myNewY = newCenter.getY()
        
        oldCenter = shape.getCenter()
        
        myXUpd = myNewX - oldCenter.getX()
        myYUpd = myNewY - oldCenter.getY()
        
        shape.move(myXUpd, myYUpd)
        
        return myNewX, myNewY
        
        