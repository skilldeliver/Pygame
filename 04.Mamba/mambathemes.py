import pygame as pg
import mamba
import random

# yourTheme = {"themeThumb": ,  "snakeElement": , "gameBack": , "snakeHead": {"left": , "right": , "up": , "down": }, \
#             "foodIMG": ,"font": , "colortext": , "textboxCord":}


def themeLoad():
    themes = []

    languagesForEating = [pg.image.load("ThemeSprites/PysnakeSprites/68747470733a2f2f646576656c6f7065722e6665646f726170726f6a6563742e6f72672f7374617469632f6c6f676f2f6373686172702e706e67.png").convert_alpha(), \
    pg.image.load("ThemeSprites/PysnakeSprites/2000px-Ruby_logo.svg.png").convert_alpha(), \
    pg.image.load("ThemeSprites/PysnakeSprites/cpp_logo.png").convert_alpha(), \
    pg.image.load("ThemeSprites/PysnakeSprites/JavaScript-logo.png").convert_alpha(), \
    pg.image.load("ThemeSprites/PysnakeSprites/swift-og.png").convert_alpha()]

    pythonTheme = {"themeThumb": pg.image.load("ThemeSprites/PysnakeSprites/pythumb.png").convert_alpha(), \
    "snakeElement": pg.image.load("ThemeSprites/PysnakeSprites/pyel.png").convert_alpha(), \
    "gameBack": pg.image.load("ThemeSprites/PysnakeSprites/pyback.png").convert_alpha(), \
    "snakeHead": {"left": pg.image.load("ThemeSprites/PysnakeSprites/pyl.png").convert_alpha(), \
    "right": pg.image.load("ThemeSprites/PysnakeSprites/pyr.png").convert_alpha(), \
    "up": pg.image.load("ThemeSprites/PysnakeSprites/pyu.png").convert_alpha(), \
    "down":pg.image.load("ThemeSprites/PysnakeSprites/pyd.png").convert_alpha()}, \
    "foodIMG": languagesForEating[random.randint(0, len(languagesForEating) - 1)], \
    "font": pg.font.SysFont("Helvetica", 24), "colortext": (255, 237, 71), "textboxCord": (865, 0) }

    pythonTheme["snakeElement"] = pg.transform.scale(pythonTheme["snakeElement"], (mamba.CELLSIZE + 5, mamba.CELLSIZE + 5))
    for el in pythonTheme["snakeHead"]:
       pythonTheme["snakeHead"][el] = pg.transform.scale(pythonTheme["snakeHead"][el], (mamba.CELLSIZE + 5, mamba.CELLSIZE + 5))    
    pythonTheme["foodIMG"] = pg.transform.scale(pythonTheme["foodIMG"], (mamba.CELLSIZE + 5, mamba.CELLSIZE + 5))

    themes.append(pythonTheme)

    moonTheme = {"themeThumb": pg.image.load("ThemeSprites/MoonterSprites/moonter.png").convert_alpha(), \
    "snakeElement": pg.image.load("ThemeSprites/MoonterSprites/PNGPIX-COM-Moon-PNG-Transparent-Image-500x489.png").convert_alpha(), \
    "gameBack": pg.image.load("ThemeSprites/MoonterSprites/Stars-wallpapers-HD-backgrounds-download.jpg").convert_alpha(), \
    "snakeHead": {"left": pg.image.load("ThemeSprites/MoonterSprites/snakeheadl.png").convert_alpha(), \
    "right": pg.image.load("ThemeSprites/MoonterSprites/snakeheadr.png").convert_alpha(), \
    "up": pg.image.load("ThemeSprites/MoonterSprites/snakeheadu.png").convert_alpha(), \
    "down":pg.image.load("ThemeSprites/MoonterSprites/snakeheadd.png").convert_alpha()}, \
    "foodIMG": pg.image.load("ThemeSprites/MoonterSprites/asteroid_stock_by_fimar-d64qnwa.png").convert_alpha(), \
    "font": pg.font.SysFont("Baskerville", 34), "colortext": (255, 255, 255),\
    "textboxCord": (865, 0)}

    moonTheme["snakeElement"] = pg.transform.scale(moonTheme["snakeElement"], (mamba.CELLSIZE + 5, mamba.CELLSIZE + 5))
    for el in moonTheme["snakeHead"]:
       moonTheme["snakeHead"][el] = pg.transform.scale(moonTheme["snakeHead"][el], (mamba.CELLSIZE + 5, mamba.CELLSIZE + 5))
    moonTheme["foodIMG"] = pg.transform.scale(moonTheme["foodIMG"], (mamba.CELLSIZE + 5, mamba.CELLSIZE + 5))

    themes.append(moonTheme)

    minecraftTheme = {"themeThumb": pg.image.load("ThemeSprites/StonieSprites/stoniethumb.png").convert_alpha(),  \
    "snakeElement": pg.image.load("ThemeSprites/StonieSprites/639ee336abefc1a6a1f40b97db9b409f.jpg").convert_alpha(), \
                 "gameBack": pg.image.load("ThemeSprites/StonieSprites/minecraftback.png").convert_alpha(), \
                 "snakeHead": {"left": pg.image.load("ThemeSprites/StonieSprites/msl.png").convert_alpha(), \
                 "right": pg.image.load("ThemeSprites/StonieSprites/msr.png").convert_alpha(), \
                 "up": pg.image.load("ThemeSprites/StonieSprites/msu.png").convert_alpha(), \
                 "down":pg.image.load("ThemeSprites/StonieSprites/msd.png").convert_alpha()}, \
                 "foodIMG": pg.image.load("ThemeSprites/StonieSprites/gold-block-big.png").convert_alpha(), 
                 "font": pg.font.SysFont("Franklin Gothic", 28, True), \
                 "colortext": (255, 0, 0), "textboxCord": (865, 0)}

    minecraftTheme["snakeElement"] = pg.transform.scale(minecraftTheme["snakeElement"], (mamba.CELLSIZE, mamba.CELLSIZE))
    for el in minecraftTheme["snakeHead"]:
       minecraftTheme["snakeHead"][el] = pg.transform.scale(minecraftTheme["snakeHead"][el], (mamba.CELLSIZE + 5, mamba.CELLSIZE + 5))
    minecraftTheme["foodIMG"] = pg.transform.scale(minecraftTheme["foodIMG"], (mamba.CELLSIZE, mamba.CELLSIZE))

    themes.append(minecraftTheme)

    theme = pythonTheme   
    themeSprites = {"themeBack" : pg.image.load("InterfaceSprites/themeback.png").convert_alpha(), \
     "back" : pg.image.load("InterfaceSprites/back.png").convert_alpha(), \
     "backh" : pg.image.load("InterfaceSprites/backh.png").convert_alpha(), \
     "backh" : pg.image.load("InterfaceSprites/backh.png").convert_alpha(),\
     "githubico" : pg.image.load("InterfaceSprites/githubicon.png").convert_alpha(),\
     "githubicoh" : pg.image.load("InterfaceSprites/githubiconh.png").convert_alpha(),\
     "arrowl" : pg.image.load("InterfaceSprites/arrowl.png").convert_alpha(), \
     "arrowlh" : pg.image.load("InterfaceSprites/arrowlh.png").convert_alpha(), \
     "arrowr" : pg.image.load("InterfaceSprites/arrowr.png").convert_alpha(), \
     "arrowrh" : pg.image.load("InterfaceSprites/arrowrh.png").convert_alpha(), \
     "setB" : pg.image.load("InterfaceSprites/set.png").convert_alpha(), \
     "setBh" : pg.image.load("InterfaceSprites/seth.png").convert_alpha()}

    themeSprites["back"] = pg.transform.scale(themeSprites["back"], (125, 50))
    themeSprites["backh"] = pg.transform.scale(themeSprites["backh"], (125, 50))  
    themeSprites["githubico"] = pg.transform.scale(themeSprites["githubico"], (125, 125))
    themeSprites["githubicoh"] = pg.transform.scale(themeSprites["githubicoh"], (125, 125))
    themeSprites["arrowl"] = pg.transform.scale(themeSprites["arrowl"], (150, 100))
    themeSprites["arrowlh"] = pg.transform.scale(themeSprites["arrowlh"], (150, 100))
    themeSprites["arrowr"] = pg.transform.scale(themeSprites["arrowr"], (150, 100))
    themeSprites["arrowrh"] = pg.transform.scale(themeSprites["arrowrh"], (150, 100))
    themeSprites["setB"] = pg.transform.scale(themeSprites["setB"], (250, 100))
    themeSprites["setBh"] = pg.transform.scale(themeSprites["setBh"], (250, 100))

    return themes, theme, themeSprites