
class Snake:
    """ Class for the Snake object which is made of head element and body elements stored in a list"""

    def __init__(self, lenght, startx, starty, size):
        """ The constuctor method where lenght argument is the lenght of the tile, startx is the starting x point for the starty same 
        but for the y point, the size is the cell size in general"""

        self.lenght = lenght
        self.startx = startx
        self.starty = starty
        self.size = size
        self.head = pg.Rect(self.startx, self.starty, self.size, self.size)
        self.tiles = []
        for i in range(1, lenght + 2):
            #appending the tiles elements for range of the lenght in the list
            self.tiles.append(pg.Rect(self.startx - (i * 20), self.starty - (i * 20), self.size, self.size))

    def move(self, event, pos):
        """ This method get the direction input from the keybord. "pos" stays for postdirection not for position. Poorly named variable, yeah"""

        if event.type == KEYDOWN:
            if (event.key == K_LEFT or event.key == K_a) and pos != "r": pos = "l"
            elif (event.key == K_RIGHT or event.key == K_d) and pos != "l": pos = "r" 
            elif (event.key == K_UP or event.key == K_w) and pos != "d": pos = "u"
            elif (event.key == K_DOWN or  event.key == K_s) and pos != "u": pos = "d"

        # With this for loop every tile element is history of the previous one. The first list element is history of the head.
        for rct in range(self.lenght, 0, -1):
            self.tiles[rct] = pg.Rect(self.tiles[rct - 1].left, self.tiles[rct - 1].top, self.size, self.size)    
        self.tiles[0] = pg.Rect(self.head.left, self.head.top, self.size, self.size)


        # The actual moving it is done with pygame rectange attributes adding or substacting the cellsize
        # We move only the head element, the body elements are handled by the upper for loop.
        if pos == "l": self.head.left -= 1 * self.size
        elif pos == "r": self.head.left += 1 * self.size
        elif pos == "u": self.head.top -= 1 * self.size
        elif pos == "d": self.head.top += 1 * self.size

        # return the pos for future usage in drawing method
        return pos

    def notValidSnake(self, screenx, screeny):
        """ This method return True if the snake head exit of display size or if the snake head collide with body element"""

        for item in self.tiles:
            # iterating the body list
            if self.head.colliderect(item): 
                return True
                # check if the snake head collided with body elemnt
            elif self.head.left > screenx - self.size or self.head.top > screeny - self.size or self.head.left < 0 or self.head.top < 0:
                return True
                # check if the snake head is out of the screen size with little size fix for the top and left end points, too long to explain 
        return False

    def draw(self, display, theme, pos):
        """ There is the drawing method. It takes the display, direction(pos) and current theme. Bliting all elements on the display"""

        for el in self.tiles: # we iterate the body list 
            DISP.blit(theme["snakeElement"], el) # and blit the coresponding snake element in the current theme

        #Bliting the head element it is a little bit more tricky because the head itself has different orientation which need to
        # corespond to the direction
        if pos == "l": DISP.blit(theme["snakeHead"]["left"], self.head)
        elif pos == "r": DISP.blit(theme["snakeHead"]["right"], self.head)
        elif pos == "u": DISP.blit(theme["snakeHead"]["up"], self.head)
        elif pos == "d": DISP.blit(theme["snakeHead"]["down"], self.head)

    def getrect(self):
        """ Return rect for further usage """
        return pg.Rect(self.head.left, self.head.top, self.size, self.size) 

    def addtile(self):
        """ This methods adds one more element to the body list when the snake eats the food """
        self.lenght += 1
        self.tiles.append(pg.Rect(self.tiles[self.lenght - 1].left, self.tiles[self.lenght - 1].top, self.size, self.size))

    def getbody(self):
        """ Return the body list for further usage """
        return self.tiles

    def getlenght(self):
        """ Get lenght for the to blit it on the scree """
        return len(self.tiles) + 1

