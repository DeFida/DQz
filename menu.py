import random
import os
import sys
import pygame
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QRadioButton
import math
    

class RecDialog(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('record.ui', self)

        recor = open('data/records.txt', mode="r", encoding="utf8")
        lines = recor.readlines()
        self.rec = int(lines[0])
        self.label_record.setText('Current record is ' + str(self.rec)) 


class Restart(QWidget):
    def __init__(self, score):
        super().__init__()
        self.score = score
        uic.loadUi('aftercol.ui', self)
        self.lineEdit.hide()
        self.ar.hide()
        self.bs.hide()
        self.ok.hide()
        self.iq = 0
        self.reco = open('data/records.txt', mode="r", encoding="utf8")
        self.rec = int(self.reco.readlines()[0])
        if self.score > self.rec:
            self.wrec = open('data/records.txt', mode="w", encoding="utf8")
            self.wrec.write(str(int(self.score)))
        self.label_score.setText('Your score is ' + str(int(self.score)))
        self.add.clicked.connect(self.addscore)
        self.restartb.clicked.connect(self.restart)
        self.ok.clicked.connect(self.tecs)
        self.res = False
        self.ques = ['Синоним к слову "Мәлімет"', 'Антоним к слову "Керемет"', 'Ононим к слову "Ара"', 'Синоним к слову "Нашар"', 'Антоним к слову "Қараңғы"']
        self.ars = ['1) Мағлұмат', '1) Ғажап', '1) Маса', '1) Жаман', '1) Түн']
        self.bss = ['2) Термин', '2) Нашар', '2) Ара', '2) Керемет', '2) Жарық']

    def tecs(self):
        ans = [1, 2, 2, 1, 2]
        if int(self.lineEdit.text()) == ans[self.iq]:
            self.score += 100
            self.iq += 1
            if self.iq == 5:
                if self.score > self.rec:
                    print(self.score)
                    self.wrec = open('data/records.txt', mode="w", encoding="utf8")
                    self.wrec.write(str(int(self.score)))
                self.lineEdit.hide()
                self.ar.hide()
                self.bs.hide()
                self.ok.hide()
                self.restartb.show()
                self.restartb.move(160, 80)
                self.label_score.move(150, 30)
                self.label_score.setText('Your score is ' + str(int(self.score)))
            else:
                self.ar.setText(self.ars[self.iq])
                self.bs.setText(self.bss[self.iq])
                self.label_score.setText(self.ques[self.iq])
                self.lineEdit.clear()
        else:
            if self.score > self.rec:
                self.wrec = open('data/records.txt', mode="w", encoding="utf8")
                self.wrec.write(str(int(self.score)))
            self.lineEdit.hide()
            self.ar.hide()
            self.bs.hide()
            self.ok.hide()
            self.restartb.show()
            self.restartb.move(160, 80)
            self.label_score.move(150, 30)
            self.label_score.setText('Your score is ' + str(int(self.score)))
        

    def restart(self):
        if self.score > self.rec:
            self.wrec = open('data/records.txt', mode="w", encoding="utf8")
            self.wrec.write(str(int(self.score)))
        self.t = MyWidget()
        self.close()
        self.t.start_the_game()

    def addscore(self):
        self.ar.show()
        self.bs.show()
        self.ar.setText(self.ars[self.iq])
        self.bs.setText(self.bss[self.iq])
        self.label_score.move(90, 30)
        self.label_score.setText(self.ques[0])
        self.add.hide()
        self.restartb.hide()
        self.lineEdit.show()
        self.ok.show()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        
        self.startb.clicked.connect(self.start_the_game)
        self.quitb.clicked.connect(self.close_the_app)
        self.recb.clicked.connect(self.show_rec)
        self.running = True
        self.run = True

    def return_to_menu(self, score):
        self.run = False
        self.re = Restart(score)
        self.re.show()
    
    def start_the_game(self):
        self.close()
        recor = open('data/records.txt', mode="r", encoding="utf8")
        lines = recor.readlines()
        rec = int(lines[0])
        pygame.init()
        size = width, height = 600, 400
        screen = pygame.display.set_mode(size)
        self.running = True
        self.run = True
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
            the_centre = ((the_first[2] - the_first[0]) // 2)
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

        #all aprites

        back = load_image('background.png', (255, 255, 255))

        #pos of enemy
        poses = [235, 280, 325, 300, 295, 260, 270, 290, 335, 330, 250]

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

        while self.running:
            screen.fill((196, 223, 229, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass
            
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_RIGHT]:
                x += velo * 0.5
            if pressed[pygame.K_LEFT]:
                x -= velo * 0.5
            if pressed[pygame.K_p]:
                self.return_to_menu(score)
            
            if self.run:
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
                    self.run = False
                    self.return_to_menu(score)

            # update anau mnau
            screen.blit(back, (0, 0))
            player.render(x, y)
            eny.render(x_of_enemy, y_of_enemy)
            eny2.render(x_of_enemy2, y_of_enemy2)
            score_text(score)
            speed_text(velo)
            rec_text(rec, score)

            pygame.display.flip()
        print(score)
        print(velo)
        pygame.quit()

    def close_the_app(self):
        self.close()

    def show_rec(self):
        self.r = RecDialog()
        self.r.show()





app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec())
recor.close()
reco.close()
wrec.close()