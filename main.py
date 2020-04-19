import sys

import pygame
import random
import math
from pygame.locals import *

from dinosaur import Dinosaur

pygame.init()


class Game:
    def __init__(self):
        pygame.display.set_caption('Dinosaur Game')
        self.clock = pygame.time.Clock()
        self.screen_res = [700, 400]
        self.screen = pygame.display.set_mode(self.screen_res, pygame.HWSURFACE, 32)
        self.white = [222, 222, 222]
        self.screen.fill(self.white)
        self.font = pygame.font.SysFont("Calibri", 16)

        self.end = False
        self.dinosaur = Dinosaur(self)
        while not self.end:
            self.loop()

    def loop(self):
        self.event_loop()
        self.draw()
        pygame.display.update()
        self.clock.tick(60)

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def draw(self):
        self.screen.fill(self.white)
        self.draw_dinosaur()

    def draw_dinosaur(self):
        keys = pygame.key.get_pressed()
        if not self.dinosaur.is_jumping:
            if keys[pygame.K_SPACE]:
                self.dinosaur.is_jumping = True
                self.dinosaur.direction = 'up'

        if self.dinosaur.is_jumping:
            if self.dinosaur.direction == 'up':
                self.dinosaur.move_up()
                if self.dinosaur.check_reached_top():
                    self.dinosaur.direction = 'down'
            if self.dinosaur.direction == 'down':
                self.dinosaur.move_down()
                if self.dinosaur.check_reached_down():
                    self.dinosaur.direction = 'up'
                    self.dinosaur.is_jumping = False
        self.dinosaur.update()


Game()