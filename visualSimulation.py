from graphics import *
import time
from PIL import ImageGrab
import win32gui
import math

GREEN = "#009E73"
VERMIL = "#D55E00"
BLUE = "#0072B2"

colorList = [GREEN, VERMIL, BLUE]
typeList = ["Suspectible", "Infectious", "Resistant"]

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
        win = GraphWin(title="Tekninen harkka simulaatio", width = self.width, height = self.height, autoflush=False) # create a window
        win.setCoords(0, 0, self.width, self.height)

        # Time stamps in an ugly manner
        # For days
        textAnchorDays = Point(self.width - 110, self.height - 10)
        self.timeStampDays = Text(textAnchorDays, "asdasdasdasd")
        self.timeStampDays.setTextColor('black')
        self.timeStampDays.setSize(12)
        self.timeStampDays.draw(win)

        # For hours
        textAnchorHours = Point(self.width - 40, self.height - 10)
        self.timeStampHours = Text(textAnchorHours, "asdasdasdasd")
        self.timeStampHours.setTextColor('black')
        self.timeStampHours.setSize(12)
        self.timeStampHours.draw(win)
        
        for i in range(0, len(colorList)):
            textAnchor = Point(self.width - 50, self.height - (27 + i*17))
            text = Text(textAnchor, typeList[i])
            text.setTextColor(colorList[i])
            text.setSize(13)
            text.draw(win)
        
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


    def animationStep(self, personList, obstacleList, timeInMinutes):
        
        # Updating times in an ugly fashion
        timeList = self.timeFormatter(timeInMinutes)
        self.timeStampDays.setText("Days:" + str(timeList[0]+1))
        self.timeStampHours.setText("Hours:" + str(timeList[1]))
                
        for person in personList:
            
            cords = self.worldCordsToScreen([person.x, person.y])
            
            newPos = Point(cords[0], cords[1])
            
            shapes = person.getDraw()
            
            self.movePersonGraphicsTo(shapes, newPos)
            
        
        self.win.update()
    

    def timeFormatter(self, minutes):
        
        # How many days in minutes
        fullDays = math.floor(minutes / (60*24))
        # Substract the fullDays worth of minutes from the total
        minutes -= fullDays * 60*24

        fullHours = math.floor(minutes / (60))

        return [fullDays, fullHours]
    
    
    def animationFinal(self):
        time.sleep(1)
        self.win.getMouse() # Waits the user to click the screen
        self.win.close()
    

    def takeSnapshot(self, imageNumber):

        # Find the simulation window
        hwnd = win32gui.FindWindow(None, r'Tekninen harkka simulaatio')
        win32gui.SetForegroundWindow(hwnd)
        dimensions = win32gui.GetWindowRect(hwnd)

        # Takes the screenshot and saves it with index number
        image = ImageGrab.grab(dimensions)
        fileName = "./images/TekninenSimulaatio_" + str(imageNumber) + ".jpg"
        image.save(fileName, "JPEG")
    
    
    def worldCordsToScreen(self, cords):
        
        # person's xy-coordinates in the world:
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
        
        