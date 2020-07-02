import sys

import pygame
import random
import math
import time
from pygame.locals import *

from objects import Cactus, Bird
from dinosaur import Dinosaur

pygame.init()


class Game:
    def __init__(self):
        pygame.display.set_caption('Dinosaur Game')
        self.clock = pygame.time.Clock()
        self.height = 400
        self.width = 700
        self.screen_res = [self.width, self.height]
        self.screen = pygame.display.set_mode(self.screen_res, pygame.HWSURFACE, 32)
        self.white = [222, 222, 222]
        self.black = [0, 0, 0]
        self.screen.fill(self.white)
        self.font = pygame.font.SysFont("Calibri", 16)
        self.ground_y = 250
        self.end = False
        self.obj_speed = 2.5
        self.dinosaur = Dinosaur(self)
        self.cactus_group = pygame.sprite.Group()
        self.collide = False
        self.object_period = 5
        self.current_obj = None
        self.score = 0
        self.add_speed = 5
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
        self.draw_line()
        self.draw_dinosaur()
        self.draw_objects()

    def draw_line(self):
        pygame.draw.aaline(self.screen, self.black, (0, self.ground_y), (self.width, self.ground_y))

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
                    self.dinosaur.set_speed_zero()
            if self.dinosaur.direction == 'down':
                self.dinosaur.move_down()
                if self.dinosaur.check_reached_down():
                    self.dinosaur.direction = 'up'
                    self.dinosaur.reset_speed()
                    self.dinosaur.is_jumping = False
        self.dinosaur.update()

    def create_object(self):
        self.score += 1
        self.update_object_speed()
        random_number = random.randrange(2)
        if random_number == 0:
            collide_object = Cactus(self)
        else:
            collide_object = Bird(self)
        return collide_object

    def init_objects(self):
        if self.current_obj:
            if self.current_obj.x < self.get_appear_position():
                self.current_obj = self.create_object()
        else:
            self.current_obj = self.create_object()

    def update_object_speed(self):
        if self.score % self.add_speed == 0:
            self.obj_speed += 0.3

    def draw_objects(self):
        self.init_objects()
        self.current_obj.check_collide()
        if self.collide:
            self.end = True
        else:
            self.current_obj.move()
        self.current_obj.update()

    @staticmethod
    def get_appear_position():
        return 2 * random.randrange(-5, 5)


Game()
