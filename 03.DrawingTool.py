import pygame as p, random, time, sys                                              
from pygame.locals import *

p.init()

SIZE = X, Y = (1000, 700)
DISPLAY = p.display.set_mode(SIZE)
p.display.set_caption("Drawing Tool")
CLOCK = p.time.Clock()

MENU = True
DRAW = False
ABOUT = False
COLORPALLETE = False
COLORCANVAS = False
ARTWORK = False

#                                              MENU VARIABLES
menuImg = p.image.load("menuskilldeliver.png")
played = [1, 1, 1, 1, 1]

menuButtons = { "draw": p.image.load("drawbutton.png"), "drawhover": p.image.load("drawbutton-hover.png"), \
               "colorcanvas": p.image.load("colorcanvas.png"), "colorcanvashover": p.image.load("colorcanvashover.png"), \
               "colorpalette": p.image.load("colorpalettebutton.png"), "colorpalettehover": p.image.load("colorpalettebuttonhover.png"),
               "artwork": p.image.load("myartworksbutton.png"), "artworkhover": p.image.load("myartworksbuttonhover.png"),
              "about": p.image.load("aboutbutton.png"), "abouthover": p.image.load("aboutbuttonhover.png")}

#                                             MENU FUNCTIONS

def handleEventsMenu(x, y, section, event):
    DRAW = 0
    ABOUT = 0
    COLORPALLETE = 0
    COLORCANVAS = 0
    ARTWORK = 0

    if section and event.type == MOUSEBUTTONDOWN and x > 351 and x < 623 and y > 290 and y < 385: section = False; DRAW = True
    if section and event.type == MOUSEBUTTONDOWN and x > 351 and x < 623 and y > 582 and y < 677: section = False; ABOUT = True
    if section and event.type == MOUSEBUTTONDOWN and x > 751 and x < 997 and y > 290 and y < 385: section = False; COLORPALLETE = True
    if section and event.type == MOUSEBUTTONDOWN and x > 0 and x < 248 and y > 290 and y < 385: section = False; COLORCANVAS = True
    if section and event.type == MOUSEBUTTONDOWN and x > 351 and x < 623 and y > 21 and y < 115: section = False; ARTWORK = True

    return section, DRAW, ABOUT, COLORPALLETE, COLORCANVAS, ARTWORK

def blitMenuButtons(x, y, section, surf, image, buttons, sound1, sound2, listplay):
    if section:
        surf.blit(image, (0, 0))
        if  (x > 351 and x < 623 and y > 21 and y < 115):     
            surf.blit(buttons["artworkhover"], (375, 20))
            if listplay[0]: sound1.play()
            listplay[0] = 0
        else:
            listplay[0] = 1
            surf.blit(buttons["artwork"], (375, 20))

        if  x > 351 and x < 623 and y > 290 and y < 385:
            surf.blit(buttons["drawhover"], (375, 290))
            if listplay[1]: sound2.play()
            listplay[1]= 0
        else:
            listplay[1]= 1
            surf.blit(buttons["draw"], (375, 290))
        
        if  x > 351 and x < 623 and y > 582 and y < 677:
            surf.blit(buttons["abouthover"], (375, 580))
            if listplay[2]: sound2.play()
            listplay[2]= 0
        else: 
            listplay[2]= 1
            surf.blit(buttons["about"], (375, 580))

        if  x > 0 and x < 248 and y > 290 and y < 385:
            surf.blit(buttons["colorcanvashover"], (0, 290))
            if listplay[3]: sound2.play()
            listplay[3]= 0
        else:
            listplay[3]= 1
            surf.blit(buttons["colorcanvas"], (0, 290))

        if  x > 751 and x < 997 and y > 290 and y < 385:
            surf.blit(buttons["colorpalettehover"], (750, 290))
            if listplay[4]: sound2.play()
            listplay[4]= 0
        else:
            listplay[4]= 1
            surf.blit(menuButtons["colorpalette"], (750, 290))

        return listplay
#                                             ARTWORK VARIABLES
drawings = []
for i in range(1, 9):
    drawings.append(p.image.load("drawing" + str(i) + ".png"))

#                                             COLOR PALLETE DATA

