import pygame
from pygame import *

pygame.init() #Needed to initialize any pygame

screen_width = 1600
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height)) #Sets screen size for the game

pygame.display.set_caption("It's a me... Man... Not Mario") #This sets the caption seen in the tab window
#Code below sets grahics for the walking and standing motion
walkRight = [pygame.image.load('Images/Mario_R_2.png'), pygame.image.load('Images/Mario_R_1.png'), pygame.image.load('Images/Mario_R_3.png'), pygame.image.load('Images/Mario_R_2.png'), pygame.image.load('Images/Mario_R_1.png'), pygame.image.load('Images/Mario_R_3.png'), pygame.image.load('Images/Mario_R_2.png'), pygame.image.load('Images/Mario_R_1.png'), pygame.image.load('Images/Mario_R_3.png')]
walkLeft = [pygame.image.load('Images/Mario_L_2.png'), pygame.image.load('Images/Mario_L_1.png'), pygame.image.load('Images/Mario_L_3.png'), pygame.image.load('Images/Mario_L_2.png'), pygame.image.load('Images/Mario_L_1.png'), pygame.image.load('Images/Mario_L_3.png'), pygame.image.load('Images/Mario_L_2.png'), pygame.image.load('Images/Mario_L_1.png'), pygame.image.load('Images/Mario_L_3.png')]
background = pygame.image.load('Images/CC.png')
standingChar = pygame.image.load('Images/Mario_standing.png')

clock = pygame.time.Clock() #sets var for the clockrate so the game goes at a steady framerate rather the speed of your processor on your pc

class player():
    """Make an easy way to make a multiple players."""
    def __init__(self, x, y, width, height):
        """creating char info"""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, screen):
        """Draws to screen."""
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            screen.blit(walkLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            screen.blit(walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
            screen.blit(standingChar, (self.x, self.y))
def redrawGameWindow():
    """Draws updated images."""
    
    screen.blit(background, (0, 0)) #Update background
    man.draw(screen) #Update char (Mario)
    pygame.display.update() #Update screen size


#MainLoop
man = player((screen_width/2)- 80, screen_height - 250, 64, 64)
run = True
while run:
    """While loop for checking and updating screen until you quit."""
    clock.tick(27)
    
    for event in pygame.event.get():
        """Check for quit of the game."""
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed() #Grabs key pressed and stores in this value
    
    if keys[pygame.K_LEFT] and man.x > man.vel:
        """Check for left key press."""
        man.x -= man.vel
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < screen_width - man.width - man.vel - 50:
        """Check for right key press."""
        man.x += man.vel
        man.right = True
        man.left = False
    else:
        """default values at False and zero."""
        man.right = False
        man.left = False
        man.walkCount = 0
    if not(man.isJump):
        """Is mario in the air?"""
        if keys[pygame.K_SPACE]:
            """Was the spacebar pressed? Find out right after these short messages."""
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        """Air time formula."""
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount <0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            """After char lands, vals get set to default."""
            man.isJump = False
            man.jumpCount = 10
    
    redrawGameWindow() #Do you want to see the next frame??? Neither do I...
pygame.quit() #This is the command of all commands. THe lines in the flag that resemble freedom. The last line, but not the least. The line that allows you to be free to leave without all hell breakin loose. If you read all the way to this point, then you are a beast. Thanks for reading. Hope you like the code.... This line tells the system to leave the game by the way... In case you were wanting to know