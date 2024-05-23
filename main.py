import pygame
from Snake import *
from Food import *
from GameManager import *

def main():
    # Size of window
    screenWidth = 500
    screenHeight = 700
    # Create window and clock which will be used for FPS
    pygame.init()
    screen = pygame.display.set_mode((screenWidth,screenHeight))
    clock = pygame.time.Clock()
    running = True
    gameOver = False
    # Snake size
    snakeWidth = 25
    snakeHeight = 25
    # Offset will be size of a tile since the game will run in a grid
    offset = 20         
    # The speed is calculated based on the offset to make the snake move tile to tile    
    snakeSpeed = screenWidth / offset       
    snake = Snake(225,250,snakeWidth,snakeHeight,snakeSpeed)
    # Game manager tracks score
    gameManager = GameManager()
    # Food with the same size as the snake
    food = Food(snakeWidth,snakeHeight)
    food.getSpawnPoints(screenWidth,screenHeight,offset)
    # Spawn in the food for the first time and pass it the gameManager for the score
    food.changePos(gameManager)
    retryButton = pygame.Rect(screenWidth / 2 - 60,screenHeight / 2 + 150,120,50)

    while running:
        # Clear screen to black
        screen.fill((0,0,0))
        food.update(screen,snake)
        # Check if snake is out of the screen. If it is then game is over
        if snake.xPos < 0 or snake.xPos > screenWidth - snakeWidth or snake.yPos < 0 or snake.yPos > screenHeight - snakeHeight:
            gameOver = True

        if gameOver == False:
            snake.Move(screen)
            collided = snake.checkCollision()
            if collided:
                gameOver = True
        else:
            snake.speed = 0

        # Show gameover screen
        if gameOver:
            gameOverScreen(screen,screenWidth,screenHeight,gameManager,retryButton)


        # Update screen
        pygame.display.flip()  
        # Wait 15 ms
        clock.tick(15)      

        # For closing the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                # if retry button is clicked restart game
            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                if retryButton.collidepoint(x,y) and gameOver:
                    # Create new snake and reset score and food pos
                    gameOver = False
                    food.changePos(0)
                    snake = Snake(225,250,snakeWidth,snakeHeight,snakeSpeed)
                    gameManager.score = 0
                    
# Function to create white text
def createText(screen,text,X,Y, size):
    font = pygame.font.Font(None,size)
    text = font.render(text, True, (255,255,255))
    textpos = text.get_rect(centerx = X, y = Y)
    screen.blit(text,textpos)

def gameOverScreen(screen,screenWidth,screenHeight,gameManager,retryButton):
    createText(screen,"Game over!",screenWidth / 2, screenHeight / 2,63)
    createText(screen,f"Score: {gameManager.score}",screenWidth / 2, screenHeight / 2 + 50,63)
    
    pygame.draw.rect(screen,(205,205,205), retryButton)
    createText(screen,f"Retry",screenWidth / 2, screenHeight / 2 + 160,32)

        


if __name__ == "__main__":
    main()