n = 0
once = True
COLORPALLETES = [[(255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 65, 255), (255, 255, 0),    \
                  (255, 132, 0), (128, 0, 255), (76, 49, 16),(0, 100, 0), (0, 0, 100), (255, 130, 211)], \
                 [(255,255,255), (0, 0, 0), (225,247,213), (255,189,189), (201,201,255),  (241,203,255), \
                  (255,238,173), (255,111,105), (150,206,180), (255,204,92), (136,216,176), (75,56,50)], \
                 [(255, 255, 255), (0, 0, 0), (1,31,75), (3,57,108), (0,91,150), (100,151,177), \
                  (179,205,224),(179,236,236), 	(137,236,218), (67,232,216), (64,224,208), (59,214,198)], \
                 [(255, 255, 255), (0, 0, 0),(55,56,84), (73,50,103), (158,55,159), (232,106,240), \
                  (123,179,255), 	(110,127,128),	(83,104,114), (112,128,144), (83,104,120), (54,69,79)], \
                 [(255, 255, 255), (0, 0, 0), (102,101,71), (251,46,1), (111,203,159), (255,226,138), \
                  (255,254,179), 	(255,78,80), (252,145,58), (249,214,46), (234,227,116), (226,244,199)]]
    
nextsetButtons = [p.image.load("next.png"), p.image.load("nexthover.png"), p.image.load("set.png"), p.image.load("sethover.png")]


index = 1
colorPalleteBack = p.image.load("color1.png")

#                                            COLOR PALLETE FUNCTIONS

def generateColorRects(colorlist):
    rectsList = []
    rectsList2 = []
    dist = 0
    for i in range(12):
        dist += 80
        rectsList.append(p.Rect(-60 + dist, 270, 70, 70))
        rectsList2.append(p.Rect(-60 + dist + 5, 270 + 5, 60, 60))
    return rectsList, rectsList2


#                                             COLOR CANVAS VARIABLES:
colorOfCanvas = ()
colorcanvasBack = p.image.load("backgroundmay2.png")

#                                             ABOUT VARIABLES
backandfront = {"back": p.image.load("backgroundmay.png"), "front": p.image.load("backgroundabout.png")}
moveY = 750
stage2 = False
float1 = True
float2 = False

#                                             DRAWING FUNCTIONS
def randomName():
    letters = "q w e r t y u i o p a s d f g h j k l z x c v b n m 1 2 3 4 5 6 7 8 9 0".split()
    name = ""
    for i in range(12):
        name += letters[random.randint(0, 35)]
    return name + ".png"

def transform(dict, scaleX, scaleY):
    for i in dict:
        dict[i] = p.transform.scale(dict[i], (scaleX, scaleY))
    return dict

def handleEvents(x, y, surf, canvas, event, section1, section2):
    if e.type == QUIT: raise SystemExit
    if e.type == MOUSEBUTTONDOWN:
        if x > 120 and x < 215 and y > 0 and y < 49: surf.blit(canvas, (89, 67))
        if x > 228 and x < 324 and y > 0 and y < 49: p.image.save(surf, randomName())
        if x > 10 and x < 107 and y > 0 and y < 49: section1 = False; section2 = True

    return section1, section2, [1, 1, 1, 1, 1] 

def generateColorBrushRects():
    howmany = 12
    colorRects = []
    hoveredRects = []
    brushSizes = []
    for i in range(3):
        dist = 0
        if i == 2: howmany = 9
        for k in range(howmany):
            if i == 0:
                dist += 15 + 40
                colorRects.append(p.Rect(280 + dist, 0, 40, 40))
            elif i == 1:
                dist += 15 + 40
                hoveredRects.append(p.Rect(280 + dist + 2, 0 + 2, 35, 35))
            else:
                dist += 15 + 40
                brushSizes.append(p.Rect(10, 150 + dist, 40, 40))
    return colorRects, hoveredRects, brushSizes

def getblitBrushColor(x, y, key, surf, color, index, colorslist, rectlist, rectlist2):
    for j in range(12):
        sumC = 0
        colorBorder = ()
        for k in colorslist[j]:
           sumC += k
           if sumC > 150 * 3: colorBorder = (0, 0, 0)
           else: colorBorder = (255, 255, 255)

        if x > rectlist[j].left and x < rectlist[j].right and y > rectlist[j].top and y < rectlist[j].bottom:
            #if i % 2 != 0: p.draw.rect(SURF, (255, 255, 255), colorRects[i])
            p.draw.rect(surf, colorBorder, rectlist[j])           
            p.draw.rect(surf, colorslist[j], rectlist2[j])
        elif j == index:
            p.draw.rect(surf, colorBorder, rectlist[j])           
            p.draw.rect(surf, colorslist[j], rectlist2[j])
        else:
            p.draw.rect(surf, colorslist[j], rectlist[j])
            
        if x > colorRects[j].left and x < colorRects[j].right and y > colorRects[j].top and y < colorRects[j].bottom and key: index = j; color = colorslist[j]
        color = color
    return index, color

