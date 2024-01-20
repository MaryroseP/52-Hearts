from cgi import test
from queue import Empty
from turtle import Screen
from xml.etree.ElementTree import TreeBuilder
import pygame
from pygame import MOUSEBUTTONDOWN, mixer
import os
import random
import csv
import button
import time
mixer.init()
pygame.init()


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800

QUESTION_WIDTH = 750
QUESTION_HEIGHT = 550

QUESTION_WIDTH2 = 750
QUESTION_HEIGHT2 = 550

BUTTON_WIDTH = 300
BUTTON_HEIGHT = 80

QUESTION_X = 255
QUESTION_Y = 120
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('52 Hearts')


clock = pygame.time.Clock()
FPS = 60

GRAVITY = 0.3
ROWS = 25
COLS = 40
TILE_SIZE = SCREEN_HEIGHT // ROWS
TILE_TYPES = 130
level = 1
volume = 0.2
volume = volume
mdialogue = False
mdialogue1 = False
mdialogue_finished = False
done = False
start_menu = True
start_game = False
instructions = False
start_intro = False
start_reverse_intro = False
pause_game = False
start_quiz = False
start_mdialogue = False
q1 = False
test_complete = False
start_cutscene = False
end_cutscene = False
credits = False
#define player action variables
moving_left = False
moving_right = False

#load music n sounds
pygame.mixer.music.load('assets/audio/moosic.wav')
pygame.mixer.music.play(-1)
jump_sfx = pygame.mixer.Sound('assets/audio/jump.wav')
jump_sfx.set_volume(0.5)

#cutscene images
cutscene_img_image = pygame.image.load("assets/img/mainscreen_cutscenescroll.png").convert_alpha()
endcut1 = pygame.image.load('assets/img/endcut/1.png').convert_alpha()
endcut2 = pygame.image.load('assets/img/endcut/2.png').convert_alpha()
endcut3 = pygame.image.load('assets/img/endcut/3.png').convert_alpha()
endcut4 = pygame.image.load('assets/img/endcut/4.png').convert_alpha()

#load images
shelf1_img = pygame.image.load('assets/img/bookshelves/1.png').convert_alpha()
shelf2_img = pygame.image.load('assets/img/bookshelves/2.png').convert_alpha()
shelf3_img = pygame.image.load('assets/img/bookshelves/3.png').convert_alpha()
shelf4_img = pygame.image.load('assets/img/bookshelves/4.png').convert_alpha()
shelf5_img = pygame.image.load('assets/img/bookshelves/5.png').convert_alpha()

sinarapan_img = pygame.image.load('assets/img/description/sinarapan.png').convert_alpha()
net_img = pygame.image.load('assets/img/description/net.png').convert_alpha()
tilapia_img = pygame.image.load('assets/img/description/tilapia.png').convert_alpha()
coral_img = pygame.image.load('assets/img/description/coral.png').convert_alpha()
sand_img = pygame.image.load('assets/img/description/sand.png').convert_alpha()
boracay_img = pygame.image.load('assets/img/description/boracay.png').convert_alpha()
dory_img = pygame.image.load('assets/img/description/dory.png').convert_alpha()
pole_img = pygame.image.load('assets/img/description/fishingrod.png').convert_alpha()

logo_img = pygame.image.load('assets/img/logo.png').convert_alpha()
endgame_img = pygame.image.load('assets/img/endgame.png').convert_alpha()
#button imgs
start_img = pygame.image.load('assets/img/start_btn.png').convert_alpha()
exit_img = pygame.image.load('assets/img/exit_btn.png').convert_alpha()
pause_img = pygame.image.load('assets/img/pause_btn.png').convert_alpha()
quiz_img = pygame.image.load('assets/img/pause_btn.png').convert_alpha()
interact_img = pygame.image.load('assets/img/interact_btn.png').convert_alpha()
next_img = pygame.image.load('assets/img/next_btn.png').convert_alpha()
proceed_img = pygame.image.load('assets/img/proceed_btn.png').convert_alpha()
instructions_btn_img = pygame.image.load('assets/img/instructions_btn.png').convert_alpha()
instructions_img = pygame.image.load('assets/img/instructions.png').convert_alpha()
return_img = pygame.image.load('assets/img/return_btn.png').convert_alpha()
lowvol_img = pygame.image.load('assets/img/lowvol_btn.png').convert_alpha()
highvol_img = pygame.image.load('assets/img/highvol_btn.png').convert_alpha()
#bkg imgs
bkg = pygame.image.load('assets/img/background/editedbg.png').convert_alpha()
backgrnd = pygame.transform.scale(bkg, (SCREEN_WIDTH, SCREEN_HEIGHT))
titlesc = bkg = pygame.image.load('assets/img/background/titlescreen.png').convert_alpha()
titlescreen = pygame.transform.scale(titlesc, (SCREEN_WIDTH, SCREEN_HEIGHT))

