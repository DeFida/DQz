import pygame 
import os 
import random 
import math

#pygame window init.

pygame.init()
size = width, height = 600, 400
screen = pygame.display.set_mode(size)
running = True
pygame.display.set_caption('Angry py')

#load image function
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

def is_col(the_first, the_second):
    the_first = the_first.get_chara()
    the_second = the_second.get_chara()
    if (the_second[0] < the_first[0] < the_second[2] \
        and the_second[1] < the_first[1] < the_second[3]) \
            or (the_second[0] < the_first[2] < the_second[2] \
        and the_second[1] < the_first[3] < the_second[3]):
        return True
    else:
        return False


#all aprites

back = load_image('background.png', (255, 255, 255))


#pos of enemy
poses = [235, 280, 325]

class enemy():
    def __init__(self):
        self.x = int()
        self.y = 330
        self.enemy = load_image('enemies.png', -1)

    def render(self, x, y):
        self.x = x
        self.y = y
        screen.blit(self.enemy, (self.x, self.y))

    def get_chara(self):
        return (self.x, self.y + 20, self.x + 20, self.y + 20)


class pyPlayer():
    def __init__(self):
        self.x = 280
        self.y = 330
        self.pyPlayer = load_image('pyPlayer.png', -1)

    def render(self, x, y):
        self.x = x
        self.y = y
        screen.blit(self.pyPlayer, (self.x, self.y))

    def get_chara(self):
        return (self.x, self.y, self.x + 20, self.y + 20)


player = pyPlayer()
eny = enemy()

x_of_enemy = random.choice(poses)
y_of_enemy = 0

velo = 0.5

x = 280
y = 330
while running:
    screen.fill((196, 223, 229, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT]:
        x += velo * 0.4
    if pressed[pygame.K_LEFT]:
        x -= velo * 0.4

    y_of_enemy += velo

    if y_of_enemy >= 400:
        y_of_enemy = 0
        x_of_enemy = random.choice(poses)
    x_of_enemy = x_of_enemy

    if x <= 232:
        x = 232
    elif x >= 338:
        x = 338

    if is_col(eny, player):
        running = False
    # update anau mnau
    screen.blit(back, (0, 0))
    player.render(x, y)
    eny.render(x_of_enemy, y_of_enemy)
    pygame.display.flip()

pygame.quit()