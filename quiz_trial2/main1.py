import pygame

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800 #int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Quiz Trial 2')

BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50

QUESTION_WIDTH = 500
QUESTION_HEIGHT = 250

QUESTION_X = (SCREEN_WIDTH/2) - 225
QUESTION_Y = 150

#set framerate
clock = pygame.time.Clock()
FPS = 60

#define colours
BG = (144, 201, 120)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
transparent = (0, 0, 0, 0)

#define font
font = pygame.font.SysFont('Futura', 30)

def draw_bg():
	screen.fill(BG)
	pygame.draw.line(screen, RED, (0, 300), (SCREEN_WIDTH, 300))

#load background
bkg = pygame.image.load('hearts/img/background/background.png').convert_alpha()
backgrnd = pygame.transform.scale(bkg, (SCREEN_WIDTH, SCREEN_HEIGHT))

#load parameters
passed_img_image = pygame.image.load('quiz_trial2/assets/parameters/passed.png').convert_alpha()
passed_img = pygame.transform.scale(passed_img_image, (QUESTION_WIDTH, QUESTION_HEIGHT))

failed_img_image = pygame.image.load('quiz_trial2/assets/parameters/failed.png').convert_alpha()
failed_img = pygame.transform.scale(failed_img_image, (QUESTION_WIDTH, QUESTION_HEIGHT))

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

#button class
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

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action



#create button instances
yes_button = Button((SCREEN_WIDTH / 2) / 2, 600, yes_img)
no_button = Button((SCREEN_WIDTH / 2) + (SCREEN_WIDTH / 6), 600, no_img)

#question 1 class
#class Question_1():
    #screen.blit(Q1_img, (QUESTION_X, QUESTION_Y))
    #yes_button.draw()
    #no_button.draw()

def Question_1():
    points = 0
    screen.blit(Q1_img, (QUESTION_X, QUESTION_Y))
    if yes_button.draw() == True:
        points
        print (points)
        Q1_img.fill(transparent)
        draw_bg()
    elif no_button.draw() == True:
        points += 1
        print (points)
        Q1_img.fill(transparent)
        draw_bg()
    
    


run = True
while run:
    clock.tick(FPS)
    
    draw_bg()
    screen.blit(backgrnd, (0,0))

    #add if statement for collision here
    #draw questions here
    Question_1()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()