# ATTENTION !!!!!!!!!
# THIS GAME IS REPLICATION OF "THE SCARY MAZE GAME" with Pygame by Vladislav Mihov
# THIS GAME IS SETTED UP FOR FULL HD (1920, 1080), USING SMALLER RESOLUTION MAY MADE THE GAME UNPLAYBLE

# Follow me on twitter @vladislavmihov : https://twitter.com/vladislavmihov
# Subcribe to my YouTube channel Skilldeliver: https://www.youtube.com/channel/UCAnKmkB6rqgLHzklNswLvrg

import pygame
import sys
from pygame.locals import *

pygame.init()

# SHORTCUT FUNC FOR TERMINATING THE GAME
def quit():
    pygame.quit()
    sys.exit()

# CONSTANT VARIABLES: SIZE, COLORS AND TITLE
SIZE = X, Y = (1920, 1080)
COLORS = BLACK, AQUA, RED, BLUE = (0, 0, 0), (0, 255, 255), (255, 51, 9), (4, 0, 104)
SURF = pygame.display.set_mode(SIZE, pygame.FULLSCREEN)
pygame.display.set_caption("Maze Game")

# SET THE CURSOR INVISIBLE AND USING SMALL RECTANGLE AS CURSOR
pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
cursorRect = pygame.Rect(50, 50, 10, 10)

# SET FONT
font = pygame.font.SysFont("Arial Black", 30)

# BOOLEANS USED
played = True
intro =  True
level1 = False
level2 = False
level3 = False
jumpScare = False

# AUXILIARY VARIABLES
time = 0
levelCount = 0

# LOADING MEDIA FILES, INTRO IMAGE, SCARY IMAGE AND SCARY SOUND
introIMG = pygame.image.load("Screenshot (324).png")
scarySOUND = pygame.mixer.Sound("Scary Maze Game Face and Sound (1)Trim.ogg")
scaryIMG = pygame.image.load("The-exorcist-scary-maze-game-ad-562083102.jpg")
scaryIMG = pygame.transform.scale(scaryIMG, (1920, 1080))
finalIMG = pygame.image.load("final.png")

# DATA STRUCTURES OF RECTANGLE ELEMENTS FOR EVERY LEVEL
lv1 = { "rect1": pygame.Rect(750, 300, 300, 625), \
        "rect2": pygame.Rect(750, 225, 650, 80),  \
        "finish": pygame.Rect(1390, 225, 125, 80)}

lv2 = { "rect1": pygame.Rect(595, 225, 905, 75),  \
        "rect2": pygame.Rect(525, 225, 75, 250),  \
        "rect3": pygame.Rect(600, 400, 825, 75),  \
        "rect4": pygame.Rect(1425, 400, 75, 250), \
        "rect5": pygame.Rect(600, 575, 825, 75),  \
        "rect6": pygame.Rect(525, 575, 75, 225),  \
        "rect7": pygame.Rect(600, 725, 700, 75),  \
        "rect8": pygame.Rect(1300, 725, 200, 225),\
        "rect9": pygame.Rect(625, 875, 675, 75),  \
        "finish": pygame.Rect(525, 875, 100, 75)}

lv3 = { "rect1": pygame.Rect(525, 875, 775, 75),  \
        "rect2": pygame.Rect(1300, 725, 75, 225), \
        "rect3": pygame.Rect(525, 700, 850, 75),  \
        "rect4": pygame.Rect(525, 475, 75, 245),  \
        "rect5": pygame.Rect(525, 475, 500, 55),  \
        "rect6": pygame.Rect(965, 475, 100, 15),  \
        "rect7": pygame.Rect(1050, 402, 15, 85),  \
        "rect8": pygame.Rect(985, 402, 75, 13),   \
        "rect9": pygame.Rect(975, 350, 13, 65),   \
        "rect10": pygame.Rect(975, 347, 90, 13),  \
        "rect11": pygame.Rect(1051, 275, 15, 85), \
        "finish": pygame.Rect(1033, 225, 50, 95)}

