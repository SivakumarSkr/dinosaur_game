import time

import pygame
from pygame.locals import *


class EndGame:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    def __init__(self, game):
        self.game = game
        self.end = False
        self.quit = False
        self.screen_init()

    def screen_init(self):
        self.message_display(40, self.game.width / 2, self.game.height / 2, 'Game over')
        time.sleep(2)
        self.print_screen()
        while not self.end:
            self.loop()

    def loop(self):
        self.event_loop()
        pygame.display.update()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.end = True
                    self.quit = True
                if event.key == pygame.K_SPACE:
                    self.end = True
                    self.quit = False

    def message_display(self, size, x, y, text):
        large_text = pygame.font.SysFont(None, size)
        text_surf = large_text.render(text, True, self.BLACK)
        text_rect = text_surf.get_rect()
        text_rect.center = (x, y)
        self.game.screen.blit(text_surf, text_rect)
        pygame.display.update()

    def print_screen(self):
        self.game.screen.fill(self.WHITE)
        self.message_display(40, self.game.width / 2, self.game.height / 2, 'Game over')
        self.message_display(30, self.game.width / 2, self.game.height / 2 + 60, 'Click Space for Restart')
        self.message_display(30, self.game.width / 2, self.game.height / 2 + 90,  'Click Esc for Quit')
        self.message_display(30, self.game.width / 2, self.game.height / 2 + 120, 'Score :' + str(self.game.score))

