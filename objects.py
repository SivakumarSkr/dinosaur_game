import pygame
import random


class CollideObject:

    def __init__(self, game):
        self.game = game
        self.x = self.game.width
        self.speed = self.game.obj_speed
        self.dinosaur = self.game.dinosaur

    def move(self):
        print(self.x, self.y)
        self.x += self.speed

    def check_passed(self):
        if self.x + self.width < 0:
            return True

    def check_collide(self):
        if self.x > self.dinosaur.x + self.dinosaur.width:
            self.game.collide = True


class Cactus(CollideObject):
    def __init__(self, game):
        super().__init__(game)
        self.type = self.select_type()
        self.height, self.width = [40 + self.type[0] * 10] * 2
        self.y = game.ground_y - self.height
        self.scale = (self.height, self.width)
        self.pos = (self.x, self.y)
        self.image = pygame.image.load(self.select_image(self.type[1]))
        self.cactus = pygame.transform.scale(self.image, self.scale)
        self.game.screen.blit(self.cactus, (self.x, self.y))

    @staticmethod
    def select_type():
        return random.randrange(3), random.randrange(2)

    @staticmethod
    def select_image(image):
        return 'cactus{}.png'.format(image)

    def update(self):
        self.game.screen.blit(self.cactus, (self.x, self.y))


class Bird(CollideObject):
    def __init__(self, game):
        super().__init__(game)
        self.y = game.ground_y - self.select_x()
        self.height, self.width = (20, 20)
        self.scale = (self.height, self.width)
        self.image = pygame.image.load('bird.png')
        self.bird = self.cactus = pygame.transform.scale(self.image, self.scale)
        self.game.screen.blit(self.bird, (self.x, self.y))

    def select_x(self):
        random_number = random.randrange(3)
        dino_height_half = self.game.dinosaur.height / 2
        return random_number * dino_height_half

    def update(self):
        self.game.screen.blit(self.bird, (self.x, self.y))
