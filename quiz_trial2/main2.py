import pygame
import time
import random
import pygame.gfxdraw

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800 #int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Quiz Trial 2')

BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50

QUESTION_WIDTH = 900
QUESTION_HEIGHT = 450

#define colours
BG = (144, 201, 120)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)


#set framerate
clock = pygame.time.Clock()
FPS = 60

#define font
def fontsize(size):
	font = pygame.font.SysFont("Futura", 30)
	return font

font_default = fontsize(30)


#load background
bkg = pygame.image.load('hearts/img/background/background.png').convert_alpha()
backgrnd = pygame.transform.scale(bkg, (SCREEN_WIDTH, SCREEN_HEIGHT))

#load questions
Q1_img_image = pygame.image.load('quiz_trial2/assets/questions/Q1.png').convert_alpha()
Q1_img = pygame.transform.scale(Q1_img_image, (QUESTION_WIDTH, QUESTION_HEIGHT))

Q2_img_image = pygame.image.load('quiz_trial2/assets/questions/Q2.png').convert_alpha()
Q2_img = pygame.transform.scale(Q2_img_image, (QUESTION_WIDTH, QUESTION_HEIGHT))

Q3_img_image = pygame.image.load('quiz_trial2/assets/questions/Q3.png').convert_alpha()
Q3_img = pygame.transform.scale(Q3_img_image, (QUESTION_WIDTH, QUESTION_HEIGHT))

#load buttons
yes_img_image = pygame.image.load('quiz_trial2/assets/buttons/yes.png').convert_alpha()
yes_img = pygame.transform.scale(yes_img_image, (BUTTON_WIDTH, BUTTON_HEIGHT))

no_img_image = pygame.image.load('quiz_trial2/assets/buttons/no.png').convert_alpha()
no_img = pygame.transform.scale(no_img_image, (BUTTON_WIDTH, BUTTON_HEIGHT))

true_img_image = pygame.image.load('quiz_trial2/assets/buttons/true.png').convert_alpha()
true_img = pygame.transform.scale(true_img_image, (BUTTON_WIDTH, BUTTON_HEIGHT))

false_img_image = pygame.image.load('quiz_trial2/assets/buttons/false.png').convert_alpha()
false_img = pygame.transform.scale(false_img_image, (BUTTON_WIDTH, BUTTON_HEIGHT))

fishing_net_img_image = pygame.image.load('quiz_trial2/assets/buttons/fishing_net.png').convert_alpha()
fishing_net_img = pygame.transform.scale(fishing_net_img_image, (BUTTON_WIDTH, BUTTON_HEIGHT))
fishing_rod_img_image = pygame.image.load('quiz_trial2/assets/buttons/fishing_rod.png').convert_alpha()
fishing_rod_img = pygame.transform.scale(fishing_rod_img_image, (BUTTON_WIDTH, BUTTON_HEIGHT))

def draw_bg():
	screen.fill(BG)
	pygame.draw.line(screen, RED, (0, 300), (SCREEN_WIDTH, 300))

#button class
buttons = pygame.sprite.Group()
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()
        
        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True #the button HAS BEEN CLICKED
                #print/output something

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))
        buttons.add(self)
        return action

labels = []
class Label:
#TRY TO REMOVE THIS CLASS AND RETAIN def draw and def change_text. COPY WHOLE THING INTO NEW MAIN FILE
	''' CLASS FOR TEXT LABELS ON THE WIN SCREEN SURFACE '''
	def __init__(self, screen, text, x, y, size=20, color="white"):
		if size != 20:
			self.font = fontsize(size)
		else:
			self.font = font_default
		self.image = self.font.render(text, 1, color)
		_, _, w, h = self.image.get_rect()
		self.rect = pygame.Rect(x, y, w, h)
		self.screen = screen
		labels.append(self)
 
	def change_text(self, newtext, color="white"):
		self.image = self.font.render(newtext, 1, color)
 
	def draw(self):
		self.screen.blit(self.image, (self.rect))
 
 
def show_labels():
	for _ in labels:
		_.draw()

#ACTION FOR BUTTON CLICK
def on_right():
    check_score = ("right")

def on_false():
    #if there is no "right" argument, therefore false
    check_score()

def check_score(answered = "wrong"):
    #check if the answer is correct
    global qnum, points

    #until there are questions left to iterate
    if qnum < len(questions):
        if answered == "right":
            time.sleep(0.1)     #this is to avoid adding more points when pressing too much
            points += 1
        qnum += 1       #counter for the next question in the list
        score.change_text(str(points))
        title.swap_image(questions[qnum-1][0])
        show_question(qnum) #delete olf buttons and show new

    #this is for the last question
    elif qnum == len(questions):
        if answered == "right":
            kill()
            time.sleep(0.1)
            points += 1
        if points < 3:
            #print sumthing here
            score.change_text("you failed") #THIS IS TEMPORARY. REPLACE WITH SOMETHING ELSE
        elif points == 3:
            score.change_text("you fpassed") #THIS IS TEMPORARY. REPLACE WITH SOMETHING ELSE
    time.sleep(0.5)

#create button instances
yes_button = Button((SCREEN_WIDTH / 2) / 2, 600, yes_img)
no_button = Button((SCREEN_WIDTH / 2) + (SCREEN_WIDTH / 6), 600, no_img)
fishing_net_button = Button((SCREEN_WIDTH / 2) / 2, 600, fishing_net_img)
fishing_rod_button = Button((SCREEN_WIDTH / 2) / 2, 600, fishing_rod_img)

#create sprite groups
questions = [
    [Q1_img, [no_img, yes_img]],
    [Q2_img, [fishing_net_img, fishing_rod_img]],
    [Q3_img, [no_img, yes_img]],
]

def show_question(qnum):
    kill()

def kill():
    for _ in buttons:
        _.kill()

qnum = 1
points = 0

#SOME LABELS
score = Label(screen, "Futura", 150, 150)
title = Label(screen, questions[qnum-1][0], SCREEN_WIDTH - 450, 200)

def start_again():
    pass

def loop():
    global game_on
    show_question(qnum)

run = True
while run:
    clock.tick(FPS)
    
    draw_bg()
    screen.blit(backgrnd, (0,0))

    #add if statement for collision here
    #draw questions here
    buttons.update()
    buttons.draw(screen)
    show_labels()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