class Food:
    """Class about the food element in the Mamba Game. On theory the food object first of all shoud append on random position.
    And if the snake head collides with the food rect - the food object shoud get new (free - not somewhere on the snake body) position. """

    def __init__(self, size, cellsx, cellsy):
        """ Food constructor which takes few arguments the cell size, the amount of cells on the x axis and the amount cells on the y axis"""
        self.size = size
        self.cellsx = cellsx
        self.cellsy = cellsy
        # Get random first position
        self.position = (random.randint(1,  self.cellsx) * self.size - self.size, random.randint(1,  self.cellsy) * self.size - self.size)

    def getpos(self, snakeHead, snakeBody):
        """Method which moves the food object on new position """
        self.position = (random.randint(1,  self.cellsx) * self.size - self.size, random.randint(1,  self.cellsy) * self.size - self.size)

        # For loops which purpose is to check if the new food position it is on any snake element if so it generates new position
        for j in snakeBody:
            if j.colliderect(self.position[0], self.position[1], self.size, self.size) or snakeHead.colliderect(self.position[0], self.position[1], self.size, self.size):
              self.position = (random.randint(1,  self.cellsx) * self.size - self.size, random.randint(1,  self.cellsy) * self.size - self.size)

    def draw(self, display, theme):
        """Method which draws the food object on the display surface object, bliting corespondenting theme food sprite"""
        DISP.blit(theme["foodIMG"], (self.position[0], self.position[1], self.size, self.size))

    def getrect(self):
        """This method returns the food rect - We need it to check if this food rect collides with snake head rect"""      
        return pg.Rect(self.position[0], self.position[1], self.size, self.size)   

def introLoad():
    # Function which loads the itro elements
    # Global scope for this data structures for easy usage in other functions 
    global buttons, introBack

    buttons = {"play": pg.image.load("InterfaceSprites/play.png").convert_alpha(), \
    "playh": pg.image.load("InterfaceSprites/playh.png").convert_alpha(), \
    "theme": pg.image.load("InterfaceSprites/theme.png").convert_alpha(), \
    "themeh": pg.image.load("InterfaceSprites/themeh.png").convert_alpha(), \
    "scores": pg.image.load("InterfaceSprites/scores.png").convert_alpha(), \
    "scoresh": pg.image.load("InterfaceSprites/scoresh.png").convert_alpha(),\
    "about": pg.image.load("InterfaceSprites/about.png").convert_alpha(), \
    "abouth": pg.image.load("InterfaceSprites/abouth.png").convert_alpha(),\
    "back": pg.image.load("InterfaceSprites/back.png").convert_alpha(), \
    "backh": pg.image.load("InterfaceSprites/backh.png").convert_alpha()}
   
   # transofrming the button sprites in wanted scale
    for el in buttons:
        buttons[el] = pg.transform.scale(buttons[el], (250, 100))
    introBack = pg.image.load("InterfaceSprites/introback2.png").convert_alpha()

def inroDraw(DISP, x, y, mKey):
    # Function for drawing the intro elements
    # This func accepts display surface object, the x and y cordinates of the mouse cursor and the mouse key

    # bliting the intro background and the intro buttons
    DISP.blit(introBack, (0, 0))
    DISP.blit(buttons["play"], (370, 200))
    DISP.blit(buttons["theme"], (370, 325))
    DISP.blit(buttons["scores"], (370, 450))
    DISP.blit(buttons["about"], (370, 575))

    # With if elif chain it is done the hover effect with bliting different image on top of the previous image
    # And we handle the user input for clicking on particular button with nested if, returning coresponding values for the button 
    # 0s and 1s are used instead of long tuple with True or False - that just don't look so readable - 
    # remember the 7th Zen of Python rule: "Readability counts."

    if x > 370 and x < 620 and y > 200 and y < 300:
        DISP.blit(buttons["playh"], (370, 200))
        if mKey[0]:
            gameLoad() # Loading the game media and generating new game
            return (0, 1, 0, 0, 0) # This boolean values resond to:  INTRO, GAME, THEME, SCORES, ABOUT
            # so if we click on PLAY button everything expect PLAY is False
    elif x > 370 and x < 620 and y > 325 and y < 425:
        DISP.blit(buttons["themeh"], (370, 325))
        if mKey[0]:
            return (0, 0, 1, 0, 0) 
            #INTRO, GAME, THEME, SCORES, ABOUT
    elif x > 370 and x < 620 and y > 450 and y < 550:
        DISP.blit(buttons["scoresh"], (370, 450))
        if mKey[0]:
            return (0, 0, 0, 1, 0) 
            #INTRO, GAME, THEME, SCORES, ABOUT
    elif x > 370 and x < 620 and y > 575 and y < 675:
        DISP.blit(buttons["abouth"], (370, 575))
        if mKey[0]:
            return (0, 0, 0, 0, 1)
            #INTRO, GAME, THEME, SCORES, ABOUT

    # On defaul the INTRO just stays true
    return (1, 0, 0, 0, 0)  
    #INTRO, GAME, THEME, SCORES, ABOUT

