import pygame
import random

class Food:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.xPos = 0
        self.yPos = 0
        self.gameManager = 0
        # Array of possible X and Y coordinates for the food to spawn in
        self.possibleW = [0]
        self.possibleH = [0]

    # Get X and Y points by getting each individual tiles position for both the width and height
    def getSpawnPoints(self,screenWidth,screenHeight,offset):
        index = 0
        widthOffset = screenWidth / offset

        while index < screenWidth - widthOffset:
            index+= widthOffset
            self.possibleW.append(index)

        index = 0
        while index < screenHeight - widthOffset:
            index += widthOffset
            self.possibleH.append(index)




    # Change pos to random X and Y
    def changePos(self,gM):
        # Pick one of the random X and Y coordinates to ensure a position in a tile
        x = random.randint(0,self.possibleW.__len__() - 1)
        y = random.randint(0,self.possibleH.__len__() - 1)


        self.xPos = self.possibleW[x]
        self.yPos = self.possibleH[y]
        # If gM is not yet gotten save it as it will be used for increasing score everytime the food is eaten
        if gM !=0:
            self.gameManager = gM
        
        if self.gameManager!=0:
            self.gameManager.score +=1

    # Check for collisions with snake
    def update(self,screen,snake):
        # Draw food on the screen with the red color. The last 10 and 10 is for rounding and for filling
        pygame.draw.rect(screen,(255,0,0), pygame.Rect(self.xPos,self.yPos,self.width,self.height),10, 10)

        # Check if the food has collided with the snake. Dividing the width and height by 2 to get the center of the collision to make it more accurate as without it
        # The collision happens even if the snake is not on the same tile.
        if snake.xPos > self.xPos - self.width /2 and snake.xPos < self.xPos + self.width /2 and snake.yPos > self.yPos - self.height /2 and snake.yPos < self.yPos + self.height /2:
            # Change pos again but gameManager is not needed since its saved from when it was called in main.py
            self.changePos(0)
            snake.grow()