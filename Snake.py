import pygame

class Snake:
    def __init__(self, xPos, yPos, width, height, speed):
        self.xPos = xPos
        self.yPos = yPos
        self.width = width
        self.height = height
        self.speed = speed
        self.x = 0
        self.y = 0
        self.prevX = 0
        self.prevY = 0
        self.segments = [self]


    def Move(self,screen):
        keys = pygame.key.get_pressed()
        # Lock controls so you cant move backwards into yourself
        if keys[pygame.K_w] and self.y != 1 or keys[pygame.K_UP] and self.y != 1:
            self.y = -1
            self.x = 0
        elif keys[pygame.K_s] and self.y != -1 or keys[pygame.K_DOWN] and self.y != -1:
            self.y = 1
            self.x = 0
        elif keys[pygame.K_a] and self.x != 1 or keys[pygame.K_LEFT] and self.x != 1:
            self.x = -1
            self.y = 0
        elif keys[pygame.K_d] and self.x != -1 or keys[pygame.K_RIGHT] and self.x != -1:
            self.x = 1
            self.y = 0
        self.prevX = self.xPos
        self.prevY = self.yPos
        self.xPos += self.speed * self.x
        self.yPos += self.speed * self.y
        self.Draw(screen)

    def checkCollision(self):
        # Loop throug hevery segment and check if it collided with the head
        for x in range(self.segments.__len__() - 1):
            # Ignore first segment as its the head.
            if x > 0:
                if self.segments[x].xPos > self.xPos - self.width / 2 and self.segments[x].xPos < self.xPos + self.width / 2 and self.segments[x].yPos > self.yPos - self.height / 2 and self.segments[x].yPos < self.yPos + self.height / 2:
                    return True   

    def Draw(self,screen):
        index = 0
        # The snakes head will be the first segment so it should draw normally
        for segment in self.segments:
            if index == 0:
                pygame.draw.rect(screen,(0,255,0), pygame.Rect(segment.xPos,segment.yPos,self.width,self.height), 10, 10)
            else:
                # Other segments should be drawn to the previous position of the previous segment to create the snake movement effect
                # The previous position should be saved for the next segment
                segment.prevX = segment.xPos
                segment.prevY = segment.yPos
                segment.xPos = self.segments[index-1].prevX
                segment.yPos = self.segments[index-1].prevY
                pygame.draw.rect(screen,(0,255,0), pygame.Rect(segment.xPos,segment.yPos,self.width,self.height), 10, 10)
            index +=1
     


    def grow(self):
        # Attach new snake segment to the previous position of the last segment. The speed here is irrelevant as these segments wont be controlled
        # And will simply update the position based on the head
        newSegment = Snake(self.segments[-1].prevX - self.width,self.segments[-1].prevY,self.width,self.height,100)
        self.segments.append(newSegment)
        pass
