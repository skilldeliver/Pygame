# UPDATED SOURCES:
#http://img4.wikia.nocookie.net/__cb20130108125226/clubpenguin/images/thumb/5/58/Beta_Team_Solar_System_Space_Shuttle.png/500px-Beta_Team_Solar_System_Space_Shuttle.png       
#https://i.imgur.com/ynZ4O3p.png
#http://www.valentinalisch.de/raffi/freisteller/explode.png
#https://www.freesoundeffects.com/free-sounds/explosion-10070/
#https://vignette.wikia.nocookie.net/scribblenauts/images/0/0e/Asteroid.png/revision/latest/scale-to-width-down/631?cb=20130408211137
#https://www.youtube.com/watch?v=OnoNITE-CLc
#https://www.youtube.com/watch?v=cYMCLz5PQVw

# I am Vladislav Mihov
# Follow me on twitter: @vladislavmihov
# My YouTube Channel: Skilldeliver

import pygame
import sys
import random
from pygame.locals import *
import locale

pygame.init()
locale.setlocale(locale.LC_ALL, '')
SIZE = X, Y = (600, 750)
FPS = 60
CLOCK = pygame.time.Clock()
SURF = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Spaceship")
explosionAnimation = False

def intro():
	button1 = pygame.image.load("Screenshot (291).png")
	button2 = pygame.image.load("Screenshot (292).png")
	button3 = pygame.image.load("Screenshot (293).png")
	button4 = pygame.image.load("Screenshot (294).png")
	
	button1 = pygame.transform.scale(button1,(320, 100))
	button2 = pygame.transform.scale(button2, (260, 70))
	button3 = pygame.transform.scale(button3, (260, 70))
	button4 = pygame.transform.scale(button4, (260, 70))
	
	button1hover = pygame.image.load("button1.png")
	button2hover = pygame.image.load("button2.png")
	button3hover = pygame.image.load("button3.png")
	button4hover = pygame.image.load("button4.png")
	
	button1hover = pygame.transform.scale(button1hover,(320, 100))
	button2hover = pygame.transform.scale(button2hover, (260, 70))
	button3hover = pygame.transform.scale(button3hover, (260, 70))
	button4hover = pygame.transform.scale(button4hover, (260, 70))
	
	introIMG = pygame.image.load("gameintro.png")
	introIMG = pygame.transform.scale(introIMG, SIZE)
	introBool = True
	
	
	while introBool:
		x, y = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == MOUSEBUTTONDOWN and x >= 130 and x <= 448 and y >= 150 and y <= 250:
				introBool = False
				GAMELOOP()
			if event.type == MOUSEBUTTONDOWN and x >= 285  and x <= 545  and y >= 483 and y <= 558:
				introBool = False
				controls()
			if event.type == MOUSEBUTTONDOWN and x >= 286 and x <= 542 and y >= 572 and y <= 639:
				introBool = False
				highscores()
			if event.type == MOUSEBUTTONDOWN and x >= 286 and x <= 544 and y >= 650 and y <= 719:
				introBool = False
				about()

		SURF.blit(introIMG, (0, 0))
		if x >= 130 and x <= 448 and y >= 150 and y <= 250:
			SURF.blit(button1hover, (130, 150))
		else:
			SURF.blit(button1, (130, 150))
	
		if x >= 285  and x <= 545  and y >= 483 and y <= 558:
			SURF.blit(button3hover, (285, 490))
		else:
			SURF.blit(button2, (285, 490))
	
		if x >= 286 and x <= 542 and y >= 572 and y <= 639:
			SURF.blit(button2hover, (285, 490 + 70 + 10))
		else:
			SURF.blit(button3, (285, 490 + 70 + 10))
			
		if x >= 286 and x <= 544 and y >= 650 and y <= 719:
			SURF.blit(button4hover, (285, 490 + 140 + 20))
		else:
			SURF.blit(button4, (285, 490 + 140 + 20))
			
	
		CLOCK.tick(FPS)
		pygame.display.update()

def controls():
	controlsIMG = pygame.image.load("Screenshot (301).png")
	controlsIMG = pygame.transform.scale(controlsIMG, SIZE)
	controlsBool = True
	while controlsBool:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					controlsBool = False
					introBool = True
					intro()
		SURF.blit(controlsIMG, (0, 0))
		CLOCK.tick(60)
		pygame.display.update()

def highscores():
	filetxt = open("recordlist.txt", "r")
	highestlv = 0
	countGames = 0
	for i in filetxt.readlines():
		countGames += 1
		if int(i) > int(highestlv):
			highestlv = int(i)

	filetxt.close()
	font3 = pygame.font.SysFont("Arial Black", 105)
	highestlvTxt = font3.render(str(highestlv), True, (255, 255, 255))
	countGamesTxt = font3.render(str(countGames), True, (255, 255, 255))

	highscoresIMG = pygame.image.load("Screenshot (304).png")
	highscoresIMG = pygame.transform.scale(highscoresIMG, SIZE)
	highscoresBool = True
	while highscoresBool:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					highscoresBool = False
					introBool = True
					intro()
				if event.key == K_m:
					if musicPlaying:
						pygame.mixer.music.stop()
					else:
						pygame.mixer.music.play(-1, 0.0)
					musicPlaying = not musicPlaying





		SURF.blit(highscoresIMG, (0, 0))
		SURF.blit(highestlvTxt, (int(X / 2) - 25, 150))
		SURF.blit(countGamesTxt, (int(X / 2) - 60, 500))
		CLOCK.tick(60)
		pygame.display.update()

def about():
	aboutIMG = pygame.image.load("Screenshot (308).png")
	aboutIMG = pygame.transform.scale(aboutIMG, SIZE)
	aboutBool = True
	while aboutBool:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					about = False
					introBool = True
					intro()
		SURF.blit(aboutIMG, (0, 0))
		CLOCK.tick(60)
		pygame.display.update()

def GAMELOOP():
	j = 0
	
	LEVEL1 = True
	
	GAME = True
	
	exX = 100
	exY = 100
	
	left = False
	right = False
	top = False
	down = False
	
	SHUTTLESPEED = 7
	SATELITESPEED = 4
	
	append1 = True
	append2 = True
	append3 = True
	append4 = True
	append5 = True

	blitingObstacles = True; musicPlaying = True
	pygame.mixer.music.load("shuttle.ogg") 
	pygame.mixer.music.play(-1, 0.0)
	boost = pygame.mixer.Sound("shuttleboodt.ogg")
	
	font = pygame.font.SysFont("Arial Black", 30)
	cloudRects= []
	
	stars1 = pygame.image.load("SpaceStars1.png")
	stars2 = pygame.image.load("SpaceStars2.png")
	stars3 = pygame.image.load("SpaceStars3.png")
	stars4 = pygame.image.load("SpaceStars4.png")
	stars5 = pygame.image.load("SpaceStars5.png")
	stars6 = pygame.image.load("SpaceStars6.png")
	stars7 = pygame.image.load("SpaceStars7.png")
	stars8 = pygame.image.load("SpaceStars8.png")
	stars9 = pygame.image.load("SpaceStars9.png")
	stars10 = pygame.image.load("SpaceStars10.png")
	stars11 = pygame.image.load("SpaceStars11.png")
	stars12 = pygame.image.load("SpaceStars12.png")
	
	explosion = pygame.image.load("explosion-effect-PNG-image-thumb26.png")
	lightexplosion = pygame.image.load("lightexplosion.png")
	explosion = pygame.transform.scale(explosion, (exX, exY))
	lightexplosion = pygame.transform.scale(lightexplosion, (exX, exY))
	Bexplosion = pygame.transform.scale(explosion, (exX + 25, exY + 25))
	Blightexplosion = pygame.transform.scale(lightexplosion, (exX + 25, exY + 25))
	
	level1and2back = [stars1, stars2, stars3, stars4, stars5, stars6, stars7, stars8, stars9, stars10, stars11, stars12]
	
	for i in level1and2back:
		i = pygame.transform.scale(i, SIZE)
	
	spaceship = pygame.Rect(int(X / 2), Y - 180, 60, 180)
	spaceshipIMG = pygame.image.load("Beta_Team_Solar_System_Space_Shuttle.png")
	spaceshipIMG = pygame.transform.scale(spaceshipIMG, (140, 180))
	xObstacle, yObstacle = (40, 25)
	starsX = 0
	starsY = 0
	obstacle = []
	
	sateliteIMG = pygame.image.load("satelite-hi.png")
	sateliteIMG = pygame.transform.scale(sateliteIMG, (75, 75))
	asteroidIMG = pygame.image.load("Asteroid.png")
	asteroidIMG = pygame.transform.scale(asteroidIMG, (75, 75))
	flameIMG = pygame.image.load("misc_fire_element_png_by_dbszabo1-d54jgfp.png")
	flameIMG = pygame.transform.scale(flameIMG, (70, 180))
	lighterFlameIMG = pygame.image.load("lighterflame.png")
	lighterFlameIMG = pygame.transform.scale(lighterFlameIMG, (70, 180))
	darkerFLameIMG = pygame.image.load("darkerflame.png")
	darkerFLameIMG = pygame.transform.scale(darkerFLameIMG, (70, 180))
	
	
	obastacleIMGs = [sateliteIMG, asteroidIMG]
	
	sliceStarsList = 0
	checkTemp = 0
	kmh = 13000
	add = 0
	level = ""
	temp = 0
	stopAnime = 0
	speedBackobj = 14
	
	levelstop1 = True
	levelstop2 = True
	levelstop3 = True
	levelstop4 = True
	levelstop5 = True
	levelstop6 = True
	levelstop7 = True
	levelstop8 = True
	levelstop9 = True
	levelstop10 = True

	sliceStars = True
	while GAME:
		j += 1
		LEVEL2 = j >= 750 and j < 1500
		LEVEL3 = j >= 1500 and j < 2000
		LEVEL4 = j >= 2000 and j < 3000
		LEVEL5 = j >= 3000 and j < 3500
		LEVEL6 = j >= 3500 and j < 4750
		LEVEL7 = j >= 4750 and j < 6500
		LEVEL8 = j >= 6500 and j < 7500
		LEVEL9 = j >= 7500 and j < 8750
		LEVEL10 = j >= 8750 and j < 10000
	
		if LEVEL1 and levelstop1: level = 1; kmh = 14000; levelstop1 = False
		if LEVEL2 and levelstop2: level = 2; kmh = 15000; levelstop2 = False
		if LEVEL3 and levelstop3: level = 3; kmh = 16000; levelstop3 = False
		if LEVEL4 and levelstop4: level = 4; kmh = 17000; levelstop4 = False
		if LEVEL5 and levelstop5: level = 5; kmh = 18000; levelstop5 = False
		if LEVEL6 and levelstop6: level = 6; kmh = 19000; levelstop6 = False
		if LEVEL7 and levelstop7: level = 7; kmh = 20000; levelstop7 = False
		if LEVEL8 and levelstop8: level = 8; kmh = 21000; levelstop8 = False
		if LEVEL9 and levelstop9: level = 9; kmh = 22000; levelstop9 = False
		if LEVEL10 and levelstop10: level = 10; kmh = 23000; levelstop10 = False
	
		if j % 3 == 0:
			sliceStarsList += 1
			if sliceStarsList > 11:
				sliceStarsList = 0                
	
		text = font.render("{0:n}".format(kmh) + " km/h                       " + "LEVEL: "+ str(level) , True, (255, 255, 255))
	
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_a or event.key == K_LEFT:
					left = True
					right = False
				if event.key == K_d or event.key == K_RIGHT:
					right = True
					left = False
				if event.key == K_w or event.key == K_UP:
					top = True
					down = False
					if musicPlaying: boost.play()
				if event.key == K_s or event.key == K_DOWN:
					down = True
					top = False
				if event.key == K_m:
					if musicPlaying:
						pygame.mixer.music.stop()
					else:
						pygame.mixer.music.play(-1, 0.0)
					musicPlaying = not musicPlaying
	
			if event.type == KEYUP:
				if event.key == K_ESCAPE:
					introBool = True
					pygame.mixer.music.stop()
					introAll()
				if event.key == K_a or event.key == K_LEFT:
					left = False
				if event.key == K_d or event.key == K_RIGHT:
					right = False
				if event.key == K_w or event.key == K_UP:
					top = False
				if event.key == K_s or event.key == K_DOWN:
					down = False
	
		# Controling the Shuttle
		if left and spaceship.left > 20:
			spaceship.left -= SHUTTLESPEED
		if right and spaceship.right < X - 20:
			spaceship.left += SHUTTLESPEED
		if top and spaceship.top > 0:
			spaceship.top -= SHUTTLESPEED
		if down and spaceship.top < Y - 180:
			spaceship.top += SHUTTLESPEED
		if spaceship.top < Y - 180:
			spaceship.top += 1
	
		# Satelite path
		if LEVEL1 and append1:
			#SATELITESPEED = 8
			obstacle.append(pygame.Rect(random.randint(0, X - 75), - 180, xObstacle, yObstacle))
			append1 = False
		if LEVEL2:
			SATELITESPEED = 6
		elif LEVEL3 and append2:
			obstacle.append(pygame.Rect(random.randint(0, X - 75), - 180, xObstacle, yObstacle))
			append2 = False
		elif LEVEL4:
			SATELITESPEED = 8
		elif LEVEL5 and append3:
			obstacle.append(pygame.Rect(random.randint(0, X - 75), - 180, xObstacle, yObstacle))
			append3 = False
		elif LEVEL6:
			SATELITESPEED = 10
		elif LEVEL7 and append4:
			append4 = False
			obstacle.append(pygame.Rect(random.randint(0, X - 75), - 180, xObstacle, yObstacle))
		elif LEVEL8:
			SATELITESPEED = 12
		elif LEVEL9 and append5:
			append5 = False
			obstacle.append(pygame.Rect(random.randint(0, X - 75), - 180, xObstacle, yObstacle))
		elif LEVEL10:
			SATELITESPEED = 14

	
		for i in obstacle:
			if i.colliderect(spaceship):
				explosionAnimation = True
				GAME = False
				break
			i.top += SATELITESPEED
			if i.top > Y:
				i.top = -180
				i.left = random.randint(0, X - 75)
	
		SURF.blit(level1and2back[sliceStarsList], (0, 0))
		#pygame.draw.rect(SURF, (0, 255, 0), spaceship)
		SURF.blit(spaceshipIMG, (spaceship.left - 40, spaceship.top))
		if j % 3 == 0:
			add = random.randint(1, 20)
			SURF.blit(flameIMG, (spaceship.left - 30, spaceship.top + 170))
			SURF.blit(flameIMG, (spaceship.left + 15, spaceship.top + 170))
		elif j % 2 == 0:
			add = - random.randint(1, 20)
			SURF.blit(lighterFlameIMG, (spaceship.left - 30, spaceship.top + 170))
			SURF.blit(lighterFlameIMG, (spaceship.left + 15, spaceship.top + 170))
		else:
			SURF.blit(darkerFLameIMG, (spaceship.left - 30, spaceship.top + 170))
			SURF.blit(darkerFLameIMG, (spaceship.left + 15, spaceship.top + 170))
	
		kmh += add
		SURF.blit(text, (0, 0))
		for i in obstacle:
			checkTemp += 1
			if checkTemp % 2 == 0:
				#pygame.draw.rect(SURF, (255, 0, 0), i)
				SURF.blit(obastacleIMGs[1], (i.left - 20, i.top - 15))
			else:
				#pygame.draw.rect(SURF, (0, 0, 255), i)
				SURF.blit(obastacleIMGs[0], (i.left - 25, i.top - 20))
				
		checkTemp = 0
		CLOCK.tick(60)
		pygame.display.update()
	
	records = open("recordlist.txt", "a")
	records.write(str(level) + "\n")
	records.close
	
	pygame.mixer.music.stop()
	count = 1

	font2 = pygame.font.SysFont("Arial Black", 70)
	explosionSound = pygame.mixer.Sound("Explosion+3.ogg")
	explosionSound2 = pygame.mixer.Sound("Explosion+6.ogg")
	gameOver = font2.render("Game Over!", True, (255, 255, 255))
	menuInfo = font.render("Press ESC key for Main Menu", True, (135, 136, 156))
	while explosionAnimation:
		count += 1
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					explosionAnimation = False
					introBool = True; introAll()
	
		if count < 12:
			if musicPlaying:
				explosionSound.play()
			if not count % 2 == 0:
				SURF.blit(explosion, spaceship)
			else:
				SURF.blit(lightexplosion, spaceship)
		elif count >= 12 and count < 25:
			if musicPlaying:
				explosionSound2.play()
			explosion = pygame.transform.scale(explosion, (exX + 25, exY + 25))
			lightexplosion = pygame.transform.scale(lightexplosion, (exX + 25, exY + 25))
			if not count % 2 == 0:
				SURF.blit(explosion, (spaceship.left - 25, spaceship.top - 10))
			else:
				SURF.blit(lightexplosion, (spaceship.left - 25, spaceship.top - 10))
		elif count >= 25 and count < 50:
			if musicPlaying:
				explosionSound.play()
			explosion = pygame.transform.scale(explosion, (exX + 50, exY + 50))
			lightexplosion = pygame.transform.scale(lightexplosion, (exX  + 50, exY + 50))
			if not count % 2 == 0:
				SURF.blit(explosion, (spaceship.left - 50, spaceship.top - 25))
			else:
				SURF.blit(lightexplosion, (spaceship.left - 50, spaceship.top - 25))
		elif count >= 50 and count < 75:
			if musicPlaying:
				explosionSound.play()
			explosion = pygame.transform.scale(explosion, (exX + 100, exY + 100))
			lightexplosion = pygame.transform.scale(lightexplosion, (exX + 100, exY + 100))
			if not count % 2 == 0:
				SURF.blit(explosion, (spaceship.left - 80, spaceship.top - 50))
			else:
				SURF.blit(lightexplosion, (spaceship.left - 80, spaceship.top - 50))
		elif count >= 75 and count < 125:
			if musicPlaying:
				explosionSound.play()
			explosion = pygame.transform.scale(explosion, (exX + 200, exY + 200))
			lightexplosion = pygame.transform.scale(lightexplosion, (exX + 200, exY + 200))
			if not count % 2 == 0:
				SURF.blit(explosion, (spaceship.left - 120, spaceship.top - 75))
			else:
				SURF.blit(lightexplosion, (spaceship.left - 120, spaceship.top - 75))
		elif count >= 125 and count < 200:
			if musicPlaying:
				explosionSound.play()
			explosion = pygame.transform.scale(explosion, (exX + 400, exY + 400))
			lightexplosion = pygame.transform.scale(lightexplosion, (exX + 400, exY + 400))
			if not count % 2 == 0:
				SURF.blit(explosion, (spaceship.left - 220, spaceship.top - 135))
			else:
				SURF.blit(lightexplosion, (spaceship.left - 220, spaceship.top - 135))
			SURF.blit(gameOver, (70, 300))
			SURF.blit(menuInfo, (70, 400))

	
		CLOCK.tick(60)
		pygame.display.update()

def introAll():
	pygame.mixer.music.load("David Bowie - Space Oddity.mp3")
	pygame.mixer.music.play(-1, 42.0)
	intro()
	controls()
	highscores()
	about()

introAll()
GAMELOOP()