def getBrushMode(x, y, key):
    booleans = ()
    if x > 10  and x < 50 and y > 62 and y < 100 and key: booleans = (1, 0, 0)
    elif x > 10 and x < 50 and y > 110 and y < 150 and key: booleans = (0, 1, 0)
    elif x > 10 and x < 50 and y > 160 and y < 200 and key: booleans = (0, 0, 1)

    return booleans

def blitBrushMode(x, y, surf, dict, mode1, mode2, mode3):
    if x > 10  and x < 50 and y > 62 and y < 100:
        surf.blit(dict["circlehover"], (10, 60))
    else: surf.blit(dict["circle"], (10, 60))
    if mode1: surf.blit(dict["circlehover"], (10, 60))

    if x > 10 and x < 50 and y > 110 and y < 150:
        surf.blit(dict["recthover"], (10, 110))
    else: surf.blit(dict["rect"], (10, 110))
    if mode2: surf.blit(dict["recthover"], (10, 110))

    if x > 10 and x < 50 and y > 160 and y < 200:
        surf.blit(dict["linehover"], (10, 160))
    else:         
        surf.blit(dict["line"], (10, 160))
    if mode3: DISPLAY.blit(dict["linehover"], (10, 160))
    
def getblitBrushSize(x, y, key, surf, list, index, size):
    for i in range(9):
        p.draw.rect(surf, (255, 255, 255), list[i])
        if x > list[i].left and x < list[i].right and y > list[i].top and y < list[i].bottom:
            p.draw.circle(surf, (255, 0, 0), (list[i].left + 20, list[i].top + 20), i + 2 * 2)
        elif i == index: p.draw.circle(surf, (255, 0, 0), (list[i].left + 20, list[i].top + 20), i + 2 * 2)
        else: p.draw.circle(surf, (0, 0, 0), (list[i].left + 20, list[i].top + 20), i + 2 * 2)

        if x > list[i].left and x < list[i].right and y > list[i].top and y < list[i].bottom and key:
           index = i
           size = i * 2
    return index, size


def blitMainButtons(x, y, surf, dict):
    if x > 10 and x < 107 and y > 0 and y < 49:
        surf.blit(dict["button1hover"], (10, 0))
    else:
        surf.blit(dict["button1"], (10, 0))

    if x > 120 and x < 215 and y > 0 and y < 49:
        surf.blit(dict["button2hover"], (120, 0))
    else:
        surf.blit(dict["button2"], (120, 0))

    if x > 228 and x < 324 and y > 0 and y < 49:
        surf.blit(dict["button3hover"], (228, 0))
    else:
        surf.blit(dict["button3"], (228, 0))

def draw(x, y, key, surf, size, color, mode1, mode2, mode3):
    if x > 87 + size and x < 965 - size and y > 65 + size and y < 665 - size and key:
        if mode1: p.draw.circle(surf, color, (x, y), size)
        elif mode2: p.draw.rect(surf, color, (x, y, size, size))
        elif mode3: p.draw.line(surf, color, (x, y), (x - size, y - size), 4)



buttons = transform({"button1": p.image.load("button1.png"), "button1hover": p.image.load("button1-hover.png"), \
                     "button2": p.image.load("button2.png"), "button2hover": p.image.load("button2-hover.png"), \
                     "button3": p.image.load("button3.png"), "button3hover": p.image.load("button3-hover.png")}, 100, 50)

brushes = transform({"circle": p.image.load("circle.png"), "circlehover": p.image.load("circle-hover.png"), \
                     "rect":  p.image.load("rect.png"), "recthover":  p.image.load("rect-hover.png"), \
                     "line":  p.image.load("line.png"), "linehover":  p.image.load("line-hover.png")}, 40, 40)

backgroundIMG = p.image.load("surface3.png")
CANVAS = p.Surface((880, 606))
canvas2 = p.Surface((440, 303))

