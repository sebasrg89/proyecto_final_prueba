import pygame as pg
from pygame.locals import *
import random

pg.init()

FPS = 60
framesPerSec = pg.time.Clock()

NEGRO = (0,0,0)

pantalla = pg.display.set_mode((800,530))
pantalla.fill(NEGRO)
pg.display.set_caption("StarRun")

pantalla_ancho, pantalla_alto = pg.display.get_surface().get_size()

class Meteoritos(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("images/asteroide_mediano.png")
        self.surf = pg.Surface((40,40))
        self.rect = self.surf.get_rect(center = (random.randint(40,460), 0))

    def mover(self):
        self.rect.move_ip(0,10)
        if (self.rect.bottom > 530):
            self.rect.center = (random.randint(30,460), 0)

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

N1 = Nave()
M1 = Meteoritos()

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()

    N1.update()
    M1.mover()

    pantalla.fill(NEGRO)

    N1.dibujar(pantalla)
    M1.dibujar(pantalla)

    pg.display.update()
    framesPerSec.tick(FPS)