def gameLoad():
    # There is the game loading fuction - it creates instance of the Snake and Food classes
    # If we want loss of progress for example when we hit "Play Again", we call this function again
    # Globaling the variables
    global snake, food, pos

    snake = Snake(LENGHT, 0, 0, CELLSIZE) # 0, 0 respond to starting x and y points of the head
    food = Food(CELLSIZE, tilesx, tilesy)
    pos = "r" # pos is the starting diretion


def gameDraw(pos, event, DISP, snake, food, LENGHT, PAUSE, GAMEOVER, GAME, score):
    # This is the main game function which just calls some methonds on the objects, wait for pause input,
    # blit the lenght of the snake, check for colliding of the snake head rect and food rect, and
    # set GEMEOVER True if the snake is invalid


    global lastStage

    PAUSE = False
    if event.type == KEYDOWN and (event.key == K_p or event.key == K_ESCAPE):
        PAUSE = True
        lastStage = pg.image.save(DISP, "laststage.png")
        # Here I made a little trick which saves the last display stage, because the prevent window element stays where is it
        # because nothing blits on top of him. Thaht's why I include this feature just to overwrite this annyoing prevent
        # window when to user pressed "No".

        # It is slowing the game flow but ... meh.

    pos = snake.move(event, pos)
    DISP.blit(theme["gameBack"], (0, 0))
    l = snake.getlenght()

    # blit the text rect with responding font, colortext, and text Cordinates from the theme dictonary
    textBox = theme["font"].render( "lenght: " + str(l), True, theme["colortext"]) 
    DISP.blit(textBox, theme["textboxCord"])

    # Draw the snake and the food objects
    snake.draw(DISP, theme, pos)
    food.draw(DISP, theme)

    # There is the further usage
    snakeRect = snake.getrect()
    foodRect = food.getrect()
    snakeBody = snake.getbody()

    if snakeRect.colliderect(foodRect):
        # If the snake rect collide with the food rect:

        score += 1 # Score is increasing by one
        # Score is different from LENGHT, because LENGHT it is the snake lenght itself, it can be set in the snake instance from 1 - to infinity
        #  But score must always be zero, because it counts only the collidings with the food (a.k.a scores)
        # It can be done with substracting the start lenght from the final lenght but whatever
        LENGHT += 1
        food.getpos(snakeRect, snakeBody)
        snake.addtile()

    if snake.notValidSnake(X, Y):
        # If the snake is not valid - GAMEOVER
        writingFunc("records", score)
        GAME = False
        GAMEOVER = True
        return (PAUSE, pos, GAMEOVER, GAME, score)

    return (PAUSE, pos, GAMEOVER, GAME, score)