colorOfCanvas = (255, 255, 255)
currentColors = COLORPALLETES[0]
DISPLAY.blit(backgroundIMG, (0, 0))
CANVAS.fill(currentColors[0])
canvas2.fill(currentColors[0])
DISPLAY.blit(CANVAS, (89, 67))

colorBrush = (0, 0, 0)
sizeBrush = 2
whichSize = 1
whichColor = 1

circleMode = 1
rectMode =   0 
lineMode =   0

colorRects, hoveredRects, brushSizes = generateColorBrushRects()


artworkSound = p.mixer.Sound("Clearing Throat Male-SoundBible.com-37691700.ogg")
hoverSound =  p.mixer.Sound("Tiny Button Push-SoundBible.com-513260752.ogg")


rectsList = []

count = 0
timeA = 0
slice = 0

while 1:
    x, y = p.mouse.get_pos()
    mouseKey = p.mouse.get_pressed()
    for e in p.event.get():
        if e.type == QUIT: p.quit(); sys.exit()

    if MENU:
        blitOnce = True
        MENU, DRAW, ABOUT, COLORPALLETE, COLORCANVAS, ARTWORK = handleEventsMenu(x, y, MENU, e)
        played = blitMenuButtons(x, y, MENU, DISPLAY, menuImg, menuButtons, artworkSound, hoverSound, played)
    #wrapDrawing(x, y, DRAW, DISPLAY, CANVAS, e, mouseKey, brushes, circeMode, rectMode, lineMode, buttons, sizeBrush, colorBrush, circleMode, brushSizes, whichSize)
    if DRAW:
        if blitOnce: DISPLAY.blit(backgroundIMG, (0, 0)); CANVAS.fill(colorOfCanvas); DISPLAY.blit(CANVAS, (89, 67)); blitOnce = False
        DRAW, MENU, played = handleEvents(x, y, DISPLAY, CANVAS, e, DRAW, MENU)
        whichColor, colorBrush = getblitBrushColor(x, y, mouseKey[0], DISPLAY, colorBrush, whichColor, currentColors, colorRects,        hoveredRects)
        whichSize, sizeBrush   = getblitBrushSize(x, y, mouseKey[0], DISPLAY, brushSizes, whichSize, sizeBrush)
        
        if len(getBrushMode(x, y, mouseKey[0])) > 2: circleMode, rectMode, lineMode = getBrushMode(x, y, mouseKey[0])
        blitBrushMode(x, y, DISPLAY, brushes, circleMode, rectMode, lineMode)
        blitMainButtons(x, y, DISPLAY, buttons)
        draw(x, y, mouseKey[0], DISPLAY, sizeBrush, colorBrush, circleMode, rectMode, lineMode)

    if ABOUT:
        if e.type == MOUSEBUTTONDOWN and x > 10 and x < 107 and y > 0 and y < 49: ABOUT = False; MENU = True; played = [1, 1, 1, 1, 1]
        if moveY > 0 and (not stage2): moveY -= 5
        if moveY == 0: stage2 = True
        if stage2:
            if float1: time.sleep(0.05); moveY += 1;
            if float2: time.sleep(0.05); moveY -= 1;
            if moveY > 20:
                float1 = False; float2 = True
            if moveY < -30:
                float1 = True; float2 = False
     
        DISPLAY.blit(backandfront["back"], (0, 0))
        DISPLAY.blit(backandfront["front"], (0, moveY))
        if x > 10 and x < 107 and y > 0 and y < 49:
            DISPLAY.blit(buttons["button1hover"], (10, 0))
        else:
            DISPLAY.blit(buttons["button1"], (10, 0))

    if COLORPALLETE:
        rectsList, rectsList2 = generateColorRects(COLORPALLETES[0])
        DISPLAY.blit(colorPalleteBack, (0, 0))
        for j in range(12):
            if x > rectsList[j].left and x < rectsList[j].right and y > rectsList[j].top and y < rectsList[j].bottom and mouseKey[0]: index = j
            sumC = 0
            colorBorder = ()
            for k in COLORPALLETES[n][j]:
               sumC += k
               if sumC > 150 * 3: colorBorder = (0, 0, 0)
               else: colorBorder = (255, 255, 255)
            
            if x > rectsList[j].left and x < rectsList[j].right and y > rectsList[j].top and y < rectsList[j].bottom:
                p.draw.rect(DISPLAY, colorBorder, rectsList[j])           
                p.draw.rect(DISPLAY, COLORPALLETES[n][j], rectsList2[j])
            elif j == index:
                p.draw.rect(DISPLAY, colorBorder, rectsList[j])           
                p.draw.rect(DISPLAY, COLORPALLETES[n][j], rectsList2[j])
            else:
                p.draw.rect(DISPLAY, COLORPALLETES[n][j], rectsList[j])

        if x > 250 and x < 750 and y > 400 and y < 500:
            DISPLAY.blit(nextsetButtons[1], (250, 400))
        else:
            DISPLAY.blit(nextsetButtons[0], (250, 400))
            
        if x > 400 and x < 600 and y > 550 and y < 650:
            DISPLAY.blit(nextsetButtons[3], (400, 550))
        else:
            DISPLAY.blit(nextsetButtons[2], (400, 550))

        if e.type == MOUSEBUTTONDOWN and x > 10 and x < 107 and y > 0 and y < 49: COLORPALLETE = False; MENU = True; played = [1, 1, 1, 1, 1]
        if x > 10 and x < 107 and y > 0 and y < 49:
            DISPLAY.blit(buttons["button1hover"], (10, 0))
        else:
            DISPLAY.blit(buttons["button1"], (10, 0))

        count += 1
        if count > 35:
           once = True
           count = 0
        if x > 250 and x < 750 and y > 400 and y < 500 and e.type == MOUSEBUTTONDOWN:            
            if once: n += 1; once = False
        if n > 4: n = 0
        if x > 400 and x < 600 and y > 550 and y < 650 and e.type == MOUSEBUTTONDOWN:        
            currentColors = COLORPALLETES[n]

    if COLORCANVAS:
        DISPLAY.blit(colorcanvasBack, (0, 0))
        canvas2.fill(colorOfCanvas)
        DISPLAY.blit(canvas2, (300, 150))
        rectsListCan1, rectsListCan2 = [], []
        dist = 0
        for k in range(12):     
            dist += 10 + 70
            rectsListCan1.append(p.Rect(-60 + dist, 600, 70, 70))
            rectsListCan2.append(p.Rect(-60 + dist + 5, 600 + 5, 60, 60))
            sumC = 0
            if x > rectsListCan1[k].left and x < rectsListCan1[k].right and y > rectsListCan1[k].top and y < rectsListCan1[k].bottom and mouseKey[0]: index = k
            for l in COLORPALLETES[n][k]:
               sumC += l
               if sumC > 150 * 3: colorBorder = (0, 0, 0)
               else: colorBorder = (255, 255, 255)
            
            if x > rectsListCan1[k].left and x < rectsListCan1[k].right and y > rectsListCan1[k].top and y < rectsListCan1[k].bottom:
                p.draw.rect(DISPLAY, colorBorder, rectsListCan1[k])           
                p.draw.rect(DISPLAY, COLORPALLETES[n][k], rectsListCan2[k])
            elif k == index:
                p.draw.rect(DISPLAY, colorBorder, rectsListCan1[k])           
                p.draw.rect(DISPLAY, COLORPALLETES[n][k], rectsListCan2[k])
            else:
                p.draw.rect(DISPLAY, COLORPALLETES[n][k], rectsListCan1[k])

            if x > 300 and x < 740 and y > 147 and y < 450 and e.type == MOUSEBUTTONDOWN:
                colorOfCanvas = COLORPALLETES[n][index]
        if e.type == MOUSEBUTTONDOWN and x > 10 and x < 107 and y > 0 and y < 49: COLORCANVAS = False; MENU = True; played = [1, 1, 1, 1, 1]
        if x > 10 and x < 107 and y > 0 and y < 49:
            DISPLAY.blit(buttons["button1hover"], (10, 0))
        else:
            DISPLAY.blit(buttons["button1"], (10, 0))

    if ARTWORK:
        timeA += 1
        if timeA > 300:
            slice += 1
            timeA = 0
        if slice > 7:
            slice = 0
        DISPLAY.blit(drawings[slice], (0, 0))

        
        if e.type == MOUSEBUTTONDOWN and x > 10 and x < 107 and y > 0 and y < 49: ARTWORK = False; MENU = True; played = [1, 1, 1, 1, 1]
        if x > 10 and x < 107 and y > 0 and y < 49:
            DISPLAY.blit(buttons["button1hover"], (10, 0))
        else:
            DISPLAY.blit(buttons["button1"], (10, 0))
           
    p.display.update()