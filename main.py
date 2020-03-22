import pygame 
import os 
import random 
import math

#pygame window init.
recor = open('data/records.txt', mode="r", encoding="utf8")
lines = recor.readlines()
rec = int(lines[0])
print(rec)
pygame.init()
size = width, height = 600, 400
screen = pygame.display.set_mode(size)
running = True
run = True
pygame.display.set_caption('Angry py')

#functions
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

def score_text(score):
    score = score
    font = pygame.font.Font(None, 30)
    text = font.render('Score: ' + str(int(score)), 1, (250, 250, 0))
    screen.blit(text, (60, 30))

def speed_text(speed):
    speed = speed
    font = pygame.font.Font(None, 30)
    text = font.render('Speed: ' + str(int(float(str(speed)[0:4]) * 100)), 1, (250, 250, 0))
    screen.blit(text, (60, 60))

def rec_text(rec, sc):
    reco = rec
    font = pygame.font.Font(None, 30)
    if sc < rec:
        text = font.render('Record: ' + str(reco), 1, (250, 250, 0))
    else:
        text = font.render('Record: ' + str(int(sc)), 1, (250, 250, 0))
    screen.blit(text, (60, 90))

def surak(n):
    font = pygame.font.Font(None, 20)
    if n == 0:
        pass
    elif n == 1:
        text = font.render('Антоним к слову: Керемет', 1, (250, 250, 0))
        text2 = font.render('a) Нашар', 1, (250, 250, 0))
        text3 = font.render('b) Ғажап', 1, (250, 250, 0))
        screen.blit(text, (380, 50))
        screen.blit(text2, (380, 80))
        screen.blit(text3, (380, 110))

    elif n == 2:
        text = font.render('Синоним к слову: Мәлімет', 1, (250, 250, 0))
        text2 = font.render('b) Мағлұмат', 1, (250, 250, 0))
        text3 = font.render('a) Термин', 1, (250, 250, 0))
        screen.blit(text, (380, 50))
        screen.blit(text2, (380, 110))
        screen.blit(text3, (380, 80))


def zhauap(k):
    y = True
    if n_su == 1:
        if k == 1:
            y = True
        else:
            y = False
    elif n_su == 2:
        if k == 2:
            y = True
        else:
            y = False
    return y 
#all aprites

back = load_image('background.png', (255, 255, 255))

#pos of enemy
poses = [235, 280, 325, 300, 295, 260, 270]

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

class enemy2():
    def __init__(self):
        self.x = int()
        self.y = 330
        self.enemy = load_image('enemy2.png', -1)

    def render(self, x, y):
        self.x = x
        self.y = y
        screen.blit(self.enemy, (self.x, self.y))

    def get_chara(self):
        return (self.x, self.y + 30, self.x + 30, self.y + 30)

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
eny2 = enemy2()

x_of_enemy = random.choice(poses)
y_of_enemy = 0

x_of_enemy2 = random.choice(poses)
y_of_enemy2 = -600

velo = 0.8

clock = pygame.time.Clock()

n_su = 0

bs = 1
es = 2
us = 3

score = 0

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
        x += velo * 0.5
    if pressed[pygame.K_LEFT]:
        x -= velo * 0.5
    if pressed[pygame.K_p]:
        run = False
    if pressed[pygame.K_s]:
        run = True
    if pressed[pygame.K_a]:
        if zhauap(1):
            run = True
            velo = 0.8
            y_of_enemy = 0
            y_of_enemy2 = -600
            n_su = 0
        else:
            if rec < score:
                wrecor = open('data/records.txt', mode="w", encoding="utf8")
                wrecor.write(str(int(score)))

    if pressed[pygame.K_b]:
        if zhauap(2):
            velo = 0.8
            y_of_enemy = 0
            y_of_enemy2 = -600
            n_su = 0
        else:
            if rec < score:
                wrecor = open('data/records.txt', mode="w", encoding="utf8")
                wrecor.write(str(int(score)))
    
    if run:
        velo += clock.tick() / 50500
        score += velo * 0.1

        y_of_enemy += velo
        y_of_enemy2 += velo

        if y_of_enemy >= 400:
            y_of_enemy = 0
            x_of_enemy = random.choice(poses)
        x_of_enemy = x_of_enemy

        if y_of_enemy2 >= 400:
            y_of_enemy2 = 0
            x_of_enemy2 = random.choice(poses)
        x_of_enemy2 = x_of_enemy2

        if x <= 232:
            x = 232
        elif x >= 338:
            x = 338

        if is_col(eny, player) or is_col(eny2, player) or is_col(player, eny2):
            velo = 0
            n_su = random.randint(1, 2)
            run = False

    # update anau mnau
    screen.blit(back, (0, 0))
    player.render(x, y)
    eny.render(x_of_enemy, y_of_enemy)
    eny2.render(x_of_enemy2, y_of_enemy2)
    score_text(score)
    speed_text(velo)
    rec_text(rec, score)
    surak(n_su)

    pygame.display.flip()
print(score)
print(velo)
pygame.quit()