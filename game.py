import pygame
import sys
from player import Player
import obstacle

pygame.init()


# Screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)


class Game:
    def __init__(self):
        # Player setup
        player_sprite = Player(
            (SCREEN_WIDTH/2, SCREEN_HEIGHT), SCREEN_WIDTH, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # Obstacle setup
        self.shape = obstacle.shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.create_obstacle(40, 480)

    def create_obstacle(self, x_start, y_start):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == 'x':
                    x = x_start + col_index * self.block_size
                    y = y_start + row_index * self.block_size
                    block = obstacle.Block(self.block_size, RED, x, y)
                    self.blocks.add(block)

    def create_mult_obst(self, x_start, y_start, *offset):
        for x in offset:
            self.create_obstacle()

    def run(self):
        self.player.draw(screen)

        self.player.sprite.lasers.draw(screen)
        self.player.update()

        self.blocks.draw(screen)
        # Update all sprite groups
        # Draw all sprite groups


game = Game()

while True:
    screen.fill((BLACK))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    game.run()

    clock.tick(60)

    pygame.display.update()