#load parameters
passed_img_image = pygame.image.load('quiz_trial2/assets/parameters/passed.png').convert_alpha()
passed_img = pygame.transform.scale(passed_img_image, (QUESTION_WIDTH, QUESTION_HEIGHT))

failed_img_image = pygame.image.load('quiz_trial2/assets/parameters/failed.png').convert_alpha()
failed_img = pygame.transform.scale(failed_img_image, (QUESTION_WIDTH, QUESTION_HEIGHT))

#mermaid dialogues
md1 = pygame.image.load('assets/img/mermaid dialogue/1.png').convert_alpha()
md2 = pygame.image.load('assets/img/mermaid dialogue/2.png').convert_alpha()
md3 = pygame.image.load('assets/img/mermaid dialogue/3.png').convert_alpha()
md4 = pygame.image.load('assets/img/mermaid dialogue/4.png').convert_alpha()
mdyes = pygame.image.load('assets/img/mermaid dialogue/yes.png').convert_alpha()
mdpassed = pygame.image.load('assets/img/mermaid dialogue/passed.png').convert_alpha()
mdfailed = pygame.image.load('assets/img/mermaid dialogue/failed.png').convert_alpha()
mdgoodbye = pygame.image.load('assets/img/mermaid dialogue/goodbye.png').convert_alpha()
#load questions
Q1_img_image = pygame.image.load('quiz_trial2/assets/questions/quiz(1).png').convert_alpha()
Q1_img = pygame.transform.scale(Q1_img_image, (QUESTION_WIDTH, QUESTION_HEIGHT))

Q2_img_image = pygame.image.load('quiz_trial2/assets/questions/quiz(2).png').convert_alpha()
Q2_img = pygame.transform.scale(Q2_img_image, (QUESTION_WIDTH, QUESTION_HEIGHT))

Q3_img_image = pygame.image.load('quiz_trial2/assets/questions/quiz(3).png').convert_alpha()
Q3_img = pygame.transform.scale(Q3_img_image, (QUESTION_WIDTH, QUESTION_HEIGHT))

Q4_img_image = pygame.image.load('quiz_trial2/assets/questions/quiz(4).png').convert_alpha()
Q4_img = pygame.transform.scale(Q4_img_image, (QUESTION_WIDTH, QUESTION_HEIGHT))

Q5_img_image = pygame.image.load('quiz_trial2/assets/questions/quiz(5).png').convert_alpha()
Q5_img = pygame.transform.scale(Q5_img_image, (QUESTION_WIDTH, QUESTION_HEIGHT))

Q6_img_image = pygame.image.load('quiz_trial2/assets/questions/quiz(6).png').convert_alpha()
Q6_img = pygame.transform.scale(Q6_img_image, (QUESTION_WIDTH, QUESTION_HEIGHT))

#load buttons
yes_img_image = pygame.image.load('quiz_trial2/assets/answers/answer_yes.png').convert_alpha()
yes_img = pygame.transform.scale(yes_img_image, (BUTTON_WIDTH, BUTTON_HEIGHT))

no_img_image = pygame.image.load('quiz_trial2/assets/answers/answer_no.png').convert_alpha()
no_img = pygame.transform.scale(no_img_image, (BUTTON_WIDTH, BUTTON_HEIGHT))

true_img_image = pygame.image.load('quiz_trial2/assets/answers/answer_true.png').convert_alpha()
true_img = pygame.transform.scale(true_img_image, (BUTTON_WIDTH, BUTTON_HEIGHT))

false_img_image = pygame.image.load('quiz_trial2/assets/answers/answer_false.png').convert_alpha()
false_img = pygame.transform.scale(false_img_image, (BUTTON_WIDTH, BUTTON_HEIGHT))

fishing_net_img_image = pygame.image.load('quiz_trial2/assets/answers/answer_net.png').convert_alpha()
fishing_net_img = pygame.transform.scale(fishing_net_img_image, (BUTTON_WIDTH, BUTTON_HEIGHT))

fishing_rod_img_image = pygame.image.load('quiz_trial2/assets/answers/answer_hook.png').convert_alpha()
fishing_rod_img = pygame.transform.scale(fishing_rod_img_image, (BUTTON_WIDTH, BUTTON_HEIGHT))

