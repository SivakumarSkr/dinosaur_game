import pygame


class Dinosaur:
    def __init__(self, game):
        self.game = game
        self.height = 50
        self.width = 50
        self.scale = (self.height, self.width)
        self.init_x = 70
        self.init_y = self.game.ground_y - self.height
        self.x = self.init_x
        self.y = self.init_y
        self.top_point = 100
        self.is_jumping = False
        self.speed = 4
        self.position = (self.x, self.y)
        self.image = pygame.image.load('dinosaur.png')
        self.dino = pygame.transform.scale(self.image, self.scale)
        self.game.screen.blit(self.dino, (self.x, self.y))

    def update(self):
        self.game.screen.blit(self.dino, (self.x, self.y))

    def move_up(self):
        self.y -= self.speed

    def move_down(self):
        self.y += self.speed

    def check_reached_top(self):
        return self.y < self.init_y - self.top_point

    def check_reached_down(self):
        return self.y > self.init_y

    def speed_boost(self):
        self.speed += 0.1
