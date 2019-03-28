import pygame
from time import sleep

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Cubes game")

walkRight = [pygame.image.load('res\pygame_right_1.png'),
             pygame.image.load('res\pygame_right_2.png'),
             pygame.image.load('res\pygame_right_3.png'),
             pygame.image.load('res\pygame_right_4.png'),
             pygame.image.load('res\pygame_right_5.png'),
             pygame.image.load('res\pygame_right_6.png')]

walkLeft = [pygame.image.load('res\pygame_left_1.png'),
            pygame.image.load('res\pygame_left_2.png'),
            pygame.image.load('res\pygame_left_3.png'),
            pygame.image.load('res\pygame_left_4.png'),
            pygame.image.load('res\pygame_left_5.png'),
            pygame.image.load('res\pygame_left_6.png')]

bg = pygame.image.load('res\pygame_bg.jpg')
playerStand = pygame.image.load('res\image.png')

x = 50
y = 425
width = 60
height = 71 
speed = 5

isJump = False
jumpCount = 10

left = False
right = False
animCount = 0

run = True
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 495 - width:
        x += speed

    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
    elif jumpCount >= -10:
        if jumpCount < 0:
            y += (jumpCount ** 2) / 2
        else:
            y -= (jumpCount ** 2) / 2
        jumpCount -= 1
    else:
        isJump = False
        jumpCount = 10

pygame.quit()