#store tiles in a list
img_list = []
for x in range(TILE_TYPES):
	img = pygame.image.load(f'assets/img/tile/{x}.png')
	img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
	img_list.append(img)

#define colours
BG = (144, 201, 120)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BLUE = (71,84,182)
TRANSPARENT = (0, 0, 0, 0)
#define font
font = pygame.font.SysFont('Futura', 30)

def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))


def draw_bg():
	screen.fill(BG)
	pygame.draw.line(screen, RED, (0, 300), (SCREEN_WIDTH, 300))


class Soldier(pygame.sprite.Sprite):
	def __init__(self, char_type, x, y, scale, speed):
		pygame.sprite.Sprite.__init__(self)
		self.alive = True
		self.char_type = char_type
		self.speed = speed
		self.direction = 1
		self.vel_y = 0
		self.jump = False
		self.in_air = True
		self.flip = False
		self.animation_list = []
		self.frame_index = 0
		self.action = 0
		self.update_time = pygame.time.get_ticks()
		#ai specific variables
		self.move_counter = 0
		self.vision = pygame.Rect(0, 0, 150, 20)
		self.idling = False
		self.idling_counter = 0
		#load all images for the players
		animation_types = ['Idle', 'Run', 'Jump']
		for animation in animation_types:
			#reset temporary list of images
			temp_list = []
			#count number of files in the folder
			num_of_frames = len(os.listdir(f'assets/img/{self.char_type}/{animation}'))
			for i in range(num_of_frames):
				img = pygame.image.load(f'assets/img/{self.char_type}/{animation}/{i}.png').convert_alpha()
				img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
				temp_list.append(img)
			self.animation_list.append(temp_list)

		self.image = self.animation_list[self.action][self.frame_index]
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.width = self.image.get_width()
		self.height = self.image.get_height()
	
	def update(self):
		self.update_animation()
		#update cooldown
	
	def move(self, moving_left, moving_right):
		#reset movement variables
		dx = 0
		dy = 0
	
		#assign movement variables if moving left or right
		if moving_left:
			dx = -self.speed
			self.flip = True
			self.direction = -1
			
		if moving_right:
			dx = self.speed
			self.flip = False
			self.direction = 1
		
		#jump
		if self.jump == True and self.in_air == False:
			self.vel_y = -9
			self.jump = False
			self.in_air = True
		
		#apply gravity
		self.vel_y += GRAVITY
		if self.vel_y > 10:
			self.vel_y
		dy += self.vel_y

		#check for collision
		for tile in world.obstacle_list:
			#check x collision
			if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
				dx = 0
			if mdialogue == True or start_quiz == True:
				dx = 0
				self.update_action(0)#0: idle
			#check y collision
			if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
				#check if collision from below a block (jumping)
				if self.vel_y < 0:
					self.vel_y = 0
					dy = tile[1].bottom - self.rect.top
				#check if above ground (falling)
				elif self.vel_y >= 0:
					self.vel_y = 0
					self.in_air = False
					dy = tile[1].top - self.rect.bottom
		
		#check for collision with EXIT
		level_complete = False
		if pygame.sprite.spritecollide(self, exit_group, False):
			if test_complete == True:
				level_complete = True

		#check for collision with tilapia
		tilapiadesc = False
		if pygame.sprite.spritecollide(self, tilapia_group, False):
			tilapiadesc = True

		#check for collision with sinarapan
		sinarapandesc = False
		if pygame.sprite.spritecollide(self, sinarapan_group, False):
			sinarapandesc = True

		#check for collision with dory
		dorydesc = False
		if pygame.sprite.spritecollide(self, dory_group, False):
			dorydesc = True

		#check for collision with fishing pole
		boracaydesc = False
		if pygame.sprite.spritecollide(self, boracay_group, False):
			boracaydesc = True


		netdesc = False
		if pygame.sprite.spritecollide(self, net_group, False):
			netdesc = True

		poledesc = False
		if pygame.sprite.spritecollide(self, pole_group, False):
			poledesc = True

		coraldesc = False
		if pygame.sprite.spritecollide(self, coral_group, False):
			coraldesc = True

		bookshelf1desc = False
		if pygame.sprite.spritecollide(self, bookshelf1_group, False):
			bookshelf1desc = True
		#check for collision with MERMAID
		bookshelf2desc = False
		if pygame.sprite.spritecollide(self, bookshelf2_group, False):
			bookshelf2desc = True

		bookshelf3desc = False
		if pygame.sprite.spritecollide(self, bookshelf3_group, False):
			bookshelf3desc = True

		bookshelf4desc = False
		if pygame.sprite.spritecollide(self, bookshelf4_group, False):
			bookshelf4desc = True

		bookshelf5desc = False
		if pygame.sprite.spritecollide(self, bookshelf5_group, False):
			bookshelf5desc = True

		merminteract = False
		if pygame.sprite.spritecollide(self, mermaid_group, False):
			merminteract = True

		#update rectangle position
		self.rect.x += dx
		self.rect.y += dy

		if self.char_type == 'player':
			return level_complete, tilapiadesc, sinarapandesc, dorydesc, poledesc, boracaydesc, netdesc, coraldesc, bookshelf1desc, bookshelf2desc, bookshelf3desc, bookshelf3desc, bookshelf4desc, bookshelf5desc, merminteract

	def ai(self):
		if self.alive and player.alive:
			if self.idling == False:
				self.move(False, False)
				self.update_action(0)#0: idle

	def doorlogic(self):
		if test_complete == False:
			if self.idling == False:
				self.move(False, False)
				self.update_action(0)#0: idle
		elif test_complete == True:
			self.update_action(1)#run
	def update_animation(self):
		#update animation
		ANIMATION_COOLDOWN = 100
		#update image depending on current frame
		self.image = self.animation_list[self.action][self.frame_index]
		#check if enough time has passed since the last update
		if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
			self.update_time = pygame.time.get_ticks()
			self.frame_index += 1
		#if the animation has run out the reset back to the start
		if self.frame_index >= len(self.animation_list[self.action]):
			if self.action == 3:
				self.frame_index = len(self.animation_list[self.action]) - 1
			else:
				self.frame_index = 0



	def update_action(self, new_action):
		#check if the new action is different to the previous one
		if new_action != self.action:
			self.action = new_action
			#update the animation settings
			self.frame_index = 0
			self.update_time = pygame.time.get_ticks()

	def draw(self):
		screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)


