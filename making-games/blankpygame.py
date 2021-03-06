import pygame
import time
import random

pygame.init() # initializes modules in pygame.
    
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height)) #returns surface obj

pygame.display.set_caption("Slither") # giving the title of the game

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

clock = pygame.time.Clock()

block_size = 10
FPS = 30
font = pygame.font.SysFont(None, 25) #25 is size

def message_to_screen(msg, color):
        screen_text = font.render(msg, True, color)
        gameDisplay.blit(screen_text, [display_width/2, display_height/2])
        #putting the msg in the game Display object we created

        
def gameLoop():
    gameExit = False
    gameOver = False
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = 0
    apple_x = (random.randint(0, display_width - 1) // 10) * 10
    apple_y = (random.randint(0, display_height - 1) // 10) * 10
    
    while not gameExit:
            
        if gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("You lose you fool", red)
            pygame.display.update()
            time.sleep(2)
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over. Press C to play again or Q to quit", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # quit event handling
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x < 0 or lead_x >= display_width or \
           lead_y < 0 or lead_y >= display_height:
            gameOver = True

        if lead_x == apple_x and lead_y == apple_y:
            print("ate the apple")
                
        lead_x += lead_x_change
        lead_y += lead_y_change
        
        gameDisplay.fill(white) 
        pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, block_size, block_size])
        pygame.draw.rect(gameDisplay, red, [apple_x, apple_y, block_size, block_size])
        pygame.display.update()
        

        clock.tick(FPS) #defines how many frames per second

    pygame.quit()
    quit()


# 5) Colors and fill: can load in pic from photoshop etc. but, there's built-in
#on pygame, by coordinates. fill()
# 6) Draw rect and Fill: pygame.draw.rect or gameDisplay.fill(...)
# 7) Moving Rectangle
# 8) Moving objects
# 9) Frames per second: 2nd option of changing speed. change var first
# 10) More User Control
# 11) Moving up
# 12) Boundaries
# 13) fix hardcoding
# 14) adding text to the screen (render, blit, font)
# 15) game over functionality
# 16) adding an apple
        



"""
#between fill() and update(): render allt eh other graphics
pygame.init() # I need to have it
#now I need to get my surface, the game screen, display
gameDisplay = pygame.display.set_mode((800, 600)) #height and width of display
#need to update the display
#similar functions. 
#pygame.display.flip() #updates entire surface all at once
pygame.display.update() #updates just the surface u want. if u send no parameterit updates the whole function. For that, update()is the most used instead for flip()
pygame.quit() #exit pygame, desinicia
quit() #that's what exits python
#gameDisplay.fill(red, rect = [200, 200, 50, 50]) #coord, format
if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    lead_x_change = 0 # how to make it move while you're pressing key, and making it stop when you stop pressing it
"""



                        
