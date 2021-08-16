import os
import random
import pygame
pygame.init()

# first display 
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
gameDisplay.fill((0,255,0)) # green
pygame.display.set_caption("Rock-Paper-scissors")

# colors
black = (0,0,0)
white = (255,255,255)
red =(255,0,0)
green = (0,255,0)
blue = (0,0,255)

# 2 objects in left and right
x_left = display_width/4
x_right = display_width*3/4
y_left = display_height/2
y_right = display_height/2
y_choice = display_height/3

clock = pygame.time.Clock()
CURR_DIR = os.path.dirname(os.path.realpath(__file__))

# photos
r_path =CURR_DIR+"\\R.png"
r_img = pygame.image.load(r_path)
p_path =CURR_DIR+"\\P.png"
p_img = pygame.image.load(p_path)
s_path =CURR_DIR+"\\S.png"
s_img = pygame.image.load(s_path)
sR_path = CURR_DIR + "\\SR.png"
sR_img = pygame.image.load(sR_path)

# feeling photos
win_path = CURR_DIR + "\\win.png"
win_img = pygame.image.load(win_path)
lose_path = CURR_DIR + "\\lose.png"
lose_img = pygame.image.load(lose_path)
equal_path = CURR_DIR + "\\equal.png"
equal_img = pygame.image.load(equal_path)
eq_path = CURR_DIR + "\\eq.png"
eq_img = pygame.image.load(eq_path)
emo_path = CURR_DIR + "\\emo.png"
emo_img = pygame.image.load(emo_path)



# move methods
def moveRight( leftIMG , rightIMG):
    for i in range(0 ,int(display_width/2)-150 , 5):# s_img.width = (150)
        gameDisplay.fill(blue)
        gameDisplay.blit(rightIMG,(x_right-150, y_right))
        gameDisplay.blit(lose_img,(x_right-122, y_right))
        gameDisplay.blit(leftIMG,(x_left+i, y_left))
        gameDisplay.blit(win_img,(x_left+i+27, y_left))
        pygame.display.update()
        clock.tick(35)

def moveLeft( leftIMG , rightIMG):
    for i in range(150 ,int(display_width/2) , 5):# s_img.width = (150)
        gameDisplay.fill(red)
        gameDisplay.blit(leftIMG,(x_left, y_left))
        gameDisplay.blit(lose_img,(x_left+27, y_left))
        gameDisplay.blit(rightIMG,(x_right-i, y_right))
        gameDisplay.blit(win_img,(x_right-i+27, y_right))
        pygame.display.update()
        clock.tick(35)

def equal(img):
    gameDisplay.fill(white)
    gameDisplay.blit(img,(x_left, y_left))
    gameDisplay.blit(equal_img,(x_left+27, y_left))
    if img == s_img:
        img = sR_img
    gameDisplay.blit(img,(x_right-150, y_right))
    gameDisplay.blit(equal_img,(x_right-122, y_right))
    gameDisplay.blit(eq_img,(display_width/2-37 , y_right+25))
    pygame.display.update()
    clock.tick(1) 

def choiceDisplay():
    gameDisplay.fill(green)
    gameDisplay.blit(r_img,(display_width*1/4-75, y_choice))
    gameDisplay.blit(emo_img,(display_width*1/4-75, y_choice-10))
    gameDisplay.blit(p_img,(display_width*2/4-75, y_choice))
    gameDisplay.blit(emo_img,(display_width*2/4-75, y_choice))
    gameDisplay.blit(s_img,(display_width*3/4-75, y_choice))
    gameDisplay.blit(emo_img,(display_width*3/4-100, y_choice-20))
    pygame.display.update()

def userChoice(x):
    if 125<=x and x<=275:
        return "rock"
    if 325<=x and x<=475:
        return "paper"
    if 525<=x and x<=675:
        return "scissors"
    
def compete( user , comp ):
    if user == "rock":
        if comp == "rock":
            equal(r_img)

        if comp == "paper":
            moveLeft(r_img , p_img)

        if comp == "scissors":
            moveRight(r_img , sR_img)

    
    if user == "paper":
        if comp == "rock":
            moveRight(p_img , r_img)

        if comp == "paper":
            equal(p_img)

        if comp == "scissors":
            moveLeft(p_img , sR_img)

    
    if user == "scissors":
        if comp == "rock":
            moveLeft(s_img , r_img)

        if comp == "paper":
            moveRight(s_img , p_img)

        if comp == "scissors":
            equal(s_img)

# main func.
toBeContinued = True

while toBeContinued :
    comp_choice = random.choice(["rock" , "paper" ,"scissors"])
    
    choiceDisplay()

    notClicked = True
    while notClicked:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                toBeContinued = False
                notClicked = False
                break

            if event.type == pygame.MOUSEBUTTONUP:
                user_choice = userChoice(pygame.mouse.get_pos()[0])
                notClicked = False
                break

            clock.tick(20)

    if toBeContinued == False:
        break

    compete(user_choice , comp_choice)

    