def themeDraw(event, x, y, DISP, mKey, themes, whichTheme, currentTheme, once, count, theme):

    # The theme draw fucntion draw buttons, themes thumbnails and set the current theme

    # Bliting the buttons
    DISP.blit(themeSprites["themeBack"], (0, 0))
    DISP.blit(themeSprites["back"], (10, 10))
    DISP.blit(themeSprites["githubico"], (850, 565))
    DISP.blit(themeSprites["arrowl"], (50, 250))
    DISP.blit(themeSprites["arrowr"], (800, 250))
    DISP.blit(themeSprites["setB"], (370, 475))
    DISP.blit(themes[currentTheme]["themeThumb"], (250, 100))

    count += 1
    if count > 35:
        count = 0
        once = True
    # Here is a little time slowing structure. time.sleep doesn't work, maybe there is another func in the time module
    # or other module but and this workds.

    if x > 10 and x < 135 and y > 10 and y < 60:
        DISP.blit(themeSprites["backh"], (10, 10))
        if mKey[0]: return (theme, count, once, whichTheme, currentTheme, 1, 0)
        # if the back button is pressed - the INTRO bool is set to True
    elif x > 850 and x < 970 and y > 565 and y < 686:
        DISP.blit(themeSprites["githubicoh"], (850, 565)) 
        # There is a hyperlink which leads to the github repo
        if mKey[0]: webbrowser.open("https://github.com/skilldeliver/pygame", new=0, autoraise=True)

    # The other TWO elif statements are for the arrows, they flip throught the list of the themes
    elif x > 50 and x < 200 and y > 250 and y < 350:
        DISP.blit(themeSprites["arrowlh"], (50, 250))
        if mKey[0]:
            if once:         # Here is the waiting structure, because the loop is too fast and is iterating the themes very fast
                once = False
                currentTheme -=1                               
    elif x > 800 and x < 950 and y > 250 and y < 350:
        DISP.blit(themeSprites["arrowrh"], (800, 250))
        if mKey[0]:        # The other application of the waiting structure for the another arrow
            if once:
                once = False
                currentTheme += 1
                
    elif x > 370 and x < 615 and y > 475 and y < 575:
        DISP.blit(themeSprites["setBh"], (370, 475))
        if mKey[0]:
            theme = themes[currentTheme] # If the set button is pressed - the theme is the themes item at currentTheme index

    # If currentTeme index goes out of the list range it assigns index of the the last element or the first element depending on fliping
    if currentTheme < 0: currentTheme = len(themes) -1
    elif currentTheme > len(themes) - 1: currentTheme = 0 

    # If the theme is current theme the set button stays setted
    if theme == themes[currentTheme]: DISP.blit(themeSprites["setBh"], (370, 475))

    return  (theme, count, once, whichTheme, currentTheme, 0, 1)

def writingFunc(fileString, scores):
    # This is the writing function which stores the game info in ordinary text file
    # Very messy and dumb made, but I had no success with the use of "r+" or "w+"

    fileO = open(fileString + ".txt", "r")
    listF = fileO.readline().split()

    # Extracting the scores and the games from the txt file content
    scoresF = listF[0] 
    gamesF = listF[1]
    fileO.close()
    
    fileO = open(fileString + ".txt", "w")
    writeF = []
    if scores > int(scoresF): # if the scores from the game are more than previous scores - it is overwrting
        # and counts another game
        writeF = [str(scores) + " " + str(int(gamesF) + 1)] 
    else:
        # in the else case just write the same value
        writeF = [str(scoresF) + " " + str(int(gamesF) + 1)]
    fileO.writelines(writeF)
    fileO.close()