class World():
	def __init__(self):
		self.obstacle_list = []

	def process_data(self, data):
		#iterate through each value in level data file
		for y, row in enumerate(data):
			for x, tile in enumerate(row):
				if tile >= 0:
					img = img_list[tile]
					img_rect = img.get_rect()
					img_rect.x = x * TILE_SIZE
					img_rect.y = y * TILE_SIZE
					tile_data = (img, img_rect)
					if tile >= 0 and tile <= 12:
						self.obstacle_list.append(tile_data)
					elif tile == 13:
						decoration = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
						decoration_group.add(decoration)

					elif tile >= 14 and tile <= 17:
						bookshelf1 = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
						bookshelf1_group.add(bookshelf1)

					elif tile >= 18 and tile <= 30:
						decoration = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
						decoration_group.add(decoration)

					elif tile >= 31 and tile <= 36:
						tilapia = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
						tilapia_group.add(tilapia)

					elif tile >= 37 and tile <= 38:
						decoration = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
						decoration_group.add(decoration)

					elif tile >= 39 and tile <= 42:
						exit = Exit(img, x * TILE_SIZE, y * TILE_SIZE)
						exit_group.add(exit)

					elif tile >= 43 and tile <= 54:
						dory = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
						dory_group.add(dory)

					elif tile >= 55 and tile <= 56:
						decoration = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
						decoration_group.add(decoration)

					elif tile >= 57 and tile <= 62:
						sinarapan = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
						sinarapan_group.add(sinarapan)
					
					elif tile >= 63 and tile <= 71:
						pole = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
						pole_group.add(pole)

					elif tile >= 72 and tile <= 76:
						decoration = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
						decoration_group.add(decoration)

					elif tile >= 77 and tile <= 80:
						boracay = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
						boracay_group.add(boracay)

					elif tile >= 81 and tile <= 89:
						net = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
						net_group.add(net)

					elif tile == 90:#create player
						player = Soldier('player', x * TILE_SIZE, y * TILE_SIZE, 1, 4)

					elif tile == 91:#create mermaid
						mermaid = Soldier('mermaid', x * TILE_SIZE, y * TILE_SIZE, 1, 7)
						mermaid_group.add(mermaid)
						
					elif tile >= 92 and tile <= 95:
						coral = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
						coral_group.add(coral)

					elif tile >= 96 and tile <= 99:
						bookshelf2 = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
						bookshelf2_group.add(bookshelf2)

					elif tile >= 100 and tile <= 103:
						bookshelf3 = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
						bookshelf3_group.add(bookshelf3)

					elif tile >= 104 and tile <= 107:
						bookshelf4 = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
						bookshelf4_group.add(bookshelf4)

					elif tile >= 108 and tile <= 111:
						bookshelf5 = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
						bookshelf5_group.add(bookshelf5)

					elif tile >= 116 and tile <= 129:
						decoration = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
						decoration_group.add(decoration)
		return player


	def draw(self):
		for tile in self.obstacle_list:
			screen.blit(tile[0], tile[1])



