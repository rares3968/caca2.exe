import pygame
import sys
import random
# from tkinter import messagebox
pygame.init()
pygame.mixer.init()
scrn = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
font = pygame.font.SysFont("Arial",48)
pygame.display.set_caption('caca2')
 
if getattr(sys, 'frozen', False):
    caca = pygame.image.load(sys._MEIPASS + "\\resurse\\caca.jpg").convert()
    err = pygame.image.load(sys._MEIPASS + "\\resurse\\eroare.jpg").convert()
    pygame.mixer.music.load(sys._MEIPASS + "\\resurse\\caca.mp3")
    sunet_err = pygame.mixer.Sound(sys._MEIPASS + "\\resurse\\eroare.mp3")
    cac = pygame.mixer.Sound(sys._MEIPASS + "\\resurse\\macac.mp3")
else:
    caca = pygame.image.load("resurse/caca.jpg").convert()
    err = pygame.image.load("resurse/eroare.jpg").convert()
    pygame.mixer.music.load("resurse/caca.mp3")
    sunet_err = pygame.mixer.Sound("resurse/eroare.mp3")
    cac = pygame.mixer.Sound("resurse/macac.mp3")

infoMonitor = pygame.display.Info()
lung = infoMonitor.current_w
lat = infoMonitor.current_h

pygame.mixer.music.play()

unghi = 0
rotari = 0
erori = 0
playErori = True
activat = True
while activat:
    if rotari < 6:
        rotat = pygame.transform.rotate(caca, unghi)
        unghi = unghi +  1
        if unghi > 359:
            unghi = 0
            rotari = rotari + 1
        scrn.blit(rotat, (0,0))
        pygame.display.update()
    else:
        if erori < 1:
            scrn.fill((0,0,0))
        int0 = 0
        timp = 1000
        while erori < 101:
            x = random.randint(0,lung)
            y = random.randint(0,lat)
            pygame.mixer.Sound.play(sunet_err)
            scrn.blit(err,(x,y))
            pygame.display.update()
            erori = erori + 1
            int0 = int0 + 1
            if int0 > 4:
                int0 = 0
                timp = timp - 100
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    activat = False
            pygame.time.delay(timp)
        pygame.display.update()
        if erori > 99:
            scrn.blit(caca,(0,0))
            pygame.display.update()
            for sunet in range(0,5):
                for i in pygame.event.get():
                    if i.type == pygame.QUIT:
                        activat = False
                pygame.mixer.Sound.play(cac)
                x = random.randint(0,lung)
                y = random.randint(0,lat)
                scrn.blit(caca,(x,y))
                pygame.display.update()
                pygame.time.delay(1000)
            pygame.display.update()
            pygame.time.delay(1000)
            scrn.fill((0,0,0))
            pygame.display.update()
            text = font.render('vezi ca m-am cacat in baie', True, (255,255,255))
            text2 = font.render('rares3968, creatorul la caca2.exe', True, (255,255,255))
            scrn.blit(text,(10,10))
            scrn.blit(text2,(10,70))
            pygame.display.update()
            pygame.time.delay(2000)
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    activat = False
            pygame.time.delay(2000)
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    activat = False
            pygame.time.delay(2000)
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    activat = False
            activat = False
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            activat = False
 
pygame.quit()