def pause(event, x, y, PAUSE, DISP, mKey, prevent, fromWhere, ifno):
    # if pause - there are three options - resume, playagain and mainmenu
    # if the last to are pressed - the progress is lost - but there is a prevent win before that

    if ifno: DISP.blit(pg.image.load("laststage.png"), (0, 0))
    if event.type == KEYDOWN and event.key == K_b: prevent = False; PAUSE = 0

    # bliting the buttons
    DISP.blit(pauseBack, (0, 0))
    DISP.blit(resume, (375, 175))
    DISP.blit(playagain, (375, 300))
    DISP.blit(mainmenu, (375, 425))


    if x > 375 and x < 625 and y > 175 and y < 275:
         DISP.blit(resumeh, (375, 175))
         if mKey[0]: 
             # if resume - "PAUSE" is false and the game just continues
             prevent = False
             PAUSE = 0
    elif x > 375 and x < 625 and y > 300 and y < 400:
         DISP.blit(playagainh, (375, 300))
         if mKey[0]:
             # If playgagain is pressed - prevent is true which means prevent win will be displayed
             prevent = True
             fromWhere = "playagain"
             PAUSE = False
             return (0, 0, prevent, PAUSE, fromWhere, ifno)
            #gameLoad(); PAUSE = False
    elif x > 375 and x < 625 and y > 425 and y < 525:
         DISP.blit(mainmenuh, (375, 425))
         if mKey[0]:
             # If mainmenu is pressed - prevent is true which means prevent win will be displayed
             fromWhere = "mainmenu"
             prevent = True
             PAUSE = False
             return (0, 0, prevent, PAUSE, fromWhere, ifno)

    return (0, 1, prevent, PAUSE, fromWhere, ifno)

def preventWinA(DISP, x, y, mKey, fromWhere, prevent, PAUSE, GAME, ifno, score):
    # There is the prevent window func
    # Two options - Yes or No

    # bliting buttons
    DISP.blit(preventWin, (550, 250))
    DISP.blit(yes, (650, 450))
    DISP.blit(no, (825, 450))

    if x > 650 and x < 775 and y > 400 and y < 500: 
        DISP.blit(yesh, (650, 450))
        if mKey[0]: # if yes is pressed
            score = 0
            if fromWhere == "mainmenu": 
                # if it is pressed from main menu button - the game is reset but also the INTRO is True
                gameLoad()
                prevent = False
                PAUSE = False
                return (1, prevent, PAUSE, GAME, ifno, score)
            elif fromWhere == "playagain":
                #if it is pressed from playagain button - the game is reset and the game is still True
                gameLoad()
                prevent = False
                PAUSE = False
                GAME = True
    
    # when no is pressed the PAUSE is True
    if x > 825 and x < 950 and y > 400 and y < 500:
        DISP.blit(noh, (825, 450))
        if mKey[0]:
            ifno = True
            prevent = False
            GAME = True
            PAUSE = True

    return (0, prevent, PAUSE, GAME, ifno, score)

def gameover(event, x, y, DISP, INTRO, GAME, GAMEOVER, mKey, score):
    # Game Over func for displaying the reached scores

    DISP.blit(gameoverIMG, (0, 0))
    DISP.blit(playagain, (100, 300))
    DISP.blit(mainmenu, (650, 300))
    textScores = fontScore.render(str(score), True, (255, 255, 255))
    DISP.blit(textScores, (625, 160))

    if x > 105 and x < 345 and y > 300 and y < 400:
        DISP.blit(playagainh, (100, 300))
        if mKey[0]:
            score = 0
            gameLoad()
            return (0, 1, 0, score)
    elif x > 650 and x < 900 and y > 300 and y < 400:
        DISP.blit(mainmenuh, (650, 300))
        if mKey[0]:
            score = 0
            return (1, 0, 0, score)

    return (0, 0, 1, score)

def scoresDraw(event, x, y, DISP):
    # SCORES section - reads from our complex database :D - .txt file

    fileO = open("records.txt", "r")
    scoresL = fileO.readline().split()

    highestscore = scoresL[0]
    totalgames = scoresL[1]

    textScores = fontArial.render( highestscore, True, (255, 255, 255)) # for the highest scores reached
    textGames = fontArial.render( totalgames, True, (255, 255, 255)) # and for the total games

    # only one button - the back button
    DISP.blit(scoresBack, (0, 0))
    DISP.blit(themeSprites["back"], (10, 10))
    DISP.blit(textScores, (165, 395))
    DISP.blit(textGames, (600, 395))

    if x > 10 and x < 135 and y > 10 and y < 60:
        DISP.blit(themeSprites["backh"], (10, 10))
        if mKey[0]: return (1, 0)
            
    fileO.close()
    return (0, 1)


