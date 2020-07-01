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
        self.init_speed = 5
        self.speed = self.init_speed
        self.accelerate = 0.1
        self.position = (self.x, self.y)
        self.image = pygame.image.load('dinosaur.png')
        self.dino = pygame.transform.scale(self.image, self.scale)
        self.game.screen.blit(self.dino, (self.x, self.y))

    def update(self):
        self.game.screen.blit(self.dino, (self.x, self.y))

    def move_up(self):
        self.deceleration()
        self.y -= self.speed

    def move_down(self):
        self.acceleration()
        self.y += self.speed

    def check_reached_top(self):
        return self.speed <= 0

    def check_reached_down(self):
        return self.y > self.init_y

    def deceleration(self):
        self.speed -= self.accelerate

    def acceleration(self):
        self.speed += self.accelerate

    def set_speed_zero(self):
        self.speed = 0

    def reset_speed(self):
        self.speed = self.init_speed