# GAME LOOP
while 1:
    # GET CURSOR POSITION AND MOVE THE RECTANGLE WITH THE CURSOR POSITION
    x, y = pygame.mouse.get_pos()
    cursorRect.top, cursorRect.left = y, x

    # CHECK FOR EVENTS
    for event in pygame.event.get():
        if event.type == KEYUP and event.key == K_ESCAPE: quit()

        # WHEN YOU PRESS THE BUTTON PLAY
        if event.type == MOUSEBUTTONDOWN and x > 851 and x < 1061 and y > 830 and y < 917 and intro:
            intro = False
            level1 = True

        # WHEN YOU ARE IN THE END AND PRESS BUTTON PLAY AGAIN
        if event.type == MOUSEBUTTONDOWN and jumpScare and x > 577 and x < 1244 and y > 677 and y < 815:  jumpScare = False; time = 0; intro = True
            
        # CHECK FOR CURSOR TO BE IN PATH RECTANGLES OR FINISH RECTANGLES /FOR ALL LEVELS
        if level1:
            levelCount = 1
            if x > (lv1["finish"].left - 5): level1 = False; level2 = True; intro = False
            if (not(x > (lv1["rect1"].left - 10) and x < lv1["rect1"].right and y > lv1["rect1"].top and y < lv1["rect1"].bottom)\
               and not(lv1["rect2"].left and x < lv1["rect2"].right and y > lv1["rect2"].top  - 10 and y < lv1["rect2"].bottom)): level1 = False; intro = True    
            
        if level2:
            levelCount = 2
            if x < lv2["finish"].right and y > lv2["finish"].top: level2 = False; intro = False; level3 = True
            if ( not(x > lv2["rect1"].left and x < lv2["rect1"].right and y > lv2["rect1"].top - 10 and y < lv2["rect1"].bottom)               \
               and not(x > lv2["rect2"].left - 10 and x < lv2["rect2"].right and y > lv2["rect2"].top - 10 and y < lv2["rect2"].bottom)        \
               and not (x > lv2["rect3"].left - 20 and x < lv2["rect3"].right + 20 and y > lv2["rect3"].top - 10 and y < lv2["rect3"].bottom)  \
               and not (x > lv2["rect4"].left - 10 and x < lv2["rect4"].right and y > lv2["rect4"].top - 10 and y < lv2["rect4"].bottom)       \
               and not (x > lv2["rect5"].left - 20 and x < lv2["rect5"].right + 20 and y > lv2["rect5"].top - 10 and y < lv2["rect5"].bottom)  \
               and not (x > lv2["rect6"].left - 10 and x < lv2["rect6"].right and y > lv2["rect6"].top - 10 and y < lv2["rect6"].bottom)       \
               and not (x > lv2["rect7"].left - 20 and x < lv2["rect7"].right + 20 and y > lv2["rect7"].top - 10 and y < lv2["rect7"].bottom)  \
               and not (x > lv2["rect8"].left - 10 and x < lv2["rect8"].right and y > lv2["rect8"].top - 10 and y < lv2["rect8"].bottom)       \
               and not (x > lv2["rect9"].left - 20 and x < lv2["rect9"].right + 30 and y > lv2["rect9"].top - 10 and y < lv2["rect9"].bottom)): level2 = False; intro = True

        if level3:
            levelCount = 3
            if y < 429:
                level = False
                jumpScare = True
            if ((not (x > lv3["rect1"].left - 10 and x < lv3["rect1"].right + 20 and y > lv3["rect1"].top - 10 and y < lv3["rect1"].bottom))     \
               and (not (x > lv3["rect2"].left - 10 and x < lv3["rect2"].right and y > lv3["rect2"].top - 10 and y < lv3["rect2"].bottom))       \
               and (not (x > lv3["rect3"].left - 20 and x < lv3["rect3"].right + 20 and y > lv3["rect3"].top - 10 and y < lv3["rect3"].bottom))  \
               and (not (x > lv3["rect4"].left - 10 and x < lv3["rect4"].right and y > lv3["rect4"].top - 10 and y < lv3["rect4"].bottom))       \
               and (not (x > lv3["rect5"].left - 20 and x < lv3["rect5"].right + 20 and y > lv3["rect5"].top - 10 and y < lv3["rect5"].bottom))  \
               and (not (x > lv3["rect6"].left - 10 and x < lv3["rect6"].right and y > lv3["rect6"].top - 10 and y < lv3["rect6"].bottom))       \
               and (not (x > lv3["rect7"].left - 20 and x < lv3["rect7"].right + 20 and y > lv3["rect7"].top - 10 and y < lv3["rect7"].bottom))  \
               and (not (x > lv3["rect8"].left - 10 and x < lv3["rect8"].right and y > lv3["rect8"].top - 10 and y < lv3["rect8"].bottom))): level3 = False; intro = True
   
    # LEVEL TEXT
    levelText = font.render("Level " + str(levelCount), True, (255, 255, 255))

    # BACKGROUND COLOR
    SURF.fill(BLACK)

    # DRAWING ALL ELEMENTS OR BLITING IMAGES
    if intro:
        SURF.blit(introIMG, (350, 75))

    if level1:
        for i in lv1:
            if i == "finish":
                pygame.draw.rect(SURF, RED, lv1[i])
            else: pygame.draw.rect(SURF, AQUA, lv1[i])
        SURF.blit(levelText, (1395, 315))

    if level2:
        for i in lv2:
            if i == "finish":
                pygame.draw.rect(SURF, RED, lv2[i])
            else: pygame.draw.rect(SURF, AQUA, lv2[i])
        SURF.blit(levelText, (520, 815))

    if level3:
        for i in lv3:
            if i == "finish":
                pygame.draw.rect(SURF, RED, lv3[i])
            else: pygame.draw.rect(SURF, AQUA, lv3[i])
        SURF.blit(levelText, (1090, 283))

    if jumpScare:
        if played: scarySOUND.play(); played = False
        SURF.blit(scaryIMG, (0, 0))  
        time += 1
        if time > 200:
            SURF.fill(BLACK)
            SURF.blit(finalIMG, (300, 50))

    # DRAWING THE CURSOR AND UPDATING DISPLAY
    pygame.draw.rect(SURF, BLUE, cursorRect)
    pygame.display.update()