import pygame
import random


class CollideObject:

    def __init__(self, game):
        self.game = game
        self.x = self.game.width
        self.speed = self.game.obj_speed
        self.dinosaur = self.game.dinosaur

    def move(self):
        self.x -= self.speed

    def check_passed(self):
        if self.x + self.width < 0:
            return True

    def check_collide(self):
        if self.x < self.dinosaur.x + self.dinosaur.width and self.x + self.width > self.dinosaur.x and self.y < self.dinosaur.y + self.dinosaur.height and \
                self.y + self.height > self.dinosaur.y:
            self.game.collide = True


class Cactus(CollideObject):
    def __init__(self, game):
        super().__init__(game)
        self.type = self.select_type()
        self.height, self.width = [30 + self.type[0] * 10] * 2
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
        self.height, self.width = (30, 30)
        self.scale = (self.height, self.width)
        self.image = pygame.image.load('bird.png')
        self.bird = pygame.transform.scale(self.image, self.scale)
        self.game.screen.blit(self.bird, (self.x, self.y))

    def select_x(self):
        random_number = random.choice([1, 3])
        dino_height_half = self.game.dinosaur.height * 3 / 4
        return random_number * dino_height_half

    def update(self):
        self.game.screen.blit(self.bird, (self.x, self.y))


class Cloud:
    def __init__(self, game):
        self.game = game
        self.y = self.select_x()
        self.x = game.width
        self.height, self.width = 50, 50
        self.speed = game.obj_speed / 2
        self.scale = (self.height, self.width)
        self.image = pygame.image.load(self.random_image())
        self.cloud = pygame.transform.scale(self.image, self.scale)
        self.game.screen.blit(self.cloud, (self.x, self.y))

    @staticmethod
    def select_x():
        return random.choice([50, 55, 60])

    @staticmethod
    def random_image():
        return random.choice(['cloud1.png', 'cloud2.png'])

    def update(self):
        self.x -= self.speed
        self.game.screen.blit(self.cloud, (self.x, self.y))

    def check_passed(self):
        if self.x + self.width < 0:
            return True



