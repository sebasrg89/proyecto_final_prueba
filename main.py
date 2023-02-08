import pygame as pg
from pygame.locals import *
import random
import time
import sys

pg.init()

FPS = 60
framesPerSec = pg.time.Clock()

NEGRO = (0,0,0)
BLANCO = (255,255,255)
VERDE = (0,128,94)
ROJO = (255,0,0)

pantalla = pg.display.set_mode((800,530))
pantalla.fill(NEGRO)
pg.display.set_caption("StarRun")

velocidad = 10

pantalla_ancho, pantalla_alto = pg.display.get_surface().get_size()

from pygame import mixer
mixer.init()
mixer.music.load("songs/partida.wav")
mixer.music.play()

class Meteoritos(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("images/asteroide_mediano.png")
        self.surf = pg.Surface((40,40))
        self.rect = self.surf.get_rect(center = (random.randint(40,500), (random.randint(-100,0))))

    def mover(self, score):
        self.rect.move_ip(0, velocidad)
        if (self.rect.bottom > 530):
            self.rect.center = (random.randint(30,460), (random.randint(-100,0)))
            score += 1
        return score

    def dibujar(self, surface):
        surface.blit(self.image, self.rect)

class Nave(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("images/nave.png")
        self.surf = pg.Surface((50,80))
        self.rect = self.surf.get_rect(center = (400,265))

    def dibujar(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        pressedKeys = pg.key.get_pressed()

        if self.rect.left > 0:
            if pressedKeys[K_LEFT]:
                self.rect.move_ip(-5,0)
        
        if self.rect.right < pantalla_ancho:
            if pressedKeys[K_RIGHT]:
                self.rect.move_ip(5,0)

class Fondo_Pantalla():
    def __init__(self):
        self.fondoPartida = pg.image.load("images/partida.png")
        self.rectFPimage = self.fondoPartida.get_rect()

        self.fpY1 = 0
        self.fpX1 = 0

        self.fpY2 = -self.rectFPimage.height
        self.fpX2 = 0
        
        self.moveSpeed = 5

    def update(self):
        self.fpY1 += self.moveSpeed
        self.fpY2 += self.moveSpeed

        if self.fpY1>self.rectFPimage.height:
            self.fpY1 = -self.rectFPimage.height

        if self.fpY2>self.rectFPimage.height:
            self.fpY2 = -self.rectFPimage.height
    
    def render(self):
        pantalla.blit(self.fondoPartida,(self.fpX1,self.fpY1))
        pantalla.blit(self.fondoPartida,(self.fpX2,self.fpY2))

fondo_pantalla = Fondo_Pantalla()

Incremento_Velocidad = pg.USEREVENT + 1
pg.time.set_timer(Incremento_Velocidad, 3000)

N1 = Nave()
M1 = Meteoritos()
M2 = Meteoritos()
M3 = Meteoritos()


meteoritosGrupo = pg.sprite.Group()
meteoritosGrupo.add(M1)
meteoritosGrupo.add(M2)
meteoritosGrupo.add(M3)


fuente = pg.font.SysFont("Verdana", 60)
gameOver = fuente.render("Game Over", True, BLANCO)

score = 0

while True:
    scoreRender = fuente.render("Score: " +str(score), True, ROJO)
    fondo_pantalla.update()
    fondo_pantalla.render()
    pantalla.blit(scoreRender, (0,0))
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
        
        if event.type == Incremento_Velocidad:
            velocidad += 0.5
        
    if pg.sprite.spritecollide(N1, meteoritosGrupo, 0):
        pantalla.fill(NEGRO)
        pantalla.blit(gameOver, (250,235))
        pg.display.update()
        time.sleep(2)
        pg.quit()
    '''
    for meteorito in meteoritosGrupo:
        score = Meteoritos.mover(score)
        Meteoritos.dibujar(pantalla)
    '''
    N1.update()
    score = M1.mover(score)
    score = M2.mover(score)
    score = M3.mover(score)

    N1.dibujar(pantalla)
    M1.dibujar(pantalla)
    M2.dibujar(pantalla)
    M3.dibujar(pantalla)


    pg.display.update()
    framesPerSec.tick(FPS)