def about(event, x, y, DISP, mKey):
    # And this is the final section - the about section

    # loading buttons mainly for social media links
    aboutIMG = pg.image.load("InterfaceSprites/aboutfront.png").convert_alpha()
    githubic = pg.image.load("InterfaceSprites/githubicon.png").convert_alpha()
    githubich = pg.image.load("InterfaceSprites/githubiconh.png").convert_alpha()
    fbic = pg.image.load("InterfaceSprites/facebookicon.png").convert_alpha()
    fbich = pg.image.load("InterfaceSprites/facebookiconh.png").convert_alpha()
    twitic = pg.image.load("InterfaceSprites/twittericon.png").convert_alpha()
    twitich = pg.image.load("InterfaceSprites/twittericonh.png").convert_alpha()

    # transforming them in appropriate scale
    githubic = pg.transform.scale(githubic, (100, 100))
    githubich = pg.transform.scale(githubich, (100, 100))
    fbic = pg.transform.scale(fbic, (100, 100))
    fbich = pg.transform.scale(fbich, (100, 100))
    twitic = pg.transform.scale(twitic, (100, 100))
    twitich = pg.transform.scale(twitich, (100, 100))

    # bliting the buttons
    DISP.blit(aboutIMG, (0, 0))
    DISP.blit(themeSprites["back"], (10, 10))
    DISP.blit(githubic, (575, 600))
    DISP.blit(fbic, (695, 600))
    DISP.blit(twitic, (815, 600))


    # hover effect and click input, if the social media buttons are clicked - they lead to responding web page - opening
    # new tab if the broweser if opened or open the default broweser if it is not opened

    if x > 10 and x < 135 and y > 10 and y < 60:
        DISP.blit(themeSprites["backh"], (10, 10))
        if mKey[0]: return (1, 0)
    elif x > 575 and x < 675 and y > 600 and y < 700:
        DISP.blit(githubich, (575, 600))
        if mKey[0]: webbrowser.open("https://github.com/skilldeliver", new=0, autoraise=True)
    elif x > 700 and x < 800 and y > 600 and y < 700:
        DISP.blit(fbich, (695, 600))
        if mKey[0]: webbrowser.open("https://www.facebook.com/skilldeliver", new=0, autoraise=True)
    elif x > 815 and x < 915 and y > 600 and y < 700:
        DISP.blit(twitich, (815, 600))
        if mKey[0]: webbrowser.open("https://twitter.com/vladislavmihov", new=0, autoraise=True)
    return (0, 1)

# This constant variables are not in the if check because they are some of them are used or may be needed in mambathemes module
CELLSIZE = 20
SIZE = X, Y = (1000, 700)
tilesx = X / CELLSIZE
tilesy = Y / CELLSIZE

if __name__ == "__main__":
    # Importing dependencies 
    import pygame as pg
    import sys
    from pygame.locals import *
    import mambathemes
    import random
    import webbrowser 
    

    # Tuple unpacking - boolean values of every section
    # In the begging we start from the INTRO - that is why it is Trur
    INTRO, GAME, THEME, SCORES, ABOUT, PAUSE, GAMEOVER =  (1, 0, 0, 0, 0, 0, 0)
    score = 0 # Score will not be used as a boolean

    # Initing all pygame modules and extra initing of the font module
    pg.init()
    pg.font.init()

    # Instances of the Clock and Surface classes
    CLOCK = pg.time.Clock()
    DISP = pg.display.set_mode(SIZE)
    pg.display.set_caption("Mamba")

    # Starting lenght of the snake
    LENGHT = 3 

    # some fonts
    fontScore = pg.font.SysFont("Arial Black", 72)
    fontArial = pg.font.SysFont("Arial Black", 162)

    LENGHT -= 1 # Aritmetic fix of annoying bug 

    # Very bad and messy loading but I am lazy... :D
    # Sry, love u
    prevent = False
    pauseBack = pg.image.load("InterfaceSprites/pauseBack.png").convert_alpha()
    resume = pg.image.load("InterfaceSprites/resume.png").convert_alpha()
    resumeh = pg.image.load("InterfaceSprites/resumeh.png").convert_alpha()
    resume = pg.transform.scale(resume, (250, 100))
    resumeh = pg.transform.scale(resumeh, (250, 100))
    playagain = pg.image.load("InterfaceSprites/playagain.png").convert_alpha()
    playagainh = pg.image.load("InterfaceSprites/playagainh.png").convert_alpha()
    playagain = pg.transform.scale(playagain, (250, 100))
    playagainh = pg.transform.scale(playagainh, (250, 100))
    mainmenu = pg.image.load("InterfaceSprites/mainmenu.png").convert_alpha()
    mainmenuh = pg.image.load("InterfaceSprites/mainmenuh.png").convert_alpha()
    mainmenu = pg.transform.scale(mainmenu, (250, 100))
    mainmenuh = pg.transform.scale(mainmenuh, (250, 100))
    preventWin = pg.image.load("InterfaceSprites/ask.png").convert_alpha()
    preventWin = pg.transform.scale(preventWin, (500, 350))
    yes = pg.image.load("InterfaceSprites/yes.png").convert_alpha()
    yesh = pg.image.load("InterfaceSprites/yesh.png").convert_alpha()
    no = pg.image.load("InterfaceSprites/no.png").convert_alpha()
    noh = pg.image.load("InterfaceSprites/noh.png").convert_alpha()
    yes = pg.transform.scale(yes, (125, 50))
    yesh = pg.transform.scale(yesh, (125, 50))
    no = pg.transform.scale(no, (125, 50))
    noh = pg.transform.scale(noh, (125, 50))
    fromWhere = " "
    scoresBack = pg.image.load("InterfaceSprites/scoresback.png").convert_alpha()
    ifno = False
    gameoverIMG = pg.image.load("InterfaceSprites/gameover.png").convert_alpha()

    # calling loading functions
    introLoad()
    gameLoad()
    themes, theme, themeSprites = mambathemes.themeLoad()

    # initializing some helping varaibles
    whichTheme = 0
    currentTheme = 0 
    once = 1
    count = 0

    # MAIN GAME LOOP
    while 1:
        
        # Get the x, y and mouse key values
        x, y = pg.mouse.get_pos()
        mKey = pg.mouse.get_pressed()

        # Event handling loop
        # in all cases if the QUIT button is clicked - the game is turning off
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()    

        # SPAGHETTI CODE - I still don't have grasp on the OOP
        # ALL SECTIONS with if - elif chain
        if INTRO: INTRO, GAME, THEME, SCORES, ABOUT = inroDraw(DISP, x, y, mKey)
        elif GAME:
            if not PAUSE:
                PAUSE, pos, GAMEOVER, GAME, score = gameDraw(pos, event, DISP, snake, food, LENGHT, PAUSE,  GAMEOVER, GAME, score)
            elif PAUSE: INTRO, GAME, prevent, PAUSE, fromWhere, ifno = pause(event, x, y, PAUSE, DISP, mKey, prevent, fromWhere, ifno)
        elif prevent: INTRO, prevent, PAUSE, GAME, ifno, score = preventWinA(DISP, x, y, mKey, fromWhere, prevent, PAUSE, GAME, ifno, score)
        elif THEME:
            theme, count, once, whichTheme, currentTheme, INTRO, THEME  = \
            themeDraw(event, x, y, DISP, mKey, themes, whichTheme, currentTheme, once, count, theme)
        elif SCORES: INTRO, SCORES = scoresDraw(event, x, y, DISP)
        elif GAMEOVER: INTRO, GAME, GAMEOVER, score = gameover(event, x, y, DISP, INTRO, GAME, GAMEOVER, mKey, score)
        elif ABOUT: INTRO, ABOUT = about(event, x, y, DISP, mKey)

        # If we are playing the clock is ticking with fifthteen fps, else is faster - sixty
        if GAME:
            CLOCK.tick(15)
        else:
            CLOCK.tick(60)

        # and updating the display
        pg.display.update()