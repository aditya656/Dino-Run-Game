import pygame
import math

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("PyGame project SEM4")

cactusImg = [pygame.image.load('Assets/Images/cactus1.png'), pygame.image.load('Assets/Images/cactus2.png'), pygame.image.load('Assets/Images/cactus3.png'),
             pygame.image.load('Assets/Images/cactus4.png')]
dinoImg = [pygame.image.load('Assets/Images/dino1.png'), pygame.image.load('Assets/Images/dino2.png'), pygame.image.load('Assets/Images/dino3.png'),
           pygame.image.load('Assets/Images/dinoDead.png')]
groundImg = pygame.image.load('Assets/Images/ground2.png')
backgroundImg = pygame.image.load('Assets/Images/bg.png')

# dino position
dinoX = 50
dinoY = 304
leg = 0
jumpCount = 8
isJump = False
legShift = True

# ground position
groundX = 0
groundY = 331
vel = 10
groundMove = False
counter = 0

# cactus position
cactusX = 500
cactusY = 300
cactusNo = 0

#cloud position
cloudX = 400
cloudY = 100


font = pygame.font.Font('Assets/Font/font1.ttf', 32)
textX = 30
textY = 30

clock = pygame.time.Clock()

def score(x, y):
    score = font.render("SCORE : " + str(counter), True, (56, 56, 56))
    screen.blit(score, (x, y))

def dino():
    global legShift
    global counter
    if legShift and groundMove:
        screen.blit(dinoImg[1], (dinoX, dinoY))
        if counter % 8 == 0:
            legShift = False
        if groundMove:
            counter = counter + 2

    else:
        screen.blit(dinoImg[2], (dinoX, dinoY))
        if groundMove:
            counter = counter + 2
        if counter % 9 == 0:
            legShift = True

def ground():
    screen.blit(groundImg, (groundX, groundY))

def cactus():
    global cactusNo
    screen.blit(cactusImg[cactusNo], (cactusX, cactusY))

def cloud(x,y):
    screen.blit(pygame.image.load('Assets/Images/cloud.png'),(x,y))
def gameStart():
    global groundMove
    groundMove = True

def startScreen():
    screen.blit(pygame.image.load('Assets/Images/startImg.png'), (150, 100))

run = True
# game Loop
while run:
    screen.blit(backgroundImg, (0, 0))
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(backgroundImg, (0, 0))

    ground()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:  # press space to start
        gameStart()
    if keys[pygame.K_ESCAPE]:  # press esc to exit game
        run = False

    if not isJump:
        if keys[pygame.K_UP] or keys[pygame.K_SPACE]:  # up arrow or space key to jump
            isJump = True
    else:
        if jumpCount >= -8:
            neg = 1
            if jumpCount < 0:
                neg = -1
            dinoY -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 8
    if not groundMove:
        startScreen()

    score(textX, textY)

    # game over
    dist = math.sqrt(math.pow((dinoX - cactusX), 2) + math.pow((dinoY - cactusY), 2))
    if dist <= 40:
        screen.blit(pygame.image.load('Assets/Images/game_over.png'), (110, 100))
        vel = 0
        isJump = False
        legShifting = False
        groundMove = False

    if groundMove:
        dino()
        cloud(cloudX,cloudY)
    elif counter != 0:
        screen.blit(dinoImg[3], (dinoX, dinoY))
    else:
        screen.blit(dinoImg[0],(dinoX,dinoY))

    cactus()
    pygame.display.update()

    # ground movement
    if groundMove and (groundX > -1700):
        groundX -= vel
    if groundX <= -1700:
        groundX = 0

    # cactus movement
    if groundMove:
        cactusX -= vel
    if cactusX <= -50:
        cactusX = 600
        if cactusNo <= 2:
            cactusNo = cactusNo + 1
        else:
            cactusNo = 0
    #cloud movement
    if groundMove:
        cloudX -= vel-10
    if cloudX <= -120:
        cloudX = 800

    # increase in velocity of objects
    if (counter % 200 == 2):
        print(counter)
        print(vel)
        vel += 1