class Decoration(pygame.sprite.Sprite): #NON INTERACTABLES
	def __init__(self, img, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = img
		self.rect = self.image.get_rect()
		self.rect.midtop = (x + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))

class Exit(pygame.sprite.Sprite): #DONE
	def __init__(self, img, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = img
		self.rect = self.image.get_rect()
		self.rect.midtop = (x + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))

class ScreenFade():
	def __init__(self, direction, colour, speed):
		self.direction = direction
		self.colour = colour
		self.speed = speed
		self.fade_counter = 0

	def fade(self):
		fade_complete = False
		self.fade_counter += self.speed
		if self.direction == 1:#whole screen fade
			pygame.draw.rect(screen, self.colour, (0 - self.fade_counter, 0, SCREEN_WIDTH // 2, SCREEN_HEIGHT))#left
			pygame.draw.rect(screen, self.colour, (SCREEN_WIDTH // 2 + self.fade_counter, 0, SCREEN_WIDTH, SCREEN_HEIGHT))#right
			pygame.draw.rect(screen, self.colour, (0, 0 - self.fade_counter, SCREEN_WIDTH, SCREEN_HEIGHT // 2))#up
			pygame.draw.rect(screen, self.colour, (0, SCREEN_HEIGHT // 2 +self.fade_counter, SCREEN_WIDTH, SCREEN_HEIGHT))#down

		if self.direction == 2:#vertical screen fade down
			pygame.draw.rect(screen, self.colour, (0, 0, SCREEN_WIDTH, 0 + self.fade_counter))

		if self.direction == 3:#whole screen fade
			pygame.draw.rect(screen, self.colour, (0, 0, SCREEN_WIDTH, 0 + self.fade_counter))#up
			pygame.draw.rect(screen, self.colour, (0, SCREEN_HEIGHT - self.fade_counter, SCREEN_WIDTH, SCREEN_HEIGHT))#down

		if self.direction == 4:
			pygame.draw.rect(screen, self.colour, (0, 0 - self.fade_counter, SCREEN_WIDTH, SCREEN_HEIGHT // 2))#up
			pygame.draw.rect(screen, self.colour, (0, SCREEN_HEIGHT // 2 +self.fade_counter, SCREEN_WIDTH, SCREEN_HEIGHT))#down
		if self.fade_counter >= SCREEN_WIDTH:
			fade_complete = True

		return fade_complete

class Background():
	def __init__(self):
		self.bgimage = cutscene_img_image
		self.rectBGimg = self.bgimage.get_rect()
		self.bgY1 = 0
		self.bgX1 = 0
		self.movingUpSpeed = 1
			
	def update(self):
		scroll_complete = False
		self.bgY1 -= self.movingUpSpeed
		if self.bgY1 <= -2700:
			self.movingUpSpeed = 0   
			scroll_complete = True
		return scroll_complete
			
	def render(self):
		screen.blit(self.bgimage, (self.bgX1, self.bgY1))


class EndingScene:
	def __init__(self):
		self.image1 = endcut1
		self.image2 = endcut2
		self.image3 = endcut3
		self.image4 = endcut4
		self.timer = 0.5
		self.countdown = 1300

	def update(self):
		complete = False
		self.countdown -= self.timer
		if self.countdown <= 200:
			complete = True
		return complete

	def render(self):
		if self.countdown <= 1300 and self.countdown >= 1000:
			screen.blit(mdgoodbye, (0,0))
			if open_fade.fade():
					pass
		elif self.countdown <= 1000 and self.countdown >= 800:
			screen.blit(endcut1, (0,0))
		elif self.countdown <= 800 and self.countdown >= 600:
			screen.blit(endcut2, (0,0))
		elif self.countdown <= 600 and self.countdown >= 400:
			screen.blit(endcut3, (0,0))
		elif self.countdown <= 400 and self.countdown >= 200:
			screen.blit(endcut4, (0,0))
def update_groups():
	decoration_group.update()
	exit_group.update()
	tilapia_group.update()
	sinarapan_group.update()
	dory_group.update()
	pole_group.update()
	boracay_group.update()
	net_group.update()
	coral_group.update()
	bookshelf1_group.update()
	bookshelf2_group.update()
	bookshelf3_group.update()
	bookshelf4_group.update()
	bookshelf5_group.update()

def draw_groups():
	decoration_group.draw(screen)
	decoration_group.draw(screen)
	exit_group.draw(screen)
	tilapia_group.draw(screen)
	sinarapan_group.draw(screen)
	dory_group.draw(screen)
	pole_group.draw(screen)
	boracay_group.draw(screen)
	net_group.draw(screen)
	coral_group.draw(screen)
	bookshelf1_group.draw(screen)
	bookshelf2_group.draw(screen)
	bookshelf3_group.draw(screen)
	bookshelf4_group.draw(screen)
	bookshelf5_group.draw(screen)

#create screen fades
intro_fade = ScreenFade(1, BLACK, 2)
pause_fade = ScreenFade(2, BLUE, 25)
close_fade = ScreenFade(3, BLACK, 4)
open_fade = ScreenFade(4, BLACK, 4)
#create sprite groups
decoration_group = pygame.sprite.Group()
decoration_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()
tilapia_group = pygame.sprite.Group()
sinarapan_group = pygame.sprite.Group()
dory_group = pygame.sprite.Group()
pole_group = pygame.sprite.Group()
boracay_group = pygame.sprite.Group()
net_group = pygame.sprite.Group()
coral_group = pygame.sprite.Group()
bookshelf1_group = pygame.sprite.Group()
bookshelf2_group = pygame.sprite.Group()
bookshelf3_group = pygame.sprite.Group()
bookshelf4_group = pygame.sprite.Group()
bookshelf5_group = pygame.sprite.Group()
mermaid_group = pygame.sprite.Group()


start_button = button.Button(SCREEN_WIDTH // 2 - 130, SCREEN_HEIGHT // 2 - 50, start_img, 1)
exit_button = button.Button(SCREEN_WIDTH // 2 - 130, SCREEN_HEIGHT // 2 + 100, exit_img, 1)
instructions_button = button.Button(SCREEN_WIDTH // 2 - 130, SCREEN_HEIGHT // 2 + 200, instructions_btn_img, 1)
lower_button = button.Button(20, 20, lowvol_img, 0.5)
higher_button = button.Button(100, 20, highvol_img, 0.5)

pause_button = button.Button(SCREEN_WIDTH // 1 - 90, SCREEN_HEIGHT // 2 - 400, pause_img, 1 * 0.8)

quiz_button = button.Button(SCREEN_WIDTH // 1 - 90, SCREEN_HEIGHT // 2 - 400, pause_img, 1 * 0.8)

resume_button = button.Button(SCREEN_WIDTH // 2 - 125, SCREEN_HEIGHT // 2 - 70, pause_img, 1 * 1.5)

interact_button = button.Button(SCREEN_WIDTH // 2 - 130, SCREEN_HEIGHT // 2 - 100, interact_img, 1)

next_button = button.Button(1000, 720, next_img, 1)

proceed_button = button.Button(1000, 720, proceed_img, 1)

return_button = button.Button(1000, 20, return_img, 1)
return_button2 = button.Button(1000, 720, return_img, 1)

yes_button = button.Button((SCREEN_WIDTH / 2) - 175 , 380, yes_img, 1)
no_button = button.Button((SCREEN_WIDTH / 2) - 175, 500, no_img, 1)

yes_button2 = button.Button((SCREEN_WIDTH / 2) - 450, 410, yes_img, 1)
no_button2 = button.Button((SCREEN_WIDTH / 2) - (-150), 410, no_img, 1)

fishing_net_button = button.Button((SCREEN_WIDTH / 2) - 175, 380, fishing_net_img, 1)
fishing_rod_button = button.Button((SCREEN_WIDTH / 2) - 175, 500, fishing_rod_img, 1)

true_button = button.Button((SCREEN_WIDTH / 2) - 175 , 380, true_img, 1)
false_button = button.Button((SCREEN_WIDTH / 2) - 175, 500, false_img, 1)

back_ground = Background()
ending_scene = EndingScene()

points = 0
def point_count():
    global points
    points += 1

#create empty tile list
world_data = []
for row in range(ROWS):
	r = [-1] * COLS
	world_data.append(r)
#load in level data and create world
with open(f'assets/level{level}_data.csv', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for x, row in enumerate(reader):
		for y, tile in enumerate(row):
			world_data[x][y] = int(tile)
world = World()
player = world.process_data(world_data)


run = True
while run:

	clock.tick(FPS)
	pygame.mixer.music.set_volume(volume)
	if start_menu == True:
		#main menu
		#draw menu
		screen.blit(cutscene_img_image, (0,0))
		screen.blit(logo_img, (350, 50))
		#add buttons
		if start_button.draw(screen):
			start_menu = False
			start_cutscene = True
		if exit_button.draw(screen):
			run = False
		if instructions_button.draw(screen):
			start_menu = False
			instructions = True
		if lower_button.draw(screen):
			volume -= 0.05
			if volume <= 0:
				volume = 0
		if higher_button.draw(screen):
			volume += 0.05
			if volume >= 1:
				volume = 1
	elif instructions == True:
		screen.blit(instructions_img, (0,0))
		if return_button.draw(screen):
			instructions = False
			start_menu = True
	elif pause_game == True:
		if pause_fade.fade():
			screen.blit(titlescreen, (0,0))
			#add buttons
			if resume_button.draw(screen):
				pause_fade.fade_counter = 0
				pause_game = False
			if exit_button.draw(screen):
				run = False
			if lower_button.draw(screen):
				volume -= 0.05
				if volume <= 0:
					volume = 0
			if higher_button.draw(screen):
				volume += 0.05
				if volume >= 1:
					volume = 1
	elif start_cutscene == True:
			back_ground.update()
			back_ground.render()
			if back_ground.update():
				start_cutscene = False
				start_game = True
				start_intro = True


	elif end_cutscene == True:
		start_game = False
		if close_fade.fade():
				if ending_scene.update():
					if close_fade.fade():
						end_cutscene = False
						credits = True
				ending_scene.render()
	elif credits == True:
		screen.blit(endgame_img, (0,0))
	elif start_game == True:	
		#update background
		if start_game == True:
			screen.blit(backgrnd, (0,0))
		#draw world map
		world.draw()

		#update and draw groups
		update_groups()
		draw_groups()

		for mermaid in mermaid_group:
			mermaid.ai()
			mermaid.update()
			mermaid.draw()

		player.update()
		player.draw()
		#show intro
		if start_intro == True:
			if intro_fade.fade():
				start_intro = False
				intro_fade.fade_counter = 0

		if start_reverse_intro == True:
			if close_fade.fade():
				start_reverse_intro = False
				close_fade.fade_counter = 0

		#update player actions
		if player.alive:
			if player.in_air:
				player.update_action(2)#2: jump
			elif moving_left or moving_right:
				player.update_action(1)#1: run
			else:
				player.update_action(0)#0: idle
			level_complete, tilapiadesc, sinarapandesc, dorydesc, poledesc, boracaydesc, netdesc, coraldesc, bookshelf1desc, bookshelf2desc, bookshelf3desc, bookshelf3desc, bookshelf4desc, bookshelf5desc, merminteract = player.move(moving_left, moving_right)

			#blit descriptions
			if tilapiadesc == True:
				screen.blit(tilapia_img, (0,485))
				
			if sinarapandesc == True:
				screen.blit(sinarapan_img, (280,485))
			
			if dorydesc == True:
				screen.blit(dory_img, (0,485))
			
			if poledesc == True:
				screen.blit(pole_img, (0,485))

			if boracaydesc == True:
				screen.blit(boracay_img, (280,485))

			if netdesc == True:
				screen.blit(net_img, (280,485))
			
			if coraldesc == True:
				screen.blit(coral_img, (0,485))

			if bookshelf1desc == True:
				screen.blit(shelf1_img, (150, 400))
			
			if bookshelf2desc == True:
				screen.blit(shelf2_img, (150, 400))

			if bookshelf3desc == True:
				screen.blit(shelf3_img, (150, 400))

			if bookshelf4desc == True:
				screen.blit(shelf4_img, (150, 400))

			if bookshelf5desc == True:
				screen.blit(shelf5_img, (10,720))

			#pops up the BUTTON  to start mermaid dialogue that leads to the quiz
			if merminteract == True and start_quiz == False and test_complete == False and mdialogue == False:
				if interact_button.draw(screen):
					start_mdialogue = True
			else:
				start_dialogue = False

			if start_mdialogue == True:
				if pause_fade.fade():
					if merminteract == True and start_mdialogue == True:
						mdialogue = True
						mdialogue1 = True
						start_mdialogue = False

			#Mermaid's dialogue before the quiz
			if mdialogue == True and merminteract == True and start_quiz == False:
				if mdialogue1 == True:
					screen.blit(md1, (0,0))
					if next_button.draw(screen):
						time.sleep(.1)
						mdialogue1 = False
						mdialogue2 = True
				elif mdialogue2 == True:
					screen.blit(md2, (0,0))
					if next_button.draw(screen):
						time.sleep(.1)
						mdialogue2 = False
						mdialogue3 = True
				elif mdialogue3 == True:
					screen.blit(md3, (0,0))
					if next_button.draw(screen):
						time.sleep(.1)
						mdialogue3 = False
						mdialogue4 = True
				elif mdialogue4 == True:
					screen.blit(md4, (0,0))
					#mdialogue_finished = True
					if yes_button2.draw(screen):
						time.sleep(.1)
						mdialogue4 = False
						mdialogue5 = True
					elif no_button2.draw(screen):
						time.sleep(.1)
						mdialogue = False
				elif mdialogue5 == True:
					screen.blit(mdyes, (0,0))
					if proceed_button.draw(screen):
						mdialogue5 = False
						go_quiz = True
				elif go_quiz == True:
					mdialogue = False
					start_quiz = True
					q1 = True
					points = 0
			#this is the stage where the player will have to decide whether or not they're ready to take the quiz

			#start the quiz while the player is colliding w mermaid
			if start_quiz and merminteract == True:
				if q1 == True:
					screen.blit(Q1_img, (QUESTION_X, QUESTION_Y))
					if yes_button.draw(screen):
						time.sleep(.1) 
						q1 = False
						q2 = True
					elif no_button.draw(screen): #DOWN
						time.sleep(.1)
						points += 1
						q1 = False
						q2 = True
				elif q2 == True:
					screen.blit(Q2_img, (QUESTION_X, QUESTION_Y))
					if fishing_net_button.draw(screen): #UP
						time.sleep(.1)
						points += 1
						q2 = False
						q3 = True
					elif fishing_rod_button.draw(screen):
						time.sleep(.1)
						q2 = False
						q3 = True
				elif q3 == True:
					screen.blit(Q3_img, (QUESTION_X, QUESTION_Y))
					if yes_button.draw(screen): 
						time.sleep(.1)
						q3 = False
						q4 = True
					elif no_button.draw(screen): #DOWN
						time.sleep(.1)
						points += 1
						q3 = False
						q4 = True
				elif q4 == True:
					screen.blit(Q4_img, (QUESTION_X, QUESTION_Y))
					if true_button.draw(screen): 
						time.sleep(.1)
						q4 = False
						q5 = True
					elif false_button.draw(screen): #DOWN
						time.sleep(.1)
						points += 1
						q4 = False
						q5 = True
				elif q5 == True:
					screen.blit(Q5_img, (QUESTION_X, QUESTION_Y))
					if true_button.draw(screen): 
						time.sleep(.1)
						q5 = False
						q6 = True
					elif false_button.draw(screen): #DOWN
						time.sleep(.1)
						points += 1
						q5 = False
						q6 = True
				elif q6 == True:
					screen.blit(Q6_img, (QUESTION_X, QUESTION_Y))
					if yes_button.draw(screen): #UP
						time.sleep(.1)
						points += 1
						q6 = False
						q7 = True
					elif no_button.draw(screen):
						time.sleep(.1)
						q6 = False
						q7 = True
				elif q7 == True:
					if points < 6:
						screen.blit (mdfailed, (0, 0))
						if return_button2.draw(screen):
							start_quiz = False
					elif points == 6:
						screen.blit (mdpassed, (0, 0))
						if proceed_button.draw(screen):
							start_quiz = False
							test_complete = True
							

			if level_complete == True:
				level_complete = False
				start_game = False
				endscene1 = True
				end_cutscene = True

					
		if pause_button.draw(screen):
			pause_game = True

	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False

		#keyboard presses
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				moving_left = True
			if event.key == pygame.K_d:
				moving_right = True
			if event.key == pygame.K_w and player.alive and player.in_air == False:
				player.jump = True
				jump_sfx.play()
			if event.key == pygame.K_ESCAPE:
				if pause_game == True:
					pause_fade.fade_counter = 0
					pause_game = False
				elif pause_game == False:
					pause_game = True

		#keyboard button released
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_a:
				moving_left = False
			if event.key == pygame.K_d:
				moving_right = False
	pygame.display.update()

pygame